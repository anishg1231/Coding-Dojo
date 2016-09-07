from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/ninjas', methods=['POST'])
def ninja_process():
    print'='*80
    print request.form
    print'='*80
    return render_template('ninjas.html', ninjas=request.form)

app.run(debug=True)
