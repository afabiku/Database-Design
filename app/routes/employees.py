from flask import Blueprint, render_template
from app.models import Employee

bp = Blueprint("employees", __name__)

@bp.route("/employees")
def index():
    employees = Employee.query.all()
    return render_template("employees.html", employees=employees)
