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
# app.config['UPLOAD_FOLDER'] = '/path/o/the/uy'


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/result')
def result():
    return render_template("result.html")


@app.route('/parse-csv', methods=['POST', 'GET'])
def parse_csv():

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
    response = {
        'message': message,
        'status': HTTP_CODE['OK']
    }
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run()
