from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/survey', methods=['POST'])
def survey():
    print'='*80
    print request.form
    print'='*80
    return render_template('survey.html', survey=request.form)

app.run(debug=True)
