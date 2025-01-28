from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

from datetime import datetime

class Annotation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    label = db.Column(db.Text, nullable=False)
    x1 = db.Column(db.Float, nullable=False)
    y1 = db.Column(db.Float, nullable=False)
    x2 = db.Column(db.Float, nullable=False)
    y2 = db.Column(db.Float, nullable=False)
    
class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.LargeBinary, nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    image_urls = db.Column(db.Text, nullable=False)  # Store as a comma-separated string
    images = db.relationship('Image', backref='project', lazy=True, cascade="all, delete-orphan")

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email=db.Column(db.String(150), unique=True)
    password=db.Column(db.String(150))
    first_name=db.Column(db.String(150))
    sur_name=db.Column(db.String(150))
    project_list=db.relationship('Project') #relationship to project table