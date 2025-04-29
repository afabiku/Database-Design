from flask import Blueprint, request, render_template
from app.forms import SearchForm
from app.models import Employee, EmployeeCertification
from app import db

bp = Blueprint("index", __name__)

@bp.route('/', methods=['GET', 'POST'])
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
    
        employees_query = employees_query.order_by(Employee.employeeid)
        employees = employees_query.paginate(page=page, per_page=per_page)


    return render_template('index.html', form=form, employees=employees)
