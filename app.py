from flask import Flask, render_template, redirect, request
import SpeechToTextMicrophone as sr
#import textToKeywords as TK
#import QA as qa
import insuranceregression as ir
app = Flask(__name__)


@app.route('/')
def redirection():
    return redirect('/patientdashboard')


@app.route('/patientdashboard', methods=['GET', 'POST'])
def patientdashboard():
    return render_template('Patientdashboard.html')


@app.route('/patientdashboard1', methods=['POST'])
def patientdashboard1():
    if request.method == 'POST':
        Micro = request.form['Micro']
        texting = sr.voiceinput()

    return render_template('Patientdashboard1.html', texting=texting)

@app.route('/patientdashboard2', methods=['GET', 'POST'])
def patientdashboard2():
    if request.method=='POST':
        age = request.form['Age']
        bmi = request.form['BMI']
        op = ir.regrate(age,bmi)
    return render_template('Patientdashboard2.html',op = op)

@app.route('/doctordashboard', methods=['GET', 'POST'])
def doctordashboard():
    return render_template('DoctorDashboard.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
