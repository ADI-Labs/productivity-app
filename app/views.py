from flask import render_template

from . import app

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/trophies')
def trophies():
    return render_template('trophies.jinja')



@app.route('/page2')
def page2():

