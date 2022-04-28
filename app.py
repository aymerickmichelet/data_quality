from flask import Flask, render_template, redirect, jsonify, request
from service.uploader import upload_csv

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

    if request.method == REQUEST_METHOD['POST']:
        file = request.files['upload']

        # upload csv (get uploaded_file_path)
        uploaded_file_path = upload_csv(file)

        # parse csv

        # return template avec les stats du parse + le chemin du csv (pour dl)

        # Nicolas fait de la magie avec pandas
        # Affichage des résultats + Téléchargement du fichier csv pandaifié

    elif request.method == REQUEST_METHOD['GET']:
        return redirect("/", code=HTTP_CODE['FOUND'])

    # Temporaire en attendant Nicolas

    results = {
        "correct": '{percent:.2%}'.format(percent=0.6686),
        "warning": '{percent:.2%}'.format(percent=0.1391),
        "error": '{percent:.2%}'.format(percent=0.1923)
    }

    return render_template("result.html", results=results)


if __name__ == '__main__':
    app.run()
