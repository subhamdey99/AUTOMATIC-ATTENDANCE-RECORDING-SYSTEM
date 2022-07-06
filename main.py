############################################# IMPORTING ################################################
import email
from faulthandler import disable
from logging import PlaceHolder
import tkinter as tk
from tkinter import DISABLED, END, ttk
from tkinter import messagebox as mess
from tkinter.font import NORMAL
import tkinter.simpledialog as tsd
import cv2
import os
import csv
import numpy as np
from PIL import Image
import pandas as pd
import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint
from pymongo import MongoClient
############################################# FUNCTIONS ################################################

def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

##################################################################################

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(200,tick)

###################################################################################

def contact():
    mess._show(title='Contact us', message="Please contact us on : 'mandalmilan356@gmail.com' ")

###################################################################################

def check_haarcascadefile():
    exists = os.path.isfile("haarcascade_frontalface_default.xml")
    if exists:
        pass
    else:
        mess._show(title='Some file missing', message='Please contact us for help')
        window.destroy()

###################################################################################

def save_pass():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        master.destroy()
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    op = (old.get())
    newp= (new.get())
    nnewp = (nnew.get())
    if (op == key):
        if(newp == nnewp):
            txf = open("TrainingImageLabel\psd.txt", "w")
            txf.write(newp)
        else:
            mess._show(title='Error', message='Confirm new password again!!!')
            return
    else:
        mess._show(title='Wrong Password', message='Please enter correct old password.')
        return
    mess._show(title='Password Changed', message='Password changed successfully!!')
    master.destroy()

###################################################################################

def OTPVerification():
    #EnOTP.destroy()
    client=MongoClient()
    client = MongoClient("mongodb://localhost:27017/")
    mydatabase = client['project']
    otpcollection=mydatabase['otp']

    data = mydatabase.otpcollection.find({"Email" : receiver_email}).sort("DateTime",-1).limit(1)
    sOTP = data[0]['OTP']
    
    cOTP = (InOTP.get())
    #print(sOTP)
    #print(xxx)

    if str(cOTP) == str(sOTP):
        EnOTP.destroy()
        with open("VerifiedEmails/Emails.csv", 'a+',newline='', encoding='utf-8') as csvFile1:
            emails = []
            emails.append(receiver_email)
            writer = csv.writer(csvFile1)
            writer.writerow(emails)
        csvFile1.close()
        mess._show(title='Success', message='OTP Verified!')
    else:
        mess._show(title='OTP', message='Incorrect OTP!')


#######################################################################################

def change_pass():
    global master
    master = tk.Tk()
    master.geometry("400x160")
    master.resizable(False,False)
    master.title("Change Password")
    master.configure(background="white")
    lbl4 = tk.Label(master,text='    Enter Old Password',bg='white',font=('century gothic', 12, ' bold '))
    lbl4.place(x=10,y=10)
    global old
    old=tk.Entry(master,width=25 ,fg="black",relief='solid',font=('century gothic', 12, ' bold '),show='*')
    old.place(x=180,y=10)
    lbl5 = tk.Label(master, text='   Enter New Password', bg='white', font=('century gothic', 12, ' bold '))
    lbl5.place(x=10, y=45)
    global new
    new = tk.Entry(master, width=25, fg="black",relief='solid', font=('century gothic', 12, ' bold '),show='*')
    new.place(x=180, y=45)
    lbl6 = tk.Label(master, text='Confirm New Password', bg='white', font=('century gothic', 12, ' bold '))
    lbl6.place(x=10, y=80)
    global nnew
    nnew = tk.Entry(master, width=25, fg="black", relief='solid',font=('century gothic', 12, ' bold '),show='*')
    nnew.place(x=180, y=80)
    cancel=tk.Button(master,text="Cancel", command=master.destroy ,fg="black"  ,bg="red" ,height=1,width=25 , activebackground = "white" ,font=('century gothic', 10, ' bold '))
    cancel.place(x=200, y=120)
    save1 = tk.Button(master, text="Save", command=save_pass, fg="black", bg="#3ece48", height = 1,width=25, activebackground="white", font=('century gothic', 10, ' bold '))
    save1.place(x=10, y=120)
    master.mainloop()

