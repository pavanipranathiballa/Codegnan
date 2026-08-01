#Now in this case we will use email package where we can add subject to the mail and also
#We can give "TO" address...
'''
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#give from address, to address and subject
From = 'pavanipranathiballa@gmail.com'
To = 'bhuvan_kethineni@srmap.edu.in'
Subject = 'Okotte imasu'

msg = MIMEMultipart()
msg['From'] = From
msg['To'] = To
msg['Subject'] = Subject

body = 'Daikirai da'
msg.attach(MIMEText(body))
#Entire mssg to string format
text = msg.as_string()
#same as previous SMTP usage we will follow
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('pavanipranathiballa@gmail.com','njzo nmwg plqf fbjv')
server.sendmail(From, To, text)
print("Mail Sent")
server.quit()
'''
#Send an OTP to user and validated

import smtplib
import email
import math,random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#give from address, to address and subject
From = 'pavanipranathiballa@gmail.com'
To = 'bhuvan_kethineni@srmap.edu.in'
Subject = 'Ur OTP'

msg = MIMEMultipart()
msg['From'] = From
msg['To'] = To
msg['Subject'] = Subject

OTP = random.randint(1000, 9999)

body = f'Your OTP is {OTP}'

msg.attach(MIMEText(body))
#Entire mssg to string format
text = msg.as_string()
#same as previous SMTP usage we will follow
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('pavanipranathiballa@gmail.com','njzo nmwg plqf fbjv')
server.sendmail(From, To, body)
a = input("Enter the OTP received: ")
if a == OTP:
    print(f'Login Success')
else:
    print(f'Login failed')


'''
From = 'pavanipranathiballa@gmail.com'
To = 'bhuvan_kethineni@srmap.edu.in'
Subject = 'Ur OTP'
msg = MIMEMultipart()
msg['From'] = From
msg['To'] = To
msg['Subject'] = Subject

digits = '0123456789'
OTP = ""
for i in range(4):
    OTP += digits[math.floor(random.random() * 10)]
body = 'Your OTP is' + OTP
msg.attach(MIMEText(body))
#Entire mssg to string format
text = msg.as_string()
#same as previous SMTP usage we will follow
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('pavanipranathiballa@gmail.com','njzo nmwg plqf fbjv')
server.sendmail(From, To, text)
a = input("Enter the OTP received: ")
if a == OTP:
    print(f'Login Success')
else:
    print(f'Login failed')
'''
