from flask import Blueprint, request, redirect, url_for, flash, render_template,jsonify
from flask_login  import login_user, login_required, logout_user, current_user 
from . import db
from .models import Project,Image
import time
from datetime import datetime
from flask import send_file
import io

dashboard_ = Blueprint('dashboard', __name__)


@dashboard_.route('/create_project/', methods=['GET','POST'])
@login_required
def create_project():
    project_name = request.form.get('projectName')
    project_description = request.form.get('projectDescription')
    image_files = request.files.getlist('imageUpload')

    # Process the form data and save the project to the database
    image_urls = [image.filename for image in image_files]
    new_project = Project(
        name =project_name,
        description=project_description,
        date_created=datetime.now(),
        # edited_ago='just now',
        # privacy='Private',
        # image_count=len(image_files),
        # model_count=0,
        user_id=current_user.id,
        image_urls=','.join(image_urls)
    )
    db.session.add(new_project)
    db.session.commit()

    # Handle image uploads
    for image in image_files:
        new_image = Image(data=image.read(), project_id=new_project.id)
        db.session.add(new_image)
    db.session.commit()

    flash('Project created successfully!', 'success')
    return redirect(url_for('dashboard.dashboard'))




@dashboard_.route('/delete_projects/<int:project_id>/', methods=['DELETE'])
@login_required
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    if project.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    db.session.delete(project)
    db.session.commit()
    return jsonify({'success': 'Project deleted'})

@dashboard_.route('/get_projects/', methods=['GET'])
@login_required
def get_projects():
    projects = Project.query.filter_by(user_id=current_user.id).all()
    projects_list = [
                        {
                        'id': project.id,
                        'name': project.name,
                        'description': project.description,
                        'image_urls': project.image_urls.split(','),
                        'images': [image.id for image in project.images]
                        } 
                        
                        for project in projects
                    ]
    return jsonify(projects_list)





@dashboard_.route('/get_projects/<int:project_id>/', methods=['GET'])  
@login_required
def get_project_with_id(project_id):
    print('hello')
    project = Project.query.get_or_404(project_id)
    if project.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    project_data = {
        'id': project.id,
        'name': project.name,
        'description': project.description,
        'images': [image.id for image in project.images]
    }
    return jsonify(project_data)





@dashboard_.route('/edit_project/<int:project_id>/', methods=['POST'])
@login_required
def edit_project(project_id):
    project = Project.query.get_or_404(project_id)
    if project.user_id != current_user.id:
        return jsonify({'error': 'Unauthorized'}), 403

    project.name = request.form.get('projectName')
    project.description = request.form.get('projectDescription')

    image_files = request.files.getlist('imageUpload')
    if image_files:
        # Delete old images
        for image in project.images:
            db.session.delete(image)
        db.session.commit()

        # Add new images
        for image in image_files:
            new_image = Image(data=image.read(), project_id=project.id)
            db.session.add(new_image)

    db.session.commit()
    return jsonify({'success': 'Project updated'})





@dashboard_.route('/api/images/<int:image_id>/', methods=['GET'])
@login_required
def get_image(image_id):
    image = Image.query.get_or_404(image_id)
    return send_file(
        io.BytesIO(image.data),
        mimetype='image/jpeg',
        as_attachment=False,
        download_name=f'image_{image_id}.jpg'
    )
    
    
    

@dashboard_.route('/dashboard/',methods=['GET','POST'])
@login_required
def dashboard():
    return render_template('Dashboard.html')