#####################################################################################

def otpWindow():
    global EnOTP
    EnOTP = tk.Tk()
    EnOTP.geometry("400x160")
    EnOTP.eval('tk::PlaceWindow . center')
    EnOTP.resizable(False,False)
    EnOTP.title("Enter OTP")
    EnOTP.configure(background="white")
    lbl8 = tk.Label(EnOTP,text='    Enter OTP    ',bg='white',font=('century gothic', 12, ' bold '))
    lbl8.place(x=10,y=10)
    global InOTP
    InOTP=tk.Entry(EnOTP,width=20 ,fg="black",relief='solid',font=('century gothic', 12, ' bold '),show='*')
    InOTP.place(x=180,y=10)
    cancel1=tk.Button(EnOTP,text="Cancel", command=EnOTP.destroy ,fg="black"  ,bg="red" ,height=1,width=25 , activebackground = "white" ,font=('century gothic', 10, ' bold '))
    cancel1.place(x=200, y=120)
    resend=tk.Button(EnOTP,text="Resend", command=resendOTP,fg="black"  ,bg="grey" ,height=1,width=25 , activebackground = "white" ,font=('century gothic', 10, ' bold '))
    resend.place(x=105, y=80)
    save3 = tk.Button(EnOTP, text="Verify", command=OTPVerification, fg="black", bg="#3ece48", height = 1,width=25, activebackground="white", font=('century gothic', 10, ' bold '))
    save3.place(x=10, y=120)
    EnOTP.mainloop()

#####################################################################################

def psw():
    assure_path_exists("TrainingImageLabel/")
    exists1 = os.path.isfile("TrainingImageLabel\psd.txt")
    if exists1:
        tf = open("TrainingImageLabel\psd.txt", "r")
        key = tf.read()
    else:
        new_pas = tsd.askstring('Old Password not found', 'Please enter a new password below', show='*')
        if new_pas == None:
            mess._show(title='No Password Entered', message='Password not set!! Please try again')
        else:
            tf = open("TrainingImageLabel\psd.txt", "w")
            tf.write(new_pas)
            mess._show(title='Password Registered', message='New password was registered successfully!!')
            return
    password = tsd.askstring('Password', 'Enter Password', show='*')
    if (password == key):
        TrainImages()
    elif (password == None):
        pass
    else:
        mess._show(title='Wrong Password', message='You have entered wrong password')

######################################################################################

def clear():
    txt.delete(0, 'end')
    res = "1)Take Images  >>  2)Save Profile"
    message1.configure(text=res)


def clear2():
    txt2.delete(0, 'end')
    res = "1)Take Images  >>  2)Save Profile"
    message1.configure(text=res)

def clear3():
    txt3.delete(0, 'end')
    res = "1)Take Images  >>  2)Save Profile"
    message1.configure(text=res)

def clear4():
    txt4.delete(0, 'end')
    res = "1)Take Images  >>  2)Save Profile"
    message1.configure(text=res)

#######################################################################################

