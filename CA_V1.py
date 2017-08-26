#GITHUB master
#Importing datetime so when can check im expiry date has passed.
from datetime import datetime
import os
#Incasing the entire code in a loop so it can be selected if they want to run again later on.
while True:
#Getting current date
    cdate = datetime.today()
#Inputs for name, postcode ,expirt date and card number.
    os.system('CLS')
    while True:
        name = input("Please enter first and last name on card: ")
        if name.isnumeric():
            print("Please enter only letters")
        elif len(name.split()) != 2:
            print("please enter exactly 2 names")
        else:
            break
#Postcode input.
    os.system('CLS')
    pc = str(input("Please enter postcode: "))
#Expiry date input.
    os.system('CLS')
    while True:
        try:
            idate = input("Please enter date in format day/month/year, eg 24/5/2019: ")
            idate = datetime.strptime(idate, "%d/%m/%Y")
            break
        except ValueError:
            print("Please make sure you have enterd date correctly.")
#Card number input.
    os.system('CLS')
    while True:
        try:
            lyc_num = int(input("Please enter card number: "))
            if len(str(lyc_num)) != 8:
                print("Card must be 8 digits long")
            else:
                break
        except ValueError:
            print("Please enter only whole numbers.")
#Converting input to list and a new variable lyc_numL.
    lyc_numL = []
    for num in str(lyc_num):
        lyc_numL.append(int(num))

#Grabbing the check digit.
    check_digit = lyc_numL.pop()
#Revering the list and making a new variable lyc_numLR.
    lyc_numLR = lyc_numL[::-1]
#Creating list for multiplied 1,3,5 and 7 digits.
    lyc_numLRM = []
    for i in range(len(lyc_numLR)):
        if i % 2 == 0:
            lyc_numLRM.append(lyc_numLR[i] * 2)
        else:
            lyc_numLRM.append(lyc_numLR[i])
#Checking if the new digit is over 9 if so removing 9.
    for i in range(len(lyc_numLRM)):
        if lyc_numLRM[i] > 9:
            lyc_numLRM[i] = lyc_numLRM[i] - 9
#Adding the whole list up.
    added = 0
    for index in lyc_numLRM:
        added = added + index
#Adding the check digit.
    added = added + check_digit
#Outputting card.
    os.system('CLS')
    print("----------------------------------------")
    print("--Name =",name)
    print("--Postcode =",pc)
    print("--Exp Date =",datetime.strftime(idate, "%d/%m/%Y"))
    print("--Card Number =",lyc_num)
    print("----------------------------------------")
#Printing if expired or not.
    if cdate > idate:
        print("--Card out of date!")
    else:
        print("--Card in date")
        print("----------------------------------------")
#Validating the card.
    if added % 10 == 0:
        print("--Card number is valid")
    else:
        print("--Card number is invalid!")
    print("----------------------------------------")
#Selecting if they want to run the program again.
    try:
        Continue = int(input("Enter 1 to stop or any key to continue \n----------------------------------------\n"))
        if Continue == 1:
            break
    except ValueError:
        continue
