from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import random
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
# mysql = MySQLConnector(app,'')
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['POST'])
def survey():
    print'='*80
    print request.form
    print'='*80
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    else:
        flash("success!")
    # return redirect('/')
    return render_template('survey.html', survey=request.form)

app.run(debug=True)
