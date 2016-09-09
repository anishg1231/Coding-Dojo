from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

# @app.route('/otherRoute')
# def otherRoute():
#     return

def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

@app.route('/')
def index():
    sumSessionCounter()
    return render_template('index.html')

@app.route('/page1')
def page1():
  session['counter'] = session['counter'] + 1
  # if is sset name, store it on session
  return render_template('page1.html')

app.run(debug=True)
