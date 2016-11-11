from flask import render_template

from . import app

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/trophies')
def trophies():
    return render_template('trophies.jinja', 
        netflix = "Netflix and Chill",
        netflix_img = "https://i1.wp.com/fusion.net/wp-content/uploads/2015/08/maxresdefault.jpg?resize=1600%2C900&quality=80&strip=all",
        socialBee = "Social things",
        adventure_img = "http://www.infiniteguest.org/wp-content/uploads/2015/06/adventure-time.jpg")



@app.route('/page2')
def page2():
    return render_template('trophies.jinja', 
        netflix = "Netflix and Chill",
        socialBee = "Social things")
