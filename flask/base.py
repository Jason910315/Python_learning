from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/index/<int:age>')
def index(age):
    return render_template('index.html',age = age)

@app.route('/test/<int:num>')
def test(num):
    return render_template('test.html',num = num)

@app.route('/getname',methods = ['GET'])
def getname():
    name = request.args.get('name')
    age = request.args.get('age')
    return render_template('get.html',**locals())

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/submit", methods=['POST'])
def submit():
    firstname = request.values['firstname']
    lastname = request.values['lastname']
    return render_template('submit.html',**locals())

if __name__ == '__main__':
    app.run()