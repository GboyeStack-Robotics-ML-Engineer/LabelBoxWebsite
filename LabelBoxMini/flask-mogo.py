import flask
from flask import Flask, render_template, request, redirect, url_for, session, flash
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.flask_database
todos = db.todos

@app.route("/", methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        form_id = request.form['formid']
        if form_id == 'form1':
            email = request.form['email']
            password = request.form['password']
            print("Form 1 submitted with email")
            todos.insert_one({'formid':form_id, 'email': email, 'password': password})
        elif form_id == 'form2':
            email = request.form['email']
            password = request.form['password']
            print("Form 2 submitted with email")
            todos.insert_one({'formid':form_id, 'email': email, 'password': password})
        elif form_id == 'form3':
            name = request.form['Name']
            firstname = request.form['firstname']
            email = request.form['email']
            password = request.form['password']
            confirmed_password = request.form['confirmpassword']
            print("Form 3 submitted with Name")
            todos.insert_one({'formid':form_id,'name': name, 'firstname': firstname, 'email': email, 'password': password, 'confirmed_password': confirmed_password})
        else:
            pass
        return redirect(url_for('index'))
    
    all_todos = todos.find()
    return render_template('Login.html')

if __name__ == '__main__':
    app.run(debug=True)