def SendOTP():
    email = (txt3.get())
    exists6 = os.path.exists("StudentDetails/StudentDetails.csv")
    flag5 = 0
    if exists6:
        with open("StudentDetails/StudentDetails.csv", 'r') as em:
            content = list(csv.reader(em))
            for row in content:
                    if row:
                        #print(row)
                        if row[6] == email:
                            flag5+=1
                            id1 = row[2]
                            break
        em.close()

    DEmail = (txt3.get())
    exists9 = os.path.exists("VerifiedEmails/Emails.csv")
    flag4 = 0
    if exists9:
        with open("VerifiedEmails/Emails.csv", 'r') as dd:
            lst = csv.reader(dd)
            #lst = list(lst)
            for each in lst:
                if each[0] == DEmail:
                  flag4+=1
                  break
        dd.close()  
    if flag5 == 0:
        if flag4 == 0:
            client=MongoClient()
            client = MongoClient("mongodb://localhost:27017/")
            mydatabase = client['project']
            otpcollection=mydatabase['otp']


            otp = randint(000000,999999)
            timestamp = datetime.datetime.utcnow()
            data = {}
            data['email'] = email
            data['otp'] = otp
            mydatabase.otpcollection.create_index( "DateTime" ,expireAfterSeconds =120)
            mydatabase.otpcollection.insert_one({"OTP":otp,"DateTime": timestamp, "Email": email})

            html = '''
                <html>
                    <body>
                        <h3>Your OTP for Automatic Attendance Recording System is {}</h3>
                        <h3>This code will expire in 2 minutes.</h3>
                    </body>
                </html>
                '''.format(otp)



            port =587
            smtp_server = "smtp.gmail.com"
            sender_email = "subhamdey297@gmail.com"
            global receiver_email 
            receiver_email = email

            password = "dfogajpksrepwxii"


            email_message = MIMEMultipart()
            email_message['From'] = sender_email
            email_message['To'] = receiver_email
            email_message['Subject'] = "Email Verification OTP"
            email_message.attach(MIMEText(html, "html"))
            email_string = email_message.as_string()
            #print(email_string)

            server = smtplib.SMTP(smtp_server, port)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, email_string)
            server.quit()

            mess._show(title='Success', message='Email Verification OPT sent')
            otpWindow()

        else:
            message1.configure(text="Email already verified!")   
    else:
        message1.configure(text="Email already in use with ID "+id1)
        #mess._show(title='Email Error', message='Email already in use with ID '+id1)
        #print(id1)
#######################################################################################

def resendOTP():
    EnOTP.destroy()
    SendOTP()

#######################################################################################

