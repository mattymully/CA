#Importing datetime so when can check im expiry date has passed.
import datetime

#Incasing the entire code in a loop so it can be selected if they want to run again later on.
while True:

#Functions.
    def ConvertDateToDay(year,month,day):
        days = 0
        days = days + year * 365
        days = days + month * 30
        days = days + day
        return days

#Pulling the year, month and days.
    today = datetime.date.today()
    tyear = today.year
    tmonth = today.month
    tday = today.day

#Converting into days so we can compare it to expiry date.
    TDate = ConvertDateToDay(tyear,tmonth,tday)

#Inputs for name, postcode ,expirt date and card number.
    while True:
        name = input("----------------------------------------\nPlease enter name on card: ")
        if name.isnumeric():
            print("Please enter only letters")

        else:
            break
#Postcode input.
    pc = str(input("Please enter postcode: "))

#Expiry date input.
    while True:
        try:
            exp_year = int(input("Please enter year: "))
            exp_month = int(input("Please enter month: "))
            exp_day = int(input("Please enter day: "))
            break

        except ValueError:
            print("Please enter numbers only: ")

#Coverting the date into only days so when can compare it.
    days = ConvertDateToDay(exp_year, exp_month, exp_day)

#Card number input.
    while True:
        lyc_num = input("Please enter card number: ")

        if lyc_num.isalpha():
            print("Please enter only whole numbers only")

        if len(str(lyc_num)) != 8:
            print("Card must be 8 digits long")

        else:
            break

#Converting input to list and a new variable lyc_numL.
    lyc_numL = []
    for num in lyc_num:
        lyc_numL.append(int(num))

#Grabbing the check digit.
    check_digit = lyc_numL.pop()

#Revering the list and making a new variable lyc_numLR.
    lyc_numLR = lyc_numL[::-1]

#Creating list for multiplied 1,3,5 and 7 digits.
    lyc_numLRM = []
    lyc_numLRM.append(lyc_numLR[0] * 2)
    lyc_numLRM.append(lyc_numLR[1])
    lyc_numLRM.append(lyc_numLR[2] * 2)
    lyc_numLRM.append(lyc_numLR[3])
    lyc_numLRM.append(lyc_numLR[4] * 2)
    lyc_numLRM.append(lyc_numLR[5])
    lyc_numLRM.append(lyc_numLR[6] * 2)

#Checking if the new digit is over 9 if so removing 9.
    if lyc_numLRM[0] > 9:
        lyc_numLRM[0] = lyc_numLRM[0] - 9

    if lyc_numLRM[2] > 9:
        lyc_numLRM[2] = lyc_numLRM[2] - 9

    if lyc_numLRM[4] > 9:
        lyc_numLRM[4] = lyc_numLRM[4] - 9

    if lyc_numLRM[6] > 9:
        lyc_numLRM[6] = lyc_numLRM[6] - 9

#Adding the whole list up.
    added = 0
    for index in lyc_numLRM:
        added = added + index

#Adding the check digit.
    added = added + check_digit

#Checking if expired.
    expired = 0
    if days < TDate:
        expired = 1

#Outputting card.
    print("----------------------------------------")
    print("Name =",name)
    print("Postcode =",pc)
    print("Exp Date =",exp_day,"/",exp_month,"/",exp_year)
    print("Card Number =",lyc_num)
    print("----------------------------------------")

#Printing if expired or not.
    if expired == 1:
        print("Out of date")
    else:
        print("In date")

#Validating the card.
    if added % 10 == 0:
        print("Card number is valid")

    else:
        print("Card number is invalid")

    print("----------------------------------------")

#Selecting if they want to run the program today.
    try:
        Continue = int(input("Enter 1 to stop or any key to continue \n----------------------------------------\n"))
        #print("----------------------------------------")

        if Continue == 1:
            break

    except ValueError:
        continue
