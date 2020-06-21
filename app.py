from flask import Flask, render_template, redirect, request
import SpeechToTextMicrophone as sr
#import textToKeywords as TK
#import QA as qa

app = Flask(__name__)


@app.route('/')
def redirection():
    return redirect('/patientdashboard')


@app.route('/patientdashboard', methods=['GET', 'POST'])
def patientdashboard():

    return render_template('Patientdashboard.html')


@app.route('/patientdashboard1', methods=['POST'])
def patientdashboard():
    if request.method == 'POST':
        Micro = request.form['Micro']
        texting = sr.voiceinput()

    return render_template('Patientdashboard1.html', texting=texting)


@app.route('/doctordashboard', methods=['GET', 'POST'])
def doctordashboard():

    return render_template('DoctorDashboard.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
