from flask import Flask
from models import (init_db, insert_url, get_url, get_all_urls, increment_visit_count, delete_url_by_code)
import random
import string

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello to python learners from chaicode"

@app.route("/about")
def about():
    return "This is an amazing course on python - Udemy"


if __name__ == '__main__':
    app.run(debug=True)
