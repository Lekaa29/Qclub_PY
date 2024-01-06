from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path 
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    
    app.config['SECRET_KEY'] = 'lekapassword123'
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    
    #login_manager = LoginManager()
   # login_manager.login_view = "views.welcome"
    #login_manager.init_app(app)
    
    
            
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Table
    
   # create_database(app)
   
   
    with app.app_context():
        db.create_all()
        
    

    
    return app

def create_database(app):
    from .models import User, Table
    
    if not path.exists("webiste/" + DB_NAME):
        with app.app_context():
            db.create_all()
            
        for i in range(23):
            new_table = Table(id=i)
            db.session.add(new_table)
            db.session.commit()
        print("Created Database!")