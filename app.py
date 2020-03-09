import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import datetime
from pytz import timezone
#import data

app = Flask(__name__, static_folder='', template_folder='')

#-------------------------------------------------------------------------------------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ztouwilddheixm:31f459e0d39758a2e0f395a5aae55594ac77d92f7db16ec58446fa5aceca4ce4@ec2-184-72-236-57.compute-1.amazonaws.com:5432/deohh4cbjb5fv1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class FLASHCARD(db.Model):
    __tablename__ = 'flashcard'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10))
    word = db.Column(db.String(50), unique=True)

    def __init__(self, today,word):
        self.date = today
        self.word = word
#-------------------------------------------------------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/flashcard', methods=['POST'])
def flashcard():
    x = datetime.datetime.now()
    datetime_obj_pacific = timezone('US/Pacific').localize(x)
    today = "2"
    for i in range(1,10):
        today = today + str(datetime_obj_pacific)[i]
    #print(today)
    #print(request.form['keyword'])
    newword = request.form['keyword']
    #--->add to db
    if db.session.query(FLASHCARD).filter(FLASHCARD.word == newword).count() == 0:
        data = FLASHCARD(today,newword)
        db.session.add(data)
        db.session.commit()
    
    return 'ok'

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)