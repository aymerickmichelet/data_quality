from flask import Flask, render_template, jsonify, request
import os

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/parse-csv', methods=['POST', 'GET'])
def parse_csv():

    # if request.method == 'POST':
    #     print(request.files)
    #     file = request.files['file']
    #     file.save(os.path.join('upload', file.filename))

    response = {
        'message': 'wesh',
        'status': 200
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()
