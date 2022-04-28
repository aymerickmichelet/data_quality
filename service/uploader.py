from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
import uuid
import os

XLSX_EXTENSION = ".xlsx"


def upload_xlsx(file: FileStorage):
    global XLSX_EXTENSION
    original_filename = os.path.splitext(file.filename)[0]
    random_filename = secure_filename(original_filename) + "-" + uuid.uuid4().hex + XLSX_EXTENSION
    filenames = {
        "path": os.path.join('static/upload', random_filename),
        "filename": random_filename
    }
    file.save(filenames["path"])
    return filenames
