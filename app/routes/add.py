from flask import Blueprint, redirect, url_for, render_template
from app.forms import NewEmployeeForm
from app.models import Employee
from app import db

bp = Blueprint("add", __name__)

@bp.route('/add', methods=['GET', 'POST'])
def index():
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
        return redirect(url_for('detail.index', employee_id=new_emp.employeeid))
    return render_template('add_employee.html', form=form)