from flask import Flask, render_template, redirect, url_for, request
from models import db, Employee, Department, Shift, Certification, EmployeeCertification, DisciplinaryAction
from forms import SearchForm, NewEmployeeForm, PTOForm, CertificationForm, ActionForm, ShiftForm
from config import Config
from flask import request

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()

    page = request.args.get('page', 1, type=int)
    per_page = 20

    employees_query = Employee.query

    if form.validate_on_submit():
        query = form.query.data
        if query:
            employees_query = employees_query.filter(
                (Employee.firstname.ilike(f'%{query}%')) |
                (Employee.lastname.ilike(f'%{query}%')) |
                (Employee.employeeid.cast(db.String).like(f'%{query}%'))
            )
        if form.department.data and form.department.data != 0:
            employees_query = employees_query.filter(Employee.departmentid == form.department.data)

        if form.status.data:
            employees_query = employees_query.filter(Employee.status == form.status.data)

        if form.shift.data and form.shift.data != 0:
            employees_query = employees_query.filter(Employee.shiftid == form.shift.data)

        if form.certification.data and form.certification.data != 0:
            employees_query = employees_query.join(EmployeeCertification).filter(
                EmployeeCertification.certificationid == form.certification.data
            )

        

    employees = employees_query.paginate(page=page, per_page=per_page)

    return render_template('index.html', form=form, employees=employees)


@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    form = NewEmployeeForm()
    if form.validate_on_submit():
        new_emp = Employee(
            firstname=form.FirstName.data,
            lastname=form.LastName.data,
            startdate=form.StartDate.data,
            salary=form.Salary.data,
            status=form.Status.data,
            departmentid=form.DepartmentID.data,
            shiftid=form.ShiftID.data,
            yearsatcompany=0,
            strikes=0,
            ptoused=0,
            ptoremaining=0,
            hoursworked=0
        )
        db.session.add(new_emp)
        db.session.commit()
        return redirect(url_for('employee_detail', employee_id=new_emp.employeeid))
    return render_template('add_employee.html', form=form)

@app.route('/employee/<int:employee_id>', methods=['GET', 'POST'])
def employee_detail(employee_id):
    employee = Employee.query.get_or_404(employee_id)
    pto_form = PTOForm()
    cert_form = CertificationForm()
    action_form = ActionForm()
    shift_form = ShiftForm()

    if pto_form.submit_add.data and pto_form.validate():
        employee.ptoremaining += pto_form.amount.data
        db.session.commit()
        return redirect(url_for('employee_detail', employee_id=employee_id))

    if pto_form.submit_use.data and pto_form.validate():
        employee.ptoused += pto_form.amount.data
        employee.ptoremaining -= pto_form.amount.data
        db.session.commit()
        return redirect(url_for('employee_detail', employee_id=employee_id))

    if cert_form.validate_on_submit():
        new_cert = EmployeeCertification(
            employeeid=employee_id,
            certificationid=cert_form.CertificationID.data,
            dateobtained=cert_form.DateObtained.data
        )
        db.session.add(new_cert)
        db.session.commit()
        return redirect(url_for('employee_detail', employee_id=employee_id))

    if action_form.validate_on_submit():
        new_action = DisciplinaryAction(
            employeeid=employee_id,
            actiontype=action_form.ActionType.data,
            actiondate=action_form.ActionDate.data,
            description=action_form.Description.data
        )
        db.session.add(new_action)
        db.session.commit()
        return redirect(url_for('employee_detail', employee_id=employee_id))

    if shift_form.validate_on_submit():
        employee.shiftid = shift_form.ShiftID.data
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
