from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
import time
from flask_login import login_user, login_required, logout_user, current_user

auth_= Blueprint('auth', __name__)


def validate_responses():
    pass

@auth_.route('/Login/',methods=['GET','POST'])
def Login():
    
    if request.method=='POST':
        if request.form.get('name') == 'signup':
            firstname = request.form.get('firstname')
            surname=request.form.get('surname')  
            user_mail=request.form.get('email')
            user_password=request.form.get('password')  
            user_confirm_password=request.form.get('confirmedpassword') 
            #print({'from':request.form.get('name'), 'username':username,'password':user_password})
            
            user=User.query.filter_by(email=user_mail).first()
            
            if user:
                flash('User already exists',category='error')
            elif user_password!=user_confirm_password:
                flash('Passwords do not match',category='error')
            
            else:
                new_user=User(first_name=firstname, sur_name=surname, email=user_mail, password=generate_password_hash(user_password, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash('Account created successfully',category='success')
                user=User.query.filter_by(email=user_mail).first()
                if user:
                    login_user(user, remember=True)
                return render_template('Dashboard.html')
            
            
        elif request.form.get('name') =='userlogin':
            usermail = request.form.get('usermail')
            user_password=request.form.get('password')
            #print({'from':request.form.get('name'), 'username':username,'password':user_password})
            user=User.query.filter_by(email=usermail).first() 
            if user:
                if check_password_hash(user.password, user_password):
                    flash('Logged in successfully',category='success')
                    login_user(user, remember=True)
                    return render_template('Dashboard.html',user=current_user)
                    
                else:
                    flash('Incorrect password, try again',category='error')
            else:
                flash('User not found',category='error')
            
            
        elif request.form.get('name') =='adminlogin':
            username = request.form.get('usermail')
            user_password=request.form.get('password')
            # print({'from':request.form.get('name'), 'username':username,'password':user_password})
            # if len(username)<6:
            #     flash('User name cannot be less than 6 characters',category='error')
                
        else:
            pass
    else:
        pass
            
        
    return render_template('Login.html')


@auth_.route('/Logout/')
@login_required
def Logout():
    logout_user()
    flash('Logged out successfully',category='success')
    return redirect(url_for('views.home'))

