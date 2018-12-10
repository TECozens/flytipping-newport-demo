import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3
from werkzeug.utils import secure_filename

emailaddress = "test@test.com"
DATABASE = 'Resources/Database/report.db'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'do.not.reply.flytip@gmail.com'
PASSWORD = 'NSAflytip'

def read_template(filename):

    "Returns the Template"

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main(email):

    message_template = read_template('message.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    msg = MIMEMultipart()       # create a message

    # adds email to template and fills in email
    message = message_template.substitute(PERSON_NAME=email)
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']="confirmation of report"

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg

    # Terminate the SMTP session and close the connection
    s.quit()

#if __name__ == '__main__':
    #main()


def allowed_file(filename):
    ext = filename.rsplit('.', 1)[1]
    print(ext)
    return '.' in filename and ext in ALLOWED_EXTENSIONS


@app.route("/flyReport")
def open_main_page():
    return render_template('ReportForm1.html')

@app.route("/admin")
def open_admin_page():
    username = request.cookies.get('username')
    return render_template('admin.html')

# Cookie sessions
app.secret_key = 'fj590Rt?h40gg'

@app.route("/AdminLogin", methods = ['GET','POST'])
def login():
    if request.method=='POST':
        reminder =". "
        uName = request.form.get('username', default="Error")
        pw = request.form.get('password', default="Error")
        if checkCredentials(uName, pw):
            resp = make_response(render_template('AdminPanel.html', msg='hello '+uName+reminder, username = uName))
            session['username'] = request.form['username']
            session['Password'] = 'pa55wrd'
        else:
            resp = make_response(render_template('AdminPanel.html', msg='Incorrect  login',username='Guest'))
        return resp
    else:
        username = 'none'
        if 'username' in session:
            username = escape(session['username'])
        return render_template('admin.html', msg='', username = username)

# =======================================================================
#       methods
def checkCredentials(uName, pw):
    return pw == 'ian'
# =======================================================================

@app.route("/home")
def open_home_page():
    return render_template('home.html')

@app.route("/flyreport1", methods=["POST"])
def open_flyform1_page():
    global emailaddress
    locationDescription = request.form.get("locationDescription", default ="error")
    tipLocation = request.form.get("tipLocation", default ="error")
    emailaddress = request.form.get("emailaddress", default ="error")
    print(emailaddress)
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        print("connecting")
        cur.execute("INSERT INTO Reports ('tipLocation', 'locationDescription', 'emailaddress')\
                     VALUES(?,?,?)",(tipLocation, locationDescription, emailaddress) )
        print('connected')
        conn.commit()
        print("An Error2")
        msg = "Record successfully added"
        print("An Error3")
    except:
        conn.rollback()
        msg = "error in insert operation"

    finally:
        conn.close()
        return render_template('ReportForm2.html')

@app.route("/flyreport2", methods=["POST"])
def open_flyform2_page():
    wastetypeID = request.form.get("wastetypeID", default ="error")
    wasteSize = request.form.get("wasteSize", default ="error")
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        print('Connecting')
        cur.execute("INSERT INTO Reports ('wastetypeID', 'wasteSize')\
                     VALUES(?,?)",(wastetypeID, wasteSize))
        print('connected')
        conn.commit()
        print("An Error2")
        msg = "Record successfully added"
        print("An Error3")
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        conn.close()
        return render_template('ReportForm3.html')

@app.route("/flyreport3", methods=['POST'])
def open_flyform3_page():
    contactnumber = request.form.get("contactnumber", default ="error")
    print("above contact number")
    print(contactnumber)
    print("below contact number")
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        print('connecting')
        cur.execute("UPDATE Reports SET contactnumber = 10 WHERE id=(SELECT MAX(Id) FROM Reports);")

        print('connected')
        conn.commit()
        msg = "Record successfully added"
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        conn.close()
        return render_template('ReportForm4.html')

@app.route('/flyreport4', methods=['GET','POST'])
def upload_file():
    msg = ''
    if request.method == 'POST':
        msg = 'ok'
        # check if the post request has the file part
        if 'file' not in request.files:
            msg = 'no file given'
        else:
            # file = request.files['file']
            if len(request.files.getlist('file')) > 4:
                print('Cannot excced more than 4 images')
                return render_template('ReportForm5.html')
            else:
                for file in request.files.getlist('file'):
                    if file.filename == '':
                        msg = 'no file name'
                    elif file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                        file.save(filePath)
                        # if user does not select file, browser also
                        # submit a empty part without filename
                        main(emailaddress)
                        try:
                            conn = sqlite3.connect(DATABASE)
                            cur = conn.cursor()
                            print(filePath)
                            print('connecting')
                            cur.execute("INSERT INTO Image (imagePath1) VALUES(?)", (filePath,) )
                            print('connected')
                            conn.commit()
                            msg = "Record successfully added"
                        except Exception as err:
                            conn.rollback()
                            msg = "error in insert operation"
                            print(msg)
                            print(err)
                        finally:
                            conn.close()
                            print(msg)
    return render_template('ReportForm5.html')

                    # return render_template('ReportForm5.html')

# @app.route("/flyreport4")
# def open_flyform4_page():
#     try:
#         conn = sqlite3.connect(DATABASE)
#         cur = conn.cursor()
#         cur.execute("UPDATE `Reports` SET `wasteDescription`=? WHERE _rowid_='0';")
#         conn.commit()
#         msg = "Record successfully added"
#     except:
#         conn.rollback()
#         msg = "error in insert operation"
#     finally:
#         conn.close()
#         return render_template('ReportForm5.html')

@app.route("/flyreport5")
def open_flyform5_page():
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            conn.commit()
            msg = "Record successfully added"
        except:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return render_template('home.html')

@app.route("/allReports")
def allReports():
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            print('Connecting')
            cur.execute('select * from Reports;')
            print('connected')
            rows = cur.fetchall()
            name = rows
            return rows
        except:
            conn.rollback()
            msg = "error"
        finally:
            conn.close()

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8080) #/to run this on your phone please uncomment this and type yourinternetipaddress(ipv4):8080/home
    app.run(debug=True)
    main()
