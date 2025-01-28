from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
db=SQLAlchemy()
DB_NAME='database.db'  

# def create_database(app):
#     if not path.exists('LabelBoxMini/' + DB_NAME):
#         with app.app_context():
#             db.create_all()
#         print('Created Database!')
#     else:
#         print('Database already exists!') 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='2235857970'
    app.config['SQLALCHEMY_DATABASE_URI']=f'sqlite:///{DB_NAME}'    
    db.init_app(app)    
    
    
    from .views import views
    from .auth import auth_
    from .dashboard import dashboard_
    from .annotate import annotate_
    
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth_, url_prefix='/')
    app.register_blueprint(dashboard_,url_prefix='/')
    app.register_blueprint(annotate_,url_prefix='/')
    
    from .models import User
    
    with app.app_context():
            db.create_all()
    
    print('Created Database!')
    
    login_manager=LoginManager()
    login_manager.login_view='auth.Login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    
    
    return app

