from flask import Flask, render_template, redirect, url_for, request
from models import db, Employee, Department, Shift, Certification, EmployeeCertification, DisciplinaryAction
from forms import SearchForm, NewEmployeeForm, PTOForm, CertificationForm, ActionForm, ShiftForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    employees = []
    if form.validate_on_submit():
        query = form.query.data
        employees = Employee.query.filter(
            (Employee.FirstName.ilike(f'%{query}%')) |
            (Employee.LastName.ilike(f'%{query}%')) |
            (Employee.EmployeeID.like(f'%{query}%'))
        ).all()
    return render_template('index.html', form=form, employees=employees)

@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    form = NewEmployeeForm()
    if form.validate_on_submit():
        new_emp = Employee(
            FirstName=form.FirstName.data,
            LastName=form.LastName.data,
            StartDate=form.StartDate.data,
            Salary=form.Salary.data,
            Status=form.Status.data,
            DepartmentID=form.DepartmentID.data,
            ShiftID=form.ShiftID.data,
            YearsAtCompany=0,
            Strikes=0,
            PTOUsed=0,
            PTORemaining=0,
            HoursWorked=0
        )
        db.session.add(new_emp)
        db.session.commit()
        return redirect(url_for('employee_detail', employee_id=new_emp.EmployeeID))
    return render_template('add_employee.html', form=form)

@app.route('/employee/<int:employee_id>', methods=['GET', 'POST'])
def employee_detail(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    pto_form = PTOForm()
    cert_form = CertificationForm()
    action_form = ActionForm()
    shift_form = ShiftForm()

    if pto_form.submit_add.data and pto_form.validate():
        employee.PTORemaining += pto_form.amount.data
        db.session.commit()
        return redirect(url_for('employee_detail', employee_id=employee_id))

    if pto_form.submit_use.data and pto_form.validate():
        employee.PTOUsed += pto_form.amount.data
        employee.PTORemaining -= pto_form.amount.data
        db.session.commit()
        return redirect(url_for('employee_detail', employee_id=employee_id))

    if cert_form.validate_on_submit():
        new_cert = EmployeeCertification(
            EmployeeID=employee_id,
            CertificationID=cert_form.CertificationID.data,
            DateObtained=cert_form.DateObtained.data
        )
        db.session.add(new_cert)
        db.session.commit()
        return redirect(url_for('employee_detail', employee_id=employee_id))

    if action_form.validate_on_submit():
        new_action = DisciplinaryAction(
            EmployeeID=employee_id,
            ActionType=action_form.ActionType.data,
            ActionDate=action_form.ActionDate.data,
            Description=action_form.Description.data
        )
        db.session.add(new_action)
        db.session.commit()
        return redirect(url_for('employee_detail', employee_id=employee_id))

    if shift_form.validate_on_submit():
        employee.ShiftID = shift_form.ShiftID.data
        db.session.commit()
        return redirect(url_for('employee_detail', employee_id=employee_id))

    return render_template('employee_detail.html', employee=employee,
                           pto_form=pto_form, cert_form=cert_form,
                           action_form=action_form, shift_form=shift_form)

@app.route('/initdb')
def init_db():
    db.create_all()
    return "Database initialized!"


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
