from flask import Flask, render_template, redirect, request
import QA as qa

app = Flask(__name__)


@app.route('/')
def redirection():
    return redirect('/home')


@app.route('/home')
def homePage():
    return render_template('home.html')


@app.route('/login')
def loginPage():
    return render_template('login.html')


@app.route('/predict', methods=['POST'])
def predict():
    passage = request.form['para']
    question = request.form['que']
    sol = qa.findAnswer(passage, question)
    return render_template('ans.html', prediction_text='Answer is: {}'.format(sol))


@app.route('/ans', methods=['POST'])
def ans():
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.debug = True
    app.run()