def TakeImages():
    CEmail = (txt3.get())
    exists8 = os.path.exists("VerifiedEmails/Emails.csv")
    flag2 = 0
    if exists8:
        with open("VerifiedEmails/Emails.csv", 'r') as ab:
            lst = csv.reader(ab)
            #lst = list(lst)
            for each in lst:
                if each[0] == CEmail:
                  flag2+=1
                  break
        ab.close()
    exists10 = os.path.exists("StudentDetails\StudentDetails.csv")
    flag3 = 0
    if exists10:
        roll = (txt.get())
        with open("StudentDetails\StudentDetails.csv", 'r') as cc:
            lst = csv.reader(cc)
            #lst = list(lst)
            for each in lst:
                if each:
                    if each[2] == roll:
                        flag3+=1
                        break
    
    if flag3 == 0:
        if flag2 == 1:
            check_haarcascadefile()
            columns = ['SERIAL NO.', '', 'ID', '', 'NAME', '', 'EMAIL']
            assure_path_exists("StudentDetails/")
            assure_path_exists("TrainingImage/")
            serial = 0
            exists = os.path.isfile("StudentDetails\StudentDetails.csv")
            if exists:
                with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
                    reader1 = csv.reader(csvFile1)
                    for l in reader1:
                        serial = serial + 1
                serial = (serial // 2)
                
                csvFile1.close()
            else:
                with open("StudentDetails\StudentDetails.csv", 'a+') as csvFile1:
                    writer = csv.writer(csvFile1)
                    writer.writerow(columns)
                    serial = 1
                csvFile1.close()
            Id = (txt.get())
            name = (txt2.get())
            email = (txt3.get())

            # Validation of name
            if ((name.isalpha()) or (' ' in name)):
                cam = cv2.VideoCapture(0)
                harcascadePath = "haarcascade_frontalface_default.xml"
                detector = cv2.CascadeClassifier(harcascadePath)
                sampleNum = 0
                while (True):
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2) # Draw rectanlge on face in cam recorder
                        # incrementing sample number
                        sampleNum = sampleNum + 1
                        # saving the captured face in the dataset folder TrainingImage
                        cv2.imwrite("TrainingImage\ " + name + "." + str(serial) + "." + Id + '.' + str(sampleNum) + ".jpg",
                                    gray[y:y + h, x:x + w])
                        # display the frame
                        cv2.imshow('Taking Images', img)
                    # wait for 20 miliseconds
                    if cv2.waitKey(100) & 0xFF == ord('q'): # Waiting time for registration of face id
                        break
                    # break if the sample number is morethan 100
                    elif sampleNum > 100:
                        break
                cam.release()
                cv2.destroyAllWindows()
                res = "Images Taken for ID : " + Id
                row = [serial, '', Id, '', name, '',email]
                with open('StudentDetails\StudentDetails.csv', 'a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                message1.configure(text=res)
            else:
                if (name.isalpha() == False): # if numerical value is entered for name
                    res = "Enter Correct name"
                    message.configure(text=res)
        else:
            mess._show(title='Email Error', message='Email not verified! Please verify!')
    else:
        mess._show(title='Roll No Error', message='You are already registerd!')

########################################################################################

def TrainImages():
    check_haarcascadefile()
    assure_path_exists("TrainingImageLabel/")
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, ID = getImagesAndLabels("TrainingImage")
    try:
        recognizer.train(faces, np.array(ID))
    except:
        mess._show(title='No Registrations', message='Please Register someone first!!!')
        return
    recognizer.save("TrainingImageLabel\Trainner.yml")
    res = "Profile Saved Successfully"
    message1.configure(text=res)
    message.configure(text='Total Registrations till now  : ' + str(ID[0]))

############################################################################################3

def getImagesAndLabels(path):
    # get the path of all the files in the folder
    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
    # create empth face list
    faces = []
    # create empty ID list
    Ids = []
    # now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        # loading the image and converting it to gray scale
        pilImage = Image.open(imagePath).convert('L')
        # Now we are converting the PIL image into numpy array
        imageNp = np.array(pilImage, 'uint8')
        # getting the Id from the image
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(ID)
    return faces, Ids

###########################################################################################

def subject():
    SUBJECT = ''
    weekday=0
    exists7 = os.path.exists("TimeTable/TimeTable.csv")
    if exists7:
        with open("TimeTable/TimeTable.csv", 'r') as tt:
            weekday=datetime.datetime.today().weekday()
            #print('weekday: ',weekday)
            timetable = csv.reader(tt)

            routine = list(timetable)
            

            hr = datetime.datetime.now().hour

            # if hr>=9 and hr<=12:
            #print('Hour: ',hr)
            #print('Routine header ',routine[0])
            #print('Current routine', routine[weekday+1])

            col=0
            # Finding the column index for that partitucar hour
            for hour in routine[0]:
                if hour.isdigit():
                    if int(hour)==hr:
                        #print('Current hours: ',hr)
                        #print('Col: ',col)
                        break
                    
                col += 1
            try:
                SUBJECT = routine[weekday+1][col]
                
            except IndexError:
                SUBJECT = "NIL"
    else:
        mess._show(title='FileNotFound', message='Time Table file is missing')
    tt.close()
    return(SUBJECT)
###########################################################################################

def TrackImages():
    SUBJECT = subject()
    if SUBJECT == "NIL":
        mess._show(title='No Class', message='There is no class in this period')
    else:
        check_haarcascadefile()
        assure_path_exists("Attendance/")
        assure_path_exists("StudentDetails/")
        for k in tv.get_children():
            tv.delete(k)
        msg = ''
        i = 0
        j = 0
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer() # Face Detection
        exists3 = os.path.isfile("TrainingImageLabel\Trainner.yml")
        if exists3:
            recognizer.read("TrainingImageLabel\Trainner.yml")
        else:
            mess._show(title='Data Missing', message='Please click on Save Profile to reset data!!')
            return
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);

        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        date = datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y')

    
        col_names = ['Id', 'Name', str(date)]
        exists1 = os.path.isfile("StudentDetails\StudentDetails.csv")
        if exists1:
            df = pd.read_csv("StudentDetails\StudentDetails.csv")
        else:
            mess._show(title='Details Missing', message='Students details are missing, please check!')
            cam.release()
            cv2.destroyAllWindows()
            window.destroy()

            # ######################################################################## 


            # ######################################################################## 
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 2)
                serial, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
                    date_ = datetime.datetime.fromtimestamp(ts).strftime('%m-%Y')
                    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['SERIAL NO.'] == serial]['NAME'].values
                    ID = df.loc[df['SERIAL NO.'] == serial]['ID'].values
                    ID = str(ID)
                    ID = ID[1:-1]
                    bb = str(aa)
                    bb = bb[2:-2]
                    attendance = [ID,bb]
                    
                else:
                    Id = 'Not recognized'
                    bb = str(Id)
                
                cv2.putText(im, str(bb), (x, y + h), font, 1, (255, 255, 255), 2)
            cv2.imshow('Taking Attendance', im)

            
            if (cv2.waitKey(1) == ord('q')):
                cv2.destroyAllWindows()
                break



            ########################################################################

        
    
        
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%m-%Y')
        exists = os.path.isfile("Attendance/"+SUBJECT+'_'+ date + ".csv")
        if exists:

            # with open("Attendance\Attendance_" + date  + '_' + SUBJECT + ".csv", 'a+') as csvFile1:
            #     writer = csv.writer(csvFile1)
            #     writer.writerow(attendance)
            # csvFile1.close()

            date_header = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
            content=[]
            flag = 0
            ind = 0
            with open("Attendance/"+SUBJECT+'_'+ date + ".csv",'r+',newline='') as f:
                content = csv.reader(f)
                content = list(content)
                size = len(content[0])
                header = content[:1][0]
                row = content[1:]
                # print(header)
                # print(row)
                if str(date_header) not in content[0]:
                    content[0].append(str(date_header))
                ind=content[0].index(str(date_header))
                #print(ind)
                for each in content:
                    #print(each)
                    if each:
                        if each[0]==attendance[0]:
                            x = each.index(each[-1])
                            #print(x)
                            if ind !=x:
                                e = ind - x
                                if e>1:
                                    for i in range(e-1):
                                        each.append('')
                                    each.append(str(timestamp))
                                    flag+=1
                                    
                                else:
                                    each.append(str(timestamp))
                                    flag+=1
                                
                                        
                            else:
                                flag+=1
                                mess._show(title='Recorded', message='Your Attendance Already Recorded For This Class')
                                #window.destroy()
                        #     row.append(attendance)
                        #     break
                            #content[z].append(attendance)
                if flag == 0:
                    if ind>2:
                        if ind != x:
                            for i in range(ind-2):
                                attendance.append('')
                            attendance.append(str(timestamp))
                            row.append(attendance)
                        # else:
                        #     mess._show(title='Recorded', message='Your Attendance Already Recorded For This Class')
                    else:
                        
                        attendance.append(str(timestamp))
                        row.append(attendance)
                #print(content)

            f.close()

            with open("Attendance/"+ SUBJECT+'_'+ date + ".csv",'w',newline='') as f:
                w_obj = csv.writer(f)
                w_obj.writerow(header)
                w_obj.writerows(row)
            f.close()

        
        else:
            with open("Attendance/"+SUBJECT+'_'+ date + ".csv", 'a+',newline='', encoding='utf-8') as csvFile1:
                attendance.append(str(timestamp))
                writer = csv.writer(csvFile1)
                writer.writerow(col_names)
                writer.writerow(attendance)
            csvFile1.close()
        exists4 = os.path.isfile("Attendance/"+SUBJECT+'_'+ date + ".csv")
        if exists4:
            with open("Attendance/"+SUBJECT+'_'+ date + ".csv",'r',newline='') as csvFile1:
                reader = csv.reader(csvFile1)
                next(reader)
                reader = list(reader)
                for lines in reader:
                    iidd = str(lines[0]) + '   '
                    tv.insert('', 0, text=iidd, values=(str(lines[1]), str(lines[-1])))
            csvFile1.close()
        cam.release()
        cv2.destroyAllWindows()


