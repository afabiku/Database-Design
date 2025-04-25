from flask import Flask
from config import config_by_name

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name="dev"):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)

    from app.routes import home, employees, pto, scheduling
    app.register_blueprint(home.bp)
    app.register_blueprint(employees.bp)
    app.register_blueprint(pto.bp)
    app.register_blueprint(scheduling.bp)


    return app
