#While
'''
count = 0
while count < 5:
    print("Satisfies")
    a =[]
    a.append("PP")
    print(a)
    count += 1



count = 5
while count > 0:
    print(f' Count = {count}')
    count -= 1


#To find a valid password



attempt = 0
while attempt > 3:
    password = input("Enter pass: ")
    if password = "admin":
        print(f' Success')
    else:
        password = input("Enter again: ")


password = input("Enter pass: ")
while password != "admin":
    print("Incorrect")
    password = input("Enter again: ")
print("Success")


attempt = 0
password = input("Enter password: ")
while attempt < 3:
    if password == "admin":
        print("Success")
        break
    else:
        password = input("Enter again: ")
        attempt += 1
else:
    print("Locked")


#for with else, while with else --> else will be executed only when loop is completely done
#search for a product in the store

product = input("Enter the product: ")
store = ["Apple", "Mango"]
for item in store:
    if product  == item:
        print("Found")
        break
else:
    print("Not found")

'''

#Task: OTP Verification user should be given 3 chances if 3rd chance is over it shuld return account blocked for 24hrs --->
#case study: card is inserted if inserted card is correct enter otp and otp should be verified within 3 attempts else card is not inserted. after attempt is correct want to withdraw the amount and after withdrawing the new balance 



#break, continue, pass --> jumpig statement
#break --> it terminates the loop once the given condition is satisfied

#continue --> it basically skips the current iteration and gets back back to the next iteration
'''

for i in "codegnan":
    if i == "g":
        #break --> it breaks at g
        continue  # this skips g and go to next iteration
        #pass --> placeholder (to have any syntax matches)
    print(i, end ="")





units = int(input("Enter the units: "))
age = int(input("Enter age: "))

if age < 50:
    if units >= 0 and units <= 100:
        Rate_per = units * 1.5
    elif units >= 101 and units <= 200:
        Rate_per = units * 2.5
    elif units >= 201 and units <= 500:
        Rate_per = units * 4
    elif units > 500 and units <= 800:
        Rate_per = units * 6
    else:
        Amount = units * 6
        Rate_per = Amount * (5/100) + Amount
    print(f' {Rate_per}')

else:
    Rate_per *= 0.9
    print(f' {Rate_per}')
'''
    
'''
units = int(input("Enter the units: "))
age = input("Enter age: ")
if units >= 0 and units < 100:
    print(f' Rate per unit is 1.5 rupees')
    if age > 50:
        Rate_per = 1.5 - (1.5 * 10%)
        print(f' {Rate_per}')


units = int(input("Enter the units: "))
senior = input("Enter senior or not: ").lower() == "senior"

if units >= 0 and units <= 100:
    Rate_per = units * 1.5
elif units >= 101 and units <= 200:
    Rate_per = units * 2.5
elif units >= 201 and units <= 500:
    Rate_per = units * 4
elif units > 500 and units <= 800:
    Rate_per = units * 6
else:
    Rate_per = units * 6 * 1.05

if senior:
    Rate_per *= 0.9
print(Rate_per)
'''


#task:
correct_pin = "1234"
card_inserted = False
balance = 19500

if card_inserted:
    attempt = 0
    while attempt < 3:
        otp = input("Enter otp: ")
        if otp == correct_pin:
            print("Success")
            budget = int(input("Want to spend: "))
            if balance > budget:
                if budget > 500:
                    if budget >= 10000:
                        print("Plan: can go to trip")
                        New_Balance = balance- budget
                        print(f'New_Balance = {New_Balance}')
                        budget2 = int(input("Want to spend more: "))
                        if budget2 == 0:
                            print(f'Ok Thank You')
                        elif New_Balance > budget2:
                            if budget2 >= 5000:
                                print(f'Plan: Resort stay')
                                New_Balance2 = New_Balance - budget2
                                print(f'New_Balance = {New_Balance2}')
                                budget3 = int(input("Want to spend again: "))
                                if budget3 == 0:
                                    print(f'Ok Thank You')
                                elif New_Balance2 > budget3:
                                    if budget3 >= 3000:
                                        print(f'Plan: Movie and Dinner')
                                        New_Balance3 = New_Balance2 - budget3
                                        print(f'New_Balance2 = {New_Balance3}')
                                        budget4 = int(input("Want to spend again: "))
                                        if budget4 == 0:
                                            print(f'Ok Thank You')
                                        elif New_Balance3 > budget4:
                                            if budget4 >= 1000:
                                                print(f'Plan: Cafe and Shopping')
                                                New_Balance4 = New_Balance3 - budget4
                                                print(f'New_Balance3 = {New_Balance4}')
                                                budget5 = int(input("Want to spend again: "))
                                                if budget5 == 0:
                                                    print(f'Ok Thank You')
                                                elif New_Balance4 > budget5:
                                                    if budget5 >= 500:
                                                        print(f'Plan: Street Food and Part Visit')
                                                        New_Balance5 = New_Balance4 - budget5
                                                        print(f'New_Balance4 = {New_Balance5}')
                                                else:
                                                    print("Insufficient Balance and Stay Home")
                                        else:
                                            print("Insufficient Balance and Stay Home")
                                else:
                                    print("Insufficient Balance and Stay Home")
                        else:
                            print("Insufficient Balance and Stay Home")
                else:
                    print(f'Stay Home')
            else:
                print("insufficient balance and Stay Home")
            break
        else:
            print("OTP is incorrect")
            attempt += 1
    else:
        print("Account blocked for 24hrs")
else:
    print("Card is not inserted")
