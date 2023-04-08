"""Make the website folder a Python package => can import the folder and whatever inside init will run automatically"""
from flask import Flask

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config['SECRET_KEY'] = 'asldlkdjafsfjlakd'

    # Import blueprints
    from .views import views
    
    app.register_blueprint(views, url_prefix="/")

    return app

