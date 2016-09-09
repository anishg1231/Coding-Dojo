from flask import Flask, render_template, request,redirect,session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['count'] = random.randrange(100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def user():
    print 'o'*80
    print type(request.form['number'])
    if int(request.form['number']) > session['count']:
        print "Number is high"
        session['number']= 'number is high'
    elif int(request.form['number']) < session['count']:
        print "Number is low"
        session['number'] = 'number is low'
    else:
        print "You got it!"
        session['number'] = 'you got it'
    return render_template('index.html')

app.run(debug=True)
