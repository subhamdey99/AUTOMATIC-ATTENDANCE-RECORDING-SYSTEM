# import os


# print(os.getcwd())


# import datetime
# import csv
# weekday=0
# with open("TimeTable.csv", 'r') as tt:
#         weekday=datetime.datetime.today().weekday()
#         print('weekday: ',weekday)
#         reader1 = csv.reader(tt)
    
#         routine = list(reader1)
        

#         hr = datetime.datetime.now().hour

#         # if hr>=9 and hr<=12:
#         print('Hour: ',hr)
#         print('Routine header ',routine[0])
#         print('Current routine', routine[weekday+1])

#         col=0
#         # Finding the column index for that partitucar hour
#         for hour in routine[0]:
#             if hour.isdigit():
#                 if int(hour)==hr:
#                     print('Curruent hours: ',hr)
#                     print('Col: ',col)
#                     break
                
#             col += 1

#         subject = routine[weekday+1][col]
#         print(subject)
#         # else:
#         #     print('No class for this period')

# import datetime
# import time 
# import csv
# date = datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%Y')
#col_names = ['Id', 'Name', str(date)]
#col_names = ['id','Name','16-05-2022']

#col_names.append(date)
#print(col_names)
# print()
# print()

#import os
#print(os.getcwd())
# content=[]
# with open("..\Attendance\Attendance_05-2022_A_sub.csv") as f:
#     content = csv.reader(f)
#     content = list(content)
#     header = content[:1][0]
#     row = content[1:]
#     if str(date) not in header:
#         header.append(str(date))
#     print(header)
#     print(row)

# with open("..\Attendance\Attendance_05-2022_A_sub.csv",'w',newline='') as f:
#     w_obj = csv.writer(f)
#     w_obj.writerow(header)
#     w_obj.writerows(row)

# print()

# bb= 'CSB19202'
# ID='MILAN MANDAL'
# timestamp = '23:49:49'

# attendance = [ID, bb,str(timestamp)]

# header = []
# rows = []
# with open("..\Attendance\Attendance_05-2022_B_sub.csv") as f:
#     content = csv.reader(f)
#     content = list(content)
#     header = content[:1][0]
#     rows = content[1:]
#     print(header)
#     print(rows)
#     if not rows:
#         rows = attendance
#     for row in rows:
#         if row: 
#             print('----->',row[0])
#             if bb in row[0]:
#                 row.append(str(timestamp))
#                 break
            
# f.close()
# with open("..\Attendance\Attendance_05-2022_B_sub.csv",'w', newline='') as f:
#     w_obj = csv.writer(f)
#     w_obj.writerow(header)
#     w_obj.writerows(rows)
# f.close()


#mail system
# import csv
# import time
# import datetime
# import os
# import smtplib
# a = os.listdir('../Attendance')
# #print(a)
# b = "CSB19202"
# b = "'"+b+"'"
# d = "CSB19202"
# flag = 0
# attendance=[]
# name =""
# ts = time.time()
# date = datetime.datetime.fromtimestamp(ts).strftime('%m-%Y')
# # Calculate Attendance
# for file in a:
#     with open("../Attendance/"+file,'r', newline='', encoding='utf-8') as f:
#         content = list(csv.reader(f))
#         c = len(content[0])-2
#         filename = file.split('.')
#         filename = filename[0]
#         #print(c)
#         for row in content:
#             if row:
#                 #print(row)
#                 if row[0]==b:
#                     flag+=1
#                     count = -2
#                     for item in row:
#                         #print(item)
#                         if item:
#                             count+=1
#                     per = count/c*100
#                     per = "{:.2f}".format(per)
#                     msg = 'Your Attendance Percentage in '
#                     msg = msg+filename+" "
#                     msg = msg+str(per)+'%'
#                     attendance.append(msg)
#                     print(attendance)
#         if flag == 0:
#             msg = 'Your Attendance Percentage in '
#             msg = msg+filename+" "
#             msg = msg+str(0)+'%'
#             attendance.append(msg)
#     f.close()

# # Find Email
# with open("../StudentDetails/StudentDetails.csv",'r', newline='', encoding='utf-8') as f:
#     content = list(csv.reader(f))
#     flag = 0
#     for row in content:
#             if row:
#                 #print(row)
#                 if row[2]==d:
#                     name = row[4]
#                     reciever = row[6]
#                     flag+=1
#                     #print(reciever)
#                     break
#     if flag==0:
#         #mess._show(title='Email Error', message='Your Email is not registered')
#         print("Your Email is not registered")
# f.close()

# #print(attendance)

# port =587
# smtp_server = "smtp.gmail.com"
# sender_email = "subhamdey297@gmail.com"
# receiver_email = reciever
# #print(receiver_email)
# password = "dfogajpksrepwxii"
# message = """\
# Subject: Attendance Report
# Hi {} your attendance for the month of {} given below
# """.format(name,date)
# for i in range(len(attendance)):
#     #print(i)
#     message = message + "\n" + attendance[i] + "\n"
# print(message)
# server = smtplib.SMTP(smtp_server, port)
# server.starttls()
# server.login(sender_email, password)
# server.sendmail(sender_email, receiver_email, message)
# server.quit()



# from random import randint
# from pymongo import MongoClient
# import datetime
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# client=MongoClient()
# client = MongoClient("mongodb://localhost:27017/")
# mydatabase = client['project']
# otpcollection=mydatabase['otp']

# email = "mandalmilan356@gmail.com"

# otp = randint(000000,999999)
# timestamp = datetime.datetime.utcnow()
# data = {}
# data['email'] = email
# data['otp'] = otp
# mydatabase.otpcollection.create_index( "DateTime" ,expireAfterSeconds =120)
# mydatabase.otpcollection.insert_one({"OTP":otp,"DateTime": timestamp, "Email": email})

# html = '''
#     <html>
#         <body>
#             <h1>Your OTP for Automatic Attendance Recording System is {}</h1>
#             <h1>This code will expire in 2 minutes</h1>
#         </body>
#     </html>
#     '''.format(otp)



# port =587
# smtp_server = "smtp.gmail.com"
# sender_email = "subhamdey297@gmail.com"
# receiver_email = email

# password = "dfogajpksrepwxii"


# email_message = MIMEMultipart()
# email_message['From'] = sender_email
# email_message['To'] = receiver_email
# email_message['Subject'] = "Email Verification OTP"
# email_message.attach(MIMEText(html, "html"))
# email_string = email_message.as_string()
# print(email_string)

# server = smtplib.SMTP(smtp_server, port)
# server.starttls()
# server.login(sender_email, password)
# server.sendmail(sender_email, receiver_email, email_string)
# server.quit()
import os
import csv

CEmail = "zzzz"
exists8 = os.path.exists("../VerifiedEmails/Emails.csv")
if exists8:
    with open("../VerifiedEmails/Emails.csv", 'r') as ab:
        lst = csv.reader(ab)
        #lst = list(lst)
        for each in lst:
            print(each)
            if each[0] == CEmail:
                print(each[0])
                break