#################################################################################################

def generateReport():
    # Find Email
    d = (txt4.get())
    reciever = ""
    with open("StudentDetails/StudentDetails.csv",'r', newline='', encoding='utf-8') as f:
        content = list(csv.reader(f))
        flag = 0
        flag1 = 0
        for row in content:
                if row:
                    #print(row)
                    if row[2]==d:
                        flag+=1
                        name = row[4]
                        reciever = row[6]
                        if reciever:
                            flag1+=1
                            #print(reciever)
                            break
        if flag == 0:
            flag1+=1
            mess._show(title='Error', message='You are not registered! Please register.')
        if flag1==0:
            mess._show(title='Email Error', message='Your Email is not registered!')
            #print("Your Email is not registered")
    f.close()
    if reciever:
        a = os.listdir('Attendance')
        #print(a)
        b = (txt4.get())
        b = "'"+b+"'"
        attendance=[]
        # Calculate Attendance
        for file in a:
            flag2 = 0
            with open("Attendance/"+file,'r', newline='', encoding='utf-8') as f:
                content = list(csv.reader(f))
                c = len(content[0])-2
                filename = file.split('.')
                filename = filename[0]
                #print(c)
                for row in content:
                    if row:
                        #print(row)
                        if row[0]==b:
                            flag2+=1
                            count = -2
                            for item in row:
                                #print(item)
                                if item:
                                    count+=1
                            per = count/c*100
                            per = "{:.2f}".format(per)
                            msg = 'Your Attendance Percentage in '
                            msg = msg+filename+" "
                            msg = msg+str(per)+'%'
                            attendance.append(msg)
                            #print(attendance)
                if flag2 == 0:
                    msg = 'Your Attendance Percentage in '
                    msg = msg+filename+" "
                    msg = msg+str(0)+'%'
                    attendance.append(msg)
            f.close()

        #print(attendance)

        port =587
        smtp_server = "smtp.gmail.com"
        sender_email = "subhamdey297@gmail.com"
        receiver_email = reciever
        #print(receiver_email)
        password = "dfogajpksrepwxii"

        html = '''
<html>
<body>
<h4>Hi {}</h4>
'''.format(name)
        for i in range(len(attendance)):
            html = html + "\n" + '<h4>' + attendance[i] + '</h4>'
        html = html + '\n' + '</body>' + '\n' + '</html>'
        email_message = MIMEMultipart()
        email_message['From'] = sender_email
        email_message['To'] = receiver_email
        email_message['Subject'] = "Attendance Report"
        email_message.attach(MIMEText(html, "html"))
        email_string = email_message.as_string()
        #print(email_string)
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, email_string)
        server.quit()
        mess._show(title='SUCCESS', message='The Mail has been sent successfully! Please check your mailbox')

