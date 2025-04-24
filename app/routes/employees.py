from flask import Blueprint, render_template

bp = Blueprint("employees", __name__)

@bp.route("/employees")
def index():
    return render_template("employees.html")
