from flask import Flask, render_template, request, jsonify
import data

app = Flask(__name__, static_folder='', template_folder='')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lookup', methods=['POST'])
def lookup():
    data.Find(request.form)
    return "ok"

#@app.route('/serverRetrieve', methods=['POST'])
#def serverRetrieve():
#    ret = data.store_retrieve(request.form)
#    return ret

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')