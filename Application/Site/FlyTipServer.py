import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3

DATABASE = 'Resources/Database/report.db'

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

@app.route("/flyreport2")
def open_flyform2_page():
    try:
        print('1')
        conn = sqlite3.connect(DATABASE)
        print('2')
        cur = conn.cursor()
        # cur.execute("UPDATE `Reports` SET `tipLocation`=? WHERE _rowid_='0';")
        # conn.commit()
        msg = "Record successfully added"
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        conn.close()
    return render_template('ReportForm2.html')

@app.route("/flyreport3")
def open_flyform3_page():
        # try:
        #     conn = sqlite3.connect(DATABASE)
        #     cur = conn.cursor()
        #     cur.execute("UPDATE `Reports` SET `locationDescription`=? WHERE _rowid_='0';")
        #     conn.commit()
        #     msg = "Record successfully added"
        # except:
        #     conn.rollback()
        #     msg = "error in insert operation"
        # finally:
        #     conn.close()
        return render_template('ReportForm3.html')

@app.route("/flyreport4")
def open_flyform4_page():
    # try:
    #     conn = sqlite3.connect(DATABASE)
    #     cur = conn.cursor()
    #     cur.execute("UPDATE `Reports` SET `wasteDescription`=? WHERE _rowid_='0';")
    #     conn.commit()
    #     msg = "Record successfully added"
    # except:
    #     conn.rollback()
    #     msg = "error in insert operation"
    # finally:
    #     conn.close()
    return render_template('ReportForm4.html')

@app.route("/flyreport5")
def open_flyform5_page():
        # try:
        #     conn = sqlite3.connect(DATABASE)
        #     cur = conn.cursor()
        #     cur.execute("UPDATE `Reports` SET `emailaddress`=? WHERE _rowid_='0';")
        #     conn.commit()
        #     msg = "Record successfully added"
        # except:
        #     conn.rollback()
        #     msg = "error in insert operation"
        # finally:
        #     conn.close()
        return render_template('ReportForm5.html')


if __name__ == "__main__":
    app.run(debug=True)
