from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    num1 = int(request.args.get('a',))
    num2 = int(request.args['b'])
    return str(operations.add(num1, num2))

@app.route('/sub')
def sub():
    num1 = int(request.args['a'])
    num2 = int(request.args['b'])
    return str(operations.sub(num1, num2))

@app.route('/mult')
def mult():
    num1 = int(request.args['a'])
    num2 = int(request.args['b'])
    return str(operations.mult(num1, num2))

@app.route('/div')
def div():
    num1 = int(request.args['a'])
    num2 = int(request.args['b'])
    return str(operations.div(num1, num2))