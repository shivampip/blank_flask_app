from flask import Flask
from flask_cors import CORS

from app.blueprints.sandbox import sandbox


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    CORS(app)

    app.config.from_object("config.settings")
    # app.config.from_pyfile("settings.py", silent=True)

    # app.register_blueprint(sandbox)
    app.register_blueprint(sandbox, url_prefix="/sb")

    return app