######################################## USED STUFFS ############################################
    
global key
key = ''

ts = time.time()
date = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
day,month,year=date.split("-")

mont={'01':'January',
      '02':'February',
      '03':'March',
      '04':'April',
      '05':'May',
      '06':'June',
      '07':'July',
      '08':'August',
      '09':'September',
      '10':'October',
      '11':'November',
      '12':'December'
      }

def click(event):
    txt4.config(state=NORMAL)
    txt4.delete(0,END)

######################################## GUI FRONT-END ###########################################

window = tk.Tk()
window.geometry("1280x720")
window.resizable(True,False)
window.title("Automatic Attendance Recording System") # title
window.configure(background='#262523') # background of GUI

frame1 = tk.Frame(window, bg="#ecc6d9") # left frame window
frame1.place(relx=0.11, rely=0.17, relwidth=0.39, relheight=0.80) # size of left frame window

frame2 = tk.Frame(window, bg="#d98cb3") # Right Frame window
frame2.place(relx=0.51, rely=0.17, relwidth=0.38, relheight=0.80)

message3 = tk.Label(window, text="Automatic Attendance Recording System" ,fg="white",bg="#262523" ,width=55 ,height=1,font=('century gothic', 29, ' bold '))
message3.place(x=10, y=10)
# Heading with width, background color, font size, font type ...and son


