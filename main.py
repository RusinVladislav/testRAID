from flask import Flask
from flask_restx import Api

from app.views.frameworks import framework_ns
from app.config import Config
from app.database import db


def create_app(config: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()

    return application


def configure_app(application: Flask):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(framework_ns)


if __name__ == '__main__':
    app = create_app(Config())
    configure_app(app)
    app.run()
