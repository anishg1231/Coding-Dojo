from flask import Flask, render_templates, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

app.route('/')
def index():
    return render_templates('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print "Got Post Info"
    name = request.form['name']
    email = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_templates('user.html', name=session['name'], email=session['email'])


app.run(debug=True)
