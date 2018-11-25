import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = 'Database/MainDatabase.db'

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route("/flyReport")
def open_main_page():
    return render_template('ReportForm.html')

@app.route("/admin")
def open_admin_page():
    return render_template('admin.html')

@app.route("/home")
def open_home_page():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
