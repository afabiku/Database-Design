from flask import Blueprint, render_template

bp = Blueprint("scheduling", __name__)

@bp.route("/scheduling")
def index():
    return render_template("scheduling.html")
