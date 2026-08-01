'''
Step 1--> Setting up gmail app password (2 step verification ON)
We will use SMTP (Simple Mail Transfer protocol)
#Step 2 --> USing smtp library we start the communication
'''

import smtplib
#First we will make the protocol connection
server = smtplib.SMTP('smtp.gmail.com', 587)
print(server)

#Start communication
server.starttls()
#we will make the login
server.login('pavanipranathiballa@gmail.com','njzo nmwg plqf fbjv')

message = "Yk, u r kusogaki rgt (An automated mail u baaka)"
#Send the mail
server.sendmail('abc@gmail.com','bhuvan_kethineni@srmap.edu.in', message)
print("Success")
