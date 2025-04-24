from flask import Blueprint

main = Blueprint("main", __name__)

from . import main  # import the route definitions
