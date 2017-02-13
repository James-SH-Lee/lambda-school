from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('templatehome.html')

@app.route('/about')
def about():
    return app.send_static_file('about.html')

@app.route('/contact')
def something():
    return app.send_static_file('contact.html')

@app.route('/post/<postnum>')
def posts(postnum):
    return 'This is post ' + postnum

@app.route('/birthday')
def birthday():
    return app.send_static_file('birthday.html')

@app.route('/greeting/<name>')
def greeting(name):
    return 'Hello ' + name

@app.route('/add/<sumNum1>/<sumNum2>')
def sum(sumNum1,sumNum2):
    num1 = int(sumNum1)
    num2 = int(sumNum2)
    sum = num1 + num2
    sumString = str(sum)
    return sumString

@app.route('/multiply/<multiplyNum1>/<multiplyNum2>')
def multiply(multiplyNum1,multiplyNum2):
    num1 = int(multiplyNum1)
    num2 = int(multiplyNum2)
    multiply = num1 * num2
    multiplyString = str(multiply)
    return multiplyString

@app.route('/subtract/<subNum1>/<subNum2>')
def sub(subNum1,subNum2):
    num1 = int(subNum1)
    num2 = int(subNum2)
    sub = num1 - num2
    subString = str(sub)
    return subString
