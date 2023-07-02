from flask import Flask
from routes.routes import *
from environments.configs import DevelopmentConfig

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(api_bp)

    return app

app = create_app()
