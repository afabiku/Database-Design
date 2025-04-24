from flask import Blueprint, render_template

bp = Blueprint("employees", __name__)

@bp.route("/employees")
def index():
    employees = [
        {
            "name": "John Doe",
            "department": "Manufacturing",
            "shift": "Night",
            "salary": "$52,000",
            "pto_used": "12 hrs",
            "strikes": 1,
            "certifications": "Forklift",
            "status": "Full-Time"
        },
        {
            "name": "Jane Smith",
            "department": "Engineering",
            "shift": "Day",
            "salary": "$67,000",
            "pto_used": "4 hrs",
            "strikes": 0,
            "certifications": "Lean Six Sigma",
            "status": "Part-Time"
        },
        {
            "name": "Carlos Ruiz",
            "department": "Logistics",
            "shift": "Evening",
            "salary": "$58,500",
            "pto_used": "8 hrs",
            "strikes": 2,
            "certifications": "CDL",
            "status": "Full-Time"
        }
    ]
    return render_template("employees.html", employees=employees)
