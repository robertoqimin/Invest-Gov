import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_cors import CORS

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    TEMPLATES_DIR = os.path.join(BASE_DIR, '..', 'templates')
    STATIC_DIR = os.path.join(BASE_DIR, '..', 'static')

    app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)
    app.config.from_object('config.Config')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    CORS(app)

    from .routes import auth, projects, comments, favorites, admin, chat, home
    app.register_blueprint(auth.bp)
    app.register_blueprint(projects.bp)
    app.register_blueprint(comments.bp)
    app.register_blueprint(favorites.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(chat.bp)
    app.register_blueprint(home.bp)

    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
