from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)

app.secret_key = "anything"

@app.route('/')
def index():
    try:
        print session['num_gold']
    except:
        session['num_gold']=0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    session['random'] = random.randrange(-51,51)
    print '*' * 8
    print request.form['buildings']
    print '*' * 8
    if request.form['buildings'] == 'farm' :
        print 'Getting gold from farm!'
        session['num_gold'] +=  random.randrange(10,21)
        session['message'] = 'Getting gold from farm!'

    elif request.form['buildings'] == 'cave':
        print 'Your striking Gold!'
        session['num_gold'] += random.randrange(5,11)
        session['message'] = 'Your striking gold!'

    elif request.form['buildings'] == 'house':
        print "Getting gold from your mama's house!"
        session['num_gold'] += random.randrange(2,6)
        session['message'] = "Getting gold from your mama's house!"

    if request.form['buildings'] == 'casino':
        print 'Your robbing the casino!'
        session['num_gold'] += random.randrange(-51,51)
        session['message'] = 'Your robbing the casino!'
    elif(session['num_gold'] < 51):
        session['message'] = 'Your losing your gold!'

    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')


app.run(debug=True)


#have /process_moneydetermine how much gold the user should have
