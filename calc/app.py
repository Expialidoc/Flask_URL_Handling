from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')  # part of URL before "?"
def addem():
    a = request.args.get('a') # string
    b = request.args.get('b')
    return f'''{add(int(a),int(b))}''' # make it string
 
@app.route('/sub')  # part of URL before "?"
def subem():
    a = request.args.get('a')
    b = request.args.get('b')
    return f'''{sub(int(a),int(b))}'''

@app.route('/mult')  # part of URL before "?"
def multem():
    a = request.args.get('a')
    b = request.args.get('b')
    return f'''{mult(int(a),int(b))}'''

@app.route('/div')  # part of URL before "?"
def divem():
    a = request.args.get('a')
    b = request.args.get('b')
    return f'''{div(int(a),int(b))}'''

@app.route('/math/<oper>')  # part of URL before "?"
def all_in_one(oper):
    a = request.args.get('a') # string
    b = request.args.get('b')
    FUNCS = {
    'add': add(int(a),int(b)),
    'sub': sub(int(a),int(b)),
    'mult': mult(int(a),int(b)),
    'div': div(int(a),int(b))
    }
    result = FUNCS[oper]
    return f'''{result}'''
    