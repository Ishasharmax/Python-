#This is an ATM

"""
# Hangman.py
# Author: Isha Sharma
# October 20, 2017
"""

print ("welcome to the ATM!")

yesOrNo=input("Do you want to log in?(True or False)")

while (yesOrNo!="False"):
    
    balance=100
    username=input ("Enter your username:")
    while (username!="Ishasharma"):
        print ("You entered a wrong username")
        username=input ("Enter your username:")
        
    password=input("Enter your password: ")
    while (password!="1234"):
        print ("You entered a wrong password")
        password=input("Enter your password: ")

    print ("you are now logged in")
    choose=input("You can now choose between withdraw, deposit, balance, or log out: ")
    while (choose!="log out"):
        choose=input("You can now choose between withdraw, deposit, balance, or log out: ")
        if (choose=="withdraw"):
            withdraw=input("Enter the amount of money you want to withdraw: ")
            balance=balance-int(withdraw)
        elif (choose=="balance"):
            print ("your balance is $"+str(balance))
        elif (choose=="deposit"):
            deposit=int(input("enter a amount you want to deposit: "))
            balance=balance+deposit
    print ("You are logged out of the system")
    yesOrNo=input("Do you want to log in again?(True or False)")
