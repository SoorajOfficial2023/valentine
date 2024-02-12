from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return '<h1>Will u be my valentine ?</h1>'

@app.route(('/no'))

def sooraj():
    return '<h1> Dont say that... </h1>'

@app.route(('/again no'))

def no():
    return '<h1> Its hurt...</h1>'

@app.route(('/its no'))
def nono():
    return '<h1> I will cry</h1>'

@app.route(('/nooo'))
def nooo():
    return '<h1>I will die</h1>'

@app.route(('/yes'))
def yes():
    return '<h1 style="color:red;"> I LOVE YOU</h1>'
app.run()

