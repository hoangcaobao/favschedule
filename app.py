from flask import Flask, redirect, render_template, url_for, request
import psycopg2 as pg
import time
import threading
app = Flask(__name__)

    

@app.route('/')
def index () :
    return redirect('http://127.0.0.1:5000/homepage')


@app.route('/homepage')
def homepage ():
    return render_template('homepage.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  
        ua = request.user_agent;
        print(ua) 
        print(request.remote_addr)     
        return request.form['username'] + " " + request.form['pwd'];
    else:
        return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':  
        ua = request.user_agent;
        print(ua) 
        print(request.remote_addr)     
        return request.form['username'] + " " + request.form['pwd'];
    else:
        return render_template('login.html')

# always run when build (for debugging) 
with app.test_request_context():
    pass
    # print(url_for('hello_world'))
    # print(url_for('sum',x=1,y=2))
    # print(url_for('login', next='/'))
    # print(url_for('profile', username='John Doe'))

if __name__ == '__main__':
    app.run();