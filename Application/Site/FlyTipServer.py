import os
from flask import Flask, redirect, request, render_template, make_response, escape, session
import sqlite3
from werkzeug.utils import secure_filename

emailaddress = "test@test.com"
DATABASE = 'Resources/Database/reports.db'

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
    Position = request.form.get("position", default = "error")
    print(emailaddress)
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        print("connecting")
        cur.execute("INSERT INTO Reports ('tipLocation', 'locationDescription', 'emailaddress', 'Position')\
                     VALUES(?,?,?,?)",(tipLocation, locationDescription, emailaddress, Position) )
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

@app.route("/flyreport2", methods=['POST'])
def open_flyform2_page():

    wasteselection = []
    for i in range(1,13):
        waste = request.form.getlist(f'{i}')
        if waste == ['on']:
            wasteselection.append("true")
        else:
            wasteselection.append("false")
    print(wasteselection)


    wasteSize = request.form['wasteSize']
    print(wasteSize)

    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        print('Connecting')
        cur.execute("INSERT INTO wastetypeID ('blackbags-househould', 'whiteGoods', 'furniture', 'mattress', 'otherUnidentified', 'greenWaste', 'blackBags-commercial', 'otherCommercialWaste', 'vehicleParts', 'asbestos', 'clinical', 'animalCarcass')\
                     VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",(wasteselection[0], wasteselection[1], wasteselection[2], wasteselection[3], wasteselection[4], wasteselection[5], wasteselection[6], wasteselection[7], wasteselection[8], wasteselection[9], wasteselection[10], wasteselection[11]) )
        cur.execute("UPDATE Reports SET ('wasteSize') = (?) WHERE id=(SELECT MAX(Id) FROM Reports)", (wasteSize,))
        conn.commit()
        msg = "Record successfully added"
    except:
        conn.rollback()
        msg = "error in insert operation"
    finally:
        conn.close()
        return render_template('ReportForm3.html')

@app.route("/flyreport3", methods=['POST'])
def open_flyform3_page():
    contactnumber = request.form.get("contactnumber", default ="error")
    firstname = request.form.get("firstname", default ="error")
    surname = request.form.get("surname", default ="error")
    witness = request.form.getlist('witness')
    print(witness)
    if witness == ['on']:
        witness = "yes"
    else:
        witness = "no"
    print(contactnumber)
    print(firstname)
    print(surname)
    print(witness)
    try:
        conn = sqlite3.connect(DATABASE)
        cur = conn.cursor()
        print('connecting')

        cur.execute("UPDATE Reports SET ('contactnumber', 'firstname', 'surname', 'witness') = (?,?,?,?) WHERE id=(SELECT MAX(Id) FROM Reports)", (contactnumber,firstname,surname,witness,))

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
    numberofimages=['','','' ,'']
    msg = ''
    main(emailaddress)
    if request.method == 'POST':
        msg = 'ok'
        print(msg)
        # check if the post request has the file part
        if 'file' not in request.files:
            msg = 'no file given'
            print(msg)
        else:
            # file = request.files['file']
            if len(request.files.getlist('file')) > 4:
                msg = 'Cannot exceed more than 4 images'
                print(msg)
                return render_template('ReportForm4.html', msg=msg)
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
                        del numberofimages[0]
                        numberofimages.append(filePath)
                numberofimages = numberofimages[::-1]
                imagepath1, imagepath2, imagepath3, imagepath4 = numberofimages
                try:
                    conn = sqlite3.connect(DATABASE)
                    cur = conn.cursor()
                    print(filePath)
                    print('connecting')
                    cur.execute("INSERT INTO Image (imagePath1, imagePath2, imagePath3, imagePath4)\
                                 VALUES(?,?,?,?)", (imagepath1, imagepath2, imagepath3, imagepath4) )
                    print('connected')
                    conn.commit()
                    print('trying id')
                    cur.execute("UPDATE Reports SET imageID =(SELECT MAX(imageID) FROM Image) WHERE id=(SELECT MAX(Id) FROM Reports)")
                    print('id successfull')
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
        except:
            msg = "Record successfully added"
            conn.rollback()
            msg = "error in insert operation"
        finally:
            conn.close()
            return render_template('home.html')

@app.route("/Reports") #change this to /Reports later
def future():
    print("In Admin")
    try:
         conn = sqlite3.connect(DATABASE)
         cur = conn.cursor()
         print("in the try1")
         cur.execute("SELECT * FROM Reports")
         print("in the try2")
         # print(data)
         data = cur.fetchall()
         print("in the try")
         print (str(data))
        #  return str(data)
    except:
        conn.rollback()
        msg = "error"
    finally:
        conn.close()
    return render_template('AdminPanel.html', report=data)

# @app.route("/Locations") 
# def locations():
#     print("In Admin")
#     try:
#          conn = sqlite3.connect(DATABASE)
#          cur = conn.cursor()
#          print("in the try1")
#          cur.execute("SELECT * FROM Reports WHERE ")
#          print("in the try2")
#          # print(data)
#          data = cur.fetchall()
#          print("in the try")
#          print (str(data))
#         #  return str(data)
#     except:
#         conn.rollback()
#         msg = "error"
#     finally:
#         conn.close()
#     return render_template('AdminPanel.html', report=data)

if __name__ == "__main__":
    # app.run(host='0.0.0.0', port=8080) #/to run this on your phone please uncomment this and type yourinternetipaddress(ipv4):8080/home
    app.run(debug=True)
    main()
