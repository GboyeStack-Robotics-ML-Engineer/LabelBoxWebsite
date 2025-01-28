from flask import Flask
from markupsafe import escape
from flask import Flask, abort
from flask import Flask,render_template

# ...

# ...

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def hello():
    return render_template('index.html')


@app.route('/Login/')
def login():
    return render_template('Login.html')

@app.route('/Dashboard/')
def about():
    return render_template('Dashboard.html')

@app.route('/Annotate/')
def annotate():
    return render_template('Annotator.html')




@app.route('/users/<int:user_id>/')
def greet_user(user_id):
    users = ['Bob', 'Jane', 'Adam']
    try:
        return '<h2>Hi {}</h2>'.format(users[user_id])
    except IndexError:
        abort(404)
        
if __name__ == '__main__':  
   app.run(debug=True)