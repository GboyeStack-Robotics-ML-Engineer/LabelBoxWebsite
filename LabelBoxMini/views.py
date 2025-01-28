from flask import render_template, request, redirect, url_for, Blueprint
from flask_login  import login_user, login_required, logout_user, current_user 
views= Blueprint('views', __name__)

@views.route('/')
@views.route('/home/')
@views.route('/index/')
def home():
    return render_template('index.html',user=current_user)


