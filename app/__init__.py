from flask import Flask
from config import config_by_name
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name="dev"):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    db.init_app(app)

    from app.routes import index, detail, add

    app.register_blueprint(index.bp)
    app.register_blueprint(add.bp)
    app.register_blueprint(detail.bp)

    return app
