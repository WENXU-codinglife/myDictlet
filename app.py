import os
from flask import Flask, render_template, request, jsonify
import datetime
from pytz import timezone
#import data

app = Flask(__name__, static_folder='', template_folder='')

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
    print(today)
    print(request.form['keyword'])
    return 'ok'

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)