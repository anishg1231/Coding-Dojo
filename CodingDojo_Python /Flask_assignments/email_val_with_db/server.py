# '''Grab all needed modules and libraries to use in our aplication'''

from flask import Flask, render_template, request, redirect, session, flash
# '''Loading up our connection to MYSQL'''
from mysqlconnection import MySQLConnector
# '''Creating the Flask applicatoin aka our runnng server'''
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app, 'the_wall')
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    valid_form = True
    print '^' * 100
    print request.form
    if len(request.form['first_name']) == 0 or len(request.form['last_name']) == 0 or len(request.form['email']) == 0 or len(request.form['password']) == 0 or len(request.form['confirm_password']) == 0:
        valid_form = False
        flash('Please fill out the whole form')
    if not request.form['first_name'].isalpha():
        valid_form = False
        flash('no special character allowed in first name')
    if not request.form['last_name'].isalpha():
        valid_form = False
        flash('no special character allowed in last name')
    if not EMAIL_REGEX.match(request.form['email']):
        valid_form = False
        flash('invalid email')
    if len(request.form['password']) < 8:
        valid_form = False
        flash('password has to be more than 8 characters')
    if not request.form['password'] == request.form['confirm_password']:
        valid_form = False
        flash('confirm password does not match password')
    if not valid_form:
        return redirect('/')
    else:
        query = "INSERT INTO users(first_name, last_name, email, password, updated_at, created_at) VALUES(:first_name,:last_name,:email,:password,NOW(),NOW())"

        data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        }
        mysql.query_db(query, data)
        flash('successful registered')
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    print '*' * 10
    print request.form["email"]
    print request.form["password"]
    print '*' * 10

    query = "SELECT * FROM users WHERE email = :email"
    data = {
        "email": request.form["email"],
    }
    user = mysql.query_db(query, data)

    print '*' * 10
    print user
    print '*' * 10

    if not user:
        print "no user returned"
        flash("User Not In Database. Please register or try again.")
        return redirect('/')
    else:
        print "checking password"
        if user[0]['password'] == request.form['password']:
            session['first_name'] = user[0]['first_name']
            session['user_id'] = user[0]['id']

            return render_template('success.html')
        else:
            return redirect('/')

@app.route('/logout', methods=['POST'])
def logging_out():
    session['clear']
    return redirect ('/')

@app.route('/wall', methods=['POST'])
def post_page():
    print '#' * 10
    print request
    print '#'* 10
    print request.form
    print '#'* 10
    print request.form['post']
    print '#'* 10
    valid_form = True
    if len(request.form['post']) == 0:
        valid_form = False
        flash('Please try again.')
    if len(request.form['post']) > 255:
        valid_form = False
        flash('Only 255 characters')
    if not valid_form:
        return redirect('/')
    else:
        query = "INSERT INTO messages(users_id,messages,created_by,updated_by)VALUES(:user_id,:post, NOW(),NOW())"
        data = {
        "post": request.form["post"],
        "user_id": session['user_id']
        }
        mysql.query_db(query, data)
    #post to wall and save to database
    query = "SELECT * FROM messages WHERE users_id = :users_id"
    data = {
        "users_id": session['user_id']
    }
    messages = mysql.query_db(query, data)

    print '*' * 10
    print messages
    print '*' * 10
    return render_template('success.html', messages=messages)


@app.route('/comment', methods=['GET'])
def message_comments():
    print '&' * 10
    print request.form
    print '&' * 10
    valid_form = True
    if len(request.form['comment']) == 0:
        valid_form = False
        flash('Please try again.')
    if len(request.form['comment']) > 255:
        valid_form = False
        flash('Only 255 characters')
    if not valid_form:
        return redirect('/')
    else:
        query = "INSERT INTO comments(messages_id,comment,created_at,updated_at)VALUES(:messages_id,:comment,NOW(),NOW())"

        data = {
        'comment': request.form['comment'],
        'messages_id': request.form ['name']
        }
        mysql.query_db(query, data)

    query = "SELECT * FROM comments WHERE users_id = :users_id"
    data = {
        "users_id": session['user_id']
    }
    comments = mysql.query_db(query, data)

    print '*' * 10
    print comments
    print '*' * 10
    return render_template('success.html', comments=comments)


app.run(debug=True)
