from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from throw import throw
from backend import newThrow

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

totPlay = 4
red = 3
blue = 3
green = 3
yellow = 3
throws = []
message = 'start'



class DiceValues(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    white1 = db.Column(db.Integer)
    white2 = db.Column(db.Integer)
    red = db.Column(db.Integer)
    blue = db.Column(db.Integer)
    green = db.Column(db.Integer)
    yellow = db.Column(db.Integer)

@app.route('/')
def index():
    message = 'return'
    
    return render_template('index.html', red = red, blue = blue, green = green, yellow = yellow, throws = throws, message = message)

@app.route('/throwDice')
def throwDice():
    if not throws:
        x = newThrow(-1, 1, totPlay) 
        print(x)
        throws.append( x )
        print(throws)
    elif len(throws) > 0:
        x = newThrow(throws[-1].id, throws[-1].player, totPlay)
        throws.append( x )
        # print(len(throws))
    message = 'throw'
    
    return render_template('index.html', red = red, blue = blue, green = green, yellow = yellow, throws = throws, message = message)

if __name__ == "__main__":
    app.run(debug=True)