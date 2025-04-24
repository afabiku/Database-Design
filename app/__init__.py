from flask import Flask

def create_app(config_name="dev"):
    app = Flask(__name__)
    from config import config_by_name
    app.config.from_object(config_by_name[config_name])

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
