from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/parse-csv', methods=['POST', 'GET'])
def parse_csv():

    message = None

    if request.method == 'POST':
        print(request.files)
        file = request.files['upload']
        file.save(os.path.join('upload', file.filename))
        message = file.filename
    elif request.method == 'GET' :
        message = "wesh"

    response = {
        'message': message,
        'status': 200
    }
    return jsonify(response)


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():

    message = None

    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join('upload', f.filename))
        message = f.filename

    elif request.method == 'GET':
        message = "wesh"

    response = {
        'message': message,
        'status': 200
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run()
