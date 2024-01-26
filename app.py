from flask import Flask
from src.routes import routes


app = Flask(__name__)

def create_app():
    global app

    app = Flask(__name__)
    app.config['FLASK_DEBUG'] = True

    # Register Routes
    app.register_blueprint(routes)

    return app


create_app()
