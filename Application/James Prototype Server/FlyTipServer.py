import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = 'databases/MainDatabase.db'

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route("/")
def open_main_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)