from flask import Blueprint, request, redirect, url_for, flash, render_template,jsonify
from flask_login  import login_user, login_required, logout_user, current_user 
from . import db
from .models import Project,Image,Annotation
import time
from datetime import datetime
from flask import send_file
import io
import matplotlib.pyplot as plt

annotate_ = Blueprint('annotate', __name__)

@annotate_.route('/save_annotation', methods=['POST'])
def save_annotation():
    data = request.get_json()
    project_id = data.get('project_id')
    image_id = data.get('image_id')
    label = data.get('label')
    coordinates = data.get('coordinates')

    if not project_id or not image_id or not label or not coordinates:
        return jsonify({'error': 'Missing data'}), 400

    annotation = Annotation(
        project_id=project_id,
        image_id=image_id,
        user_id=current_user.id,
        label=label,
        x1 = coordinates[0],
        y1 = coordinates[1],
        x2 = coordinates[2],
        y2 = coordinates[3]
    )
    # print(coordinates)
    db.session.add(annotation)
    db.session.commit()

    return jsonify({'message': 'Annotation saved successfully'}), 200
@annotate_.route('/get_project_images/<int:project_id>/', methods=['GET','POST'])
@login_required
def get_project_images(project_id):
    print(project_id)
    print('hello')
    project = Project.query.get_or_404(project_id)
   
    if project:
        print(f'{project}')
    
    
    images = [{'id':image.id,'url':f'http://127.0.0.1:5000/api/images/{image.id}/'} for image in project.images]
    print(images)
    return jsonify(images)

@annotate_.route('/Annotate/<int:project_id>/',methods=['GET','POST'])
@login_required
def annotate(project_id):
    # project = Project.query.get_or_404(project_id)
    # if project:
    #     print(f'{project}')
    # images = [url_for('static', filename=f'images/{image.id}.jpg') for image in project.images]
    
    # print(images)
   
    return render_template('Annotator.html',project_id=project_id)

