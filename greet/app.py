from flask import Flask, request
app = Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'welcome'

@app.route('/welcome/<home>')
def welcome2(home):
    return f'''welcome {home}'''
