from flask import Blueprint, render_template

bp = Blueprint("pto", __name__)

@bp.route("/pto")
def index():
    return render_template("pto.html")
