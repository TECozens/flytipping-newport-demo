import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = 'Database/report.db'

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


@app.route("/flyReport")
def open_main_page():
    return render_template('ReportForm1.html')

@app.route("/admin")
def open_admin_page():
    return render_template('admin.html')

@app.route("/home")
def open_home_page():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)

try:
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO tipLocation")
    conn.commit()
    msg = "Record successfully added“
except:
    conn.rollback()
    msg = "error in insert operation“
finally:
    return msg
    conn.close()

try:
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO locationDescription")
    conn.commit()
    msg = "Record successfully added“
except:
    conn.rollback()
    msg = "error in insert operation“
finally:
    return msg
    conn.close()

try:
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO wasteID")
    conn.commit()
    msg = "Record successfully added“
except:
    conn.rollback()
    msg = "error in insert operation“
finally:
    return msg
    conn.close()

try:
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO wasteSizeID")
    conn.commit()
    msg = "Record successfully added“
except:
    conn.rollback()
    msg = "error in insert operation“
finally:
    return msg
    conn.close()

try:
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO wasteDescription")
    conn.commit()
    msg = "Record successfully added“
except:
    conn.rollback()
    msg = "error in insert operation“
finally:
    return msg
    conn.close()

try:
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO imageID")
    conn.commit()
    msg = "Record successfully added“
except:
    conn.rollback()
    msg = "error in insert operation“
finally:
    return msg
    conn.close()

try:
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO witness")
    conn.commit()
    msg = "Record successfully added“
except:
    conn.rollback()
    msg = "error in insert operation“
finally:
    return msg
    conn.close()

try:
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO witnessID")
    conn.commit()
    msg = "Record successfully added“
except:
    conn.rollback()
    msg = "error in insert operation“
finally:
    return msg
    conn.close()

try:
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO emailaddress")
    conn.commit()
    msg = "Record successfully added“
except:
    conn.rollback()
    msg = "error in insert operation“
finally:
    return msg
    conn.close()
