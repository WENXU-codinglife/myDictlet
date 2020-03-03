import os
from flask import Flask, render_template, request, jsonify
import data

app = Flask(__name__, static_folder='', template_folder='')

@app.route('/')
def index():
    return render_template('index.html')


#@app.route('/lookup', methods=['POST'])
#def lookup():
#    aud, defi = data.extr(request.form)
#    return aud, defi

#@app.route('/serverRetrieve', methods=['POST'])
#def serverRetrieve():
#    ret = data.store_retrieve(request.form)
#    return ret

if __name__ == '__main__':
	# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)