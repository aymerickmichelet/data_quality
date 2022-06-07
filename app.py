from flask import Flask, render_template, redirect, jsonify, request
from service.uploader import upload_xlsx
from service.parser import parser

# Global variables
REQUEST_METHOD = {
    "POST": "POST",
    "GET": "GET"
}

HTTP_CODE = {
    "OK": 200,
    "FOUND": 302
}

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/parse-xlsx', methods=['POST', 'GET'])
def parse_xlsx():

    global REQUEST_METHOD
    global HTTP_CODE
    message = None
    results = {}

    if request.method == REQUEST_METHOD['POST']:
        file = request.files['upload']

        # upload csv (get uploaded_file_path)
        uploaded_file_datas = upload_xlsx(file)

        # parse csv
        results = parser(uploaded_file_datas["path"])

        results = {
            "correct": round(results["correct"], 2),
            "error": round(results["error"], 2),
            "xlsx": uploaded_file_datas["filename"]
        }

    elif request.method == REQUEST_METHOD['GET']:
        return redirect("/", code=HTTP_CODE['FOUND'])

    return render_template("result.html", results=results)


if __name__ == '__main__':
    app.run()