frame3 = tk.Frame(window, bg="#c4c6ce") # frame3 for December 2021
frame3.place(relx=0.52, rely=0.09, relwidth=0.09, relheight=0.07)

frame4 = tk.Frame(window, bg="#c4c6ce") # frame4 for clock
frame4.place(relx=0.36, rely=0.09, relwidth=0.16, relheight=0.07)

datef = tk.Label(frame4, text = day+"-"+mont[month]+"-"+year+"  |  ", fg="orange",bg="#262523" ,width=55 ,height=1,font=('century gothic', 18, ' bold '))
datef.pack(fill='both',expand=1)

clock = tk.Label(frame3,fg="orange",bg="#262523" ,width=55 ,height=1,font=('century gothic', 22, ' bold '))
clock.pack(fill='both',expand=1) # fit the clock in frame
tick()

head2 = tk.Label(frame2, text="                       For New Registrations                       ", fg="black",bg="#79d2a6" ,font=('century gothic', 17, ' bold ') )
head2.grid(row=0,column=0)

head1 = tk.Label(frame1, text="                       For Already Registered                       ", fg="black",bg="#d98cb3" ,font=('century gothic', 17, ' bold ') )
head1.place(x=0,y=0)

lbl = tk.Label(frame2, text="Enter Roll No",width=20  ,height=1  ,fg="black"  ,bg="#d98cb3" ,font=('century gothic', 17, ' bold ') )
lbl.place(x=80, y=40)

txt = tk.Entry(frame2,width=32 ,fg="black",font=('century gothic', 15, ' bold ')) # Entry of Enter ID
txt.place(x=30, y=73)

lbl2 = tk.Label(frame2, text="Enter Name",width=20  ,fg="black"  ,bg="#d98cb3" ,font=('century gothic', 17, ' bold '))
lbl2.place(x=80, y=115)

txt2 = tk.Entry(frame2,width=32 ,fg="black",font=('century gothic', 15, ' bold ')  ) # Entry of Enter n
txt2.place(x=30, y=148)

lbl4 = tk.Label(frame2, text="Enter Email",width=20  ,fg="black"  ,bg="#d98cb3" ,font=('century gothic', 17, ' bold '))
lbl4.place(x=80, y=185)

lbl5 = tk.Label(frame1, text="Enter Roll No",width=10  ,fg="black"  ,bg="#ecc6d9" ,font=('century gothic', 14, ' bold '))
lbl5.place(x=55, y=385)

txt3 = tk.Entry(frame2,width=32 ,fg="black",font=('century gothic', 15, ' bold ')  )
txt3.place(x=30, y=218) # Email

txt4 = tk.Entry(frame1,width=20,fg="black",font=('century gothic', 15, ' bold ')  )
txt4.place(x=55,y=410) # Roll no for Report

message1 = tk.Label(frame2, text="1)Take Images  >>  2)Save Profile" ,bg="#d98cb3" ,fg="black"  ,width=39 ,height=1, activebackground = "yellow" ,font=('century gothic', 15, ' bold '))
message1.place(x=7, y=270)

message = tk.Label(frame2, text="" ,bg="#00aeff" ,fg="black"  ,width=39,height=1, activebackground = "yellow" ,font=('century gothic', 16, ' bold '))
message.place(x=7, y=450) # Right Frame

lbl3 = tk.Label(frame1, text="Attendance",width=18  ,fg="black"  ,bg="#00aeff"  ,height=1 ,font=('century gothic', 17, ' bold '))
lbl3.place(x=10, y=115) # Left Frame

lbl6 = tk.Label(frame1, text="Class: "+subject(),width=14  ,fg="black"  ,bg="#00aeff"  ,height=1 ,font=('century gothic', 17, ' bold '))
lbl6.place(x=278, y=115)

