import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3
from werkzeug.utils import secure_filename

emailaddress = ""
DATABASE = 'Resources/Database/report.db'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'uploads')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

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
            for file in request.files.getlist('file'):
                if file.filename == '':
                    msg = 'no file name'
                elif file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    filePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    file.save(filePath)
                    msg = filePath
            # if user does not select file, browser also
            # submit a empty part without filename

    print(emailaddress)
    main(emailaddress)
    return render_template('ReportForm5.html', msg=msg)


@app.route("/flyReport")
def open_main_page():
    return render_template('ReportForm1.html')

@app.route("/admin")
def open_admin_page():
    return render_template('admin.html')

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

@app.route("/flyreport2")
def open_flyform2_page():
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("INSERT INTO `Waste` SET `tipLocation`= 'hello' WHERE id='0';")
        conn.commit()
        msg = "Record successfully added"
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        conn.close()
        return render_template('ReportForm3.html')

@app.route("/flyreport3")
def open_flyform3_page():
        try:
            conn = sqlite3.connect(DATABASE)
            cur = conn.cursor()
            cur.execute("UPDATE `Reports` SET `locationDescription`=? WHERE _id_='0';")
            conn.commit()
            msg = "Record successfully added"
        except:
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return render_template('ReportForm4.html')

@app.route("/flyreport4")
def open_flyform4_page():
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        cur.execute("UPDATE `Reports` SET `wasteDescription`=? WHERE _rowid_='0';")
        conn.commit()
        msg = "Record successfully added"
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        conn.close()
        return render_template('ReportForm5.html')

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


if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8080) #/to run this on your phone please uncomment this and type yourinternetipaddress(ipv4):8080/home
    app.run(debug=True)
    main()
