import os
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, distinct
import datetime
from pytz import timezone
from funcs import datetoday,differ_lists

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

@app.route('/passmelabels', methods=['POST'])
def passmelabels():
    #db.session.query(FLASHCARD).filter(FLASHCARD.word == newword).count() == 0:
    #numberofcards = db.session.query(func.count(distinct(FLASHCARD.date))).count()
    today = datetoday()
    month = today[0:7]
    #-------------flashcard labels

    labels = db.session.query(distinct(FLASHCARD.date)).filter(FLASHCARD.date.like(month+'%')).all() # labels is a list of result objects
    #labels = [('2020-03-25',), ('2020-03-24',), ('2020-03-29',), ('2020-03-21',)]
    numberofcards = len(labels)
    #print(numberofcards)
    passedlabels = []
    for i in labels:
        #the format of i is like "('2020-03-25',)"
        #the format of i[0] is like "2020-03-25"
        #i[1] is out of range!
        passedlabels.append(i[0])
    passedlabels.sort()
    #print(passedlabels)
    #-------------archive labels
    alllabels = db.session.query(distinct(FLASHCARD.date)).all()
    otherlabels = differ_lists(alllabels,labels)
    #print(otherlabels)
    nameoffolders = []
    for i in otherlabels:
        if len(nameoffolders) == 0:
            nameoffolders.append(i[0][0:7])
        elif i[0][0:7] != nameoffolders[-1]:
            nameoffolders.append(i[0][0:7])
    nameoffolders.sort()
    numberoffolders = len(nameoffolders)
    ret = {
        "count":numberofcards,
        "dates":passedlabels,
        "numberofmonthes":numberoffolders,
        "monthes":nameoffolders
        }
    print(ret)
    #ret = {'count': 25, 'dates': ['2020-03-25', '2020-03-24', '2020-03-29', '2020-03-21', '2020-03-30', '2020-03-28', '2020-03-23', '2020-04-14', '2020-03-14', '2020-04-09', '2020-04-04', '2020-03-13', '2020-03-15', '2020-03-26', '2020-03-19', '2020-03-27', '2020-03-22', '2020-04-01', '2020-03-16', '2020-03-12', '2020-03-18', '2020-04-12', '2020-04-11', '2020-03-10', '2020-03-09']}
    return ret

@app.route('/fetchwords',methods=['POST'])
def fetchwords():
    loc = request.form['keyword']
    date = ''
    month = ''
    words = []
    if loc[-12] == 'x':
        i = -10
        while(i < 0):
            date = date + loc[i]
            i = i + 1
        lBooks = db.session.query(FLASHCARD)  #returns a Query object. 
        for oBook in lBooks:
            if oBook.date == date:
                words.append(oBook.word)
    elif loc[-9] == 'x':
        i = -7
        while(i < 0):
            month = month + loc[i]
            i = i + 1
        lBooks = db.session.query(FLASHCARD).filter(FLASHCARD.date.like(month+'%'))  #returns a Query object. 
        for oBook in lBooks:
            words.append(oBook.word)

    ret = {'number':len(words),'words':words}
    return ret

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
        ret = {"feedback": True}
    else:
        lBooks = db.session.query(FLASHCARD)
        for oBook in lBooks:
            if oBook.word == newword:
                ret = {"feedback": False,"date":oBook.date}
                break
    return ret


if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)