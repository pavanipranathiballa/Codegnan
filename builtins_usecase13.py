'''
Use Random module -->Rock, Paperm Scissors


import random
player1 = input('Enter the coice : -->Rock,Paper,Scissors: ').lower()
player2 = random.choice(['Rock', 'Paper','Scissors']).lower()
print("player2 Selection:",player2)

if player1 == "rock" and player2 == "scissors":
    print("Player1 wins")

elif player1 == "rock" and player2 == "paper":
    print("Player2 wins")

elif player1 == "rock" and player2 == "rock":
    print("It's a tie")

elif player1 == "paper" and player2 == "scissors":
    print("Player2 wins")

elif player1 == "paper" and player2 == "paper":
    print("It's a tie")

elif player1 == "paper" and player2 == "rock":
    print("Player1 wins")

elif player1 == "scissors" and player2 == "scissors":
    print("It's a tie")

elif player1 == "scissors" and player2 == "paper":
    print("Player1 wins")

elif player1 == "scissors" and player2 == "rock":
    print("Player2 wins")


#Task --> Build a Game generator sequences -->Choice Menu
#1 - Rock, Paper, Scissors Game
#2 - Story Generator (random.choice()) --> when, where, what, how, who create these list
#3 - OTP Generate to Email
#4 - BMI Calci



#Build our own QR Code --> pyqrcode (python qr code)
import pyqrcode, png

link = "https://www.instagram.com/p2___pvt/"
qr = pyqrcode.create(link)
print(qr)
qr.png("myqr.png", scale = 15)
'''

"""
"""
'''
start = int(input())
end = int(input())

num = start
while num <= end:
    temp = num
    digits = 0
    
    while temp != 0:
        digits = digits + 1
        temp = temp // 10
    
    temp = num
    total = 0
    
    while temp != 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10
    
    if total == num:
        print(num, end=" ")
    
    num = num + 1
'''
"""
import math,random
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def rockpaperscissor():
    player1 = input("Enter your choice: ")
    player2 = random.choice(['Rock', 'Paper','Scissors']).lower()
    print("Player2 chooses: ",player2)
    if player1 == "rock" and player2 == "scissors":
        return("Player1 wins")

    elif player1 == "rock" and player2 == "paper":
        return("Player2 wins")

    elif player1 == "rock" and player2 == "rock":
        return("It's a tie")

    elif player1 == "paper" and player2 == "scissors":
        return("Player2 wins")

    elif player1 == "paper" and player2 == "paper":
        return("It's a tie")

    elif player1 == "paper" and player2 == "rock":
        return("Player1 wins")

    elif player1 == "scissors" and player2 == "scissors":
        return("It's a tie")

    elif player1 == "scissors" and player2 == "paper":
        return("Player1 wins")

    elif player1 == "scissors" and player2 == "rock":
        return("Player2 wins")


def story():
    when = random.choice(['Once upon a time',
                          'At one very fine afternoon',
                          'Today, in the morning']).lower()
    where = random.choice(['In the forest',
                           'At garden',
                           'At the street']).lower()
    what = random.choice(['Met the old friend',
                          'Have seen a cute lil pet',
                          'Thought of shopping']).lower()
    then = random.choice(['Had a great time']).lower()

    return(f'{when} {where} {what} {then}')

def email():
    From = 'pavanipranathiballa@gmail.com'
    To = 'pavanipranathi21@gmail.com'
    Subject = 'Ur OTP'
    msg = MIMEMultipart()
    msg['From'] = From
    msg['To'] = To
    msg['Subject'] = Subject
    OTP = random.randint(1000,9999)
    body = f'Your OTP  is {OTP}'
    msg.attach(MIMEText(body))
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('pavanipranathiballa@gmail.com', 'njzo nmwg plqf fbjv')
    server.sendmail(From, To, body)
    a = int(input("Enter the otp received: "))
    if a == OTP:
        return("Login Success")
    else:
        return("Enter the correct OTP")

def bmicalci():
    while True:
        try:
            weight = int(input("Enter the weight: "))
            height = float(input("Enter the height: "))
            bmi = (weight)/((height) ** 2)
            if weight < 0 and height < 0:
                print(f'Enter only +ve numbers')
            break
        except ValueError:
            print(f'Enter weight in int and height in float')
        except ZeroDivisionError:
            print(f'Both zeros are not allowed')

    if bmi < 18.5:
        return(f'Underweight and bmi is {bmi}')
    elif 18.5 <= bmi < 24.9:
        return(f'Normal weight and bmi is {bmi}')
    elif 25 <= bmi < 29:
        return(f'overweight and bmi is {bmi}')
    else:
        return(f'Obesity and bmi is {bmi}')

def choicechooser():
    while True:
        print("1. Rock, Paper, Scissors")
        print("2. Story Teller")
        print("3. OTP Generator")
        print("4. BMI calci")
        print("5. Exit")

        choice = int(input("Enter ur choice: "))

        if choice == 1:
            #player1 = input("Enter your choice: ")
            print(rockpaperscissor())
            print('\n')

        elif choice == 2:
            print(story())
            print('\n')
        elif choice == 3:
            print(email())
            print('\n')
        elif choice == 4:
            print(bmicalci())
            print('\n')
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Enter only valid ooptions")
choicechooser()
"""

import random
from datetime import datetime,timedelta
print("Welcome to MovieMate AI!")
print("\n")
name = input("Enter your name: ")
print("\n")
print("Choose Genre: ")
print("1. Action")
print("2. Comedy")
print("3. Horror")

genre_choice = input("Enter your choice: ")
if genre_choice == "1":
    genre = "Action"
    movies = ["Leo", "Vikram", "Jailer"]

elif genre_choice == "2":
    genre = "Comedy"
    movies = ["MAD", "DJ Tillu", "The Sheep Detective"]

elif genre_choice == "3":
    genre = "Horror"
    movies = ["Obsession", "Insidious", "Sinister"]
else:
    print("Enter from the above choices")

print("Available Movies: ")
print("1. ", movies[0])
print("2. ", movies[1])
print("3. ", movies[2])
movie_choice = input("Enter your movie choice: ")
if movie_choice == "1":
    movie_choosen = movies[0]
elif movie_choice == "2":
    movie_choosen = movies[1]
elif movie_choice == "3":
    movie_choosen = movies[2]
else:
    print("Enter from the above choices")

show_times = ["10:00 AM", "1:00 PM", "6:00 PM", "7:00 PM", "10:00 PM"]
show_time = random.choice(show_times)

book_date = datetime.now()
booking_date = book_date.strftime("%d-%m-%Y")


print("Booking Confirmed!")
print("\n")
print("Customer: ", name)
print("Movie: ", movie_choosen)
print("Show time: ", show_time)
print("Booking date: ", booking_date)
print("\n")
print("Enjoy your movie!")