res=0
exists = os.path.isfile("StudentDetails\StudentDetails.csv")
if exists:
    with open("StudentDetails\StudentDetails.csv", 'r') as csvFile1:
        reader1 = csv.reader(csvFile1)
        for l in reader1:
            res = res + 1
    res = (res // 2) - 1 # res = No of registration
    
    csvFile1.close()
else:
    res = 0
message.configure(text='Total Registrations till now  : '+str(res))

##################### MENUBAR #################################

menubar = tk.Menu(window,relief='ridge')
filemenu = tk.Menu(menubar,tearoff=0)
filemenu.add_command(label='Change Password', command = change_pass)
filemenu.add_command(label='Contact Us', command = contact)
filemenu.add_command(label='Exit',command = window.destroy)
menubar.add_cascade(label='Help',font=('century gothic', 29, ' bold '),menu=filemenu)

################## TREEVIEW ATTENDANCE TABLE ####################

tv= ttk.Treeview(frame1,height =10,columns = ('name','time'))
tv.column('#0',width=115)
tv.column('name',width=217)
tv.column('time',width=145)
tv.grid(row=2,column=0,padx=(0,0),pady=(150,0),columnspan=4)
tv.heading('#0',text ='ID')
tv.heading('name',text ='NAME')
tv.heading('time',text ='TIME')

###################### SCROLLBAR ################################

scroll=ttk.Scrollbar(frame1,orient='vertical',command=tv.yview)
scroll.grid(row=2,column=4,padx=(0,100),pady=(150,0),sticky='ns')
tv.configure(yscrollcommand=scroll.set)

###################### BUTTONS ##################################

clearButton = tk.Button(frame2, text="Clear", command=clear  ,fg="black"  ,bg="green"  ,width=11 ,activebackground = "white" ,font=('century gothic', 10, ' bold '))
clearButton.place(x=335, y=73)
clearButton2 = tk.Button(frame2, text="Clear", command=clear2  ,fg="black"  ,bg="green"  ,width=11 , activebackground = "white" ,font=('century gothic', 10, ' bold '))
clearButton2.place(x=335, y=148) 
clearButton3 = tk.Button(frame2, text="Clear", command=clear3  ,fg="black"  ,bg="green"  ,width=8 , activebackground = "white" ,font=('century gothic', 10, ' bold '))
clearButton3.place(x=285, y=218)
clearButton4 = tk.Button(frame1, text="Clear", command=clear4  ,fg="black"  ,bg="green"  ,width=11 , activebackground = "white" ,font=('century gothic', 10, ' bold '))
clearButton4.place(x=250, y=410)   
takeImg = tk.Button(frame2, text="Take Images", command=TakeImages  ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('century gothic', 15, ' bold '))
takeImg.place(x=30, y=320)
trainImg = tk.Button(frame2, text="Save Profile", command=psw ,fg="white"  ,bg="blue"  ,width=34  ,height=1, activebackground = "white" ,font=('century gothic', 15, ' bold '))
trainImg.place(x=30, y=380)
trackImg = tk.Button(frame1, text="Take Attendance", command=TrackImages  ,fg="black"  ,bg="yellow"  ,width=35  ,height=1, activebackground = "white" ,font=('century gothic', 15, ' bold '))
trackImg.place(x=30,y=50)
quitWindow = tk.Button(frame1, text="Quit", command=window.destroy  ,fg="black"  ,bg="red"  ,width=35 ,height=1, activebackground = "white" ,font=('century gothic', 15, ' bold '))
quitWindow.place(x=30, y=450)
report = tk.Button(frame1, text="Send Report", command=generateReport  ,fg="black"  ,bg="yellow"  ,width=11, activebackground = "white" ,font=('century gothic', 10, ' bold ' ))
report.place(x=340,y=410)

sendOTP = tk.Button(frame2, text="Verify", command=SendOTP ,fg="black"  ,bg="yellow"  ,width=8 , activebackground = "white" ,font=('century gothic', 10, ' bold '))
sendOTP.place(x=358, y=218)

##################### END ######################################

window.configure(menu=menubar)
window.mainloop()

####################################################################################################
