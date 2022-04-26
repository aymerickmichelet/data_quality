from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import uuid
import os

CSV_EXTENSION = ".csv"


def upload_csv(file: FileStorage):
    global CSV_EXTENSION
    original_filename = os.path.splitext(file.filename)[0]
    random_filename = secure_filename(original_filename) + "-" + uuid.uuid4().hex + CSV_EXTENSION
    file.save(os.path.join('upload', random_filename))
    # return os.path.join('upload', random_filename)
    return random_filename
