from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import uuid
import os

XLSX_EXTENSION = ".xlsx"


def upload_csv(file: FileStorage):
    global XLSX_EXTENSION
    original_filename = os.path.splitext(file.filename)[0]
    random_filename = secure_filename(original_filename) + "-" + uuid.uuid4().hex + XLSX_EXTENSION
    file.save(os.path.join('upload', random_filename))
    # return os.path.join('upload', random_filename)
    return random_filename
