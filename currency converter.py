print ("Welcome to currency converter")
start=input("Start or Quit?")    
currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
money=int(input("How much money you want to change?"))
cash=0.05*money
check=0.01*money

while (start!="Quit") and (start=="Start"):
    """for converting US to CD"""
    if (currency1=="US") and (currency2=="CD"):
        print ("Converting from : US dollars")
        print (str(money)+ " US Dollars")
        money=money*1.26
        if (money<=0):
            print("Invalid numbers")
            start=input("Start again or Quit?")    
            currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
            currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
            money=int(input("How much money you want to change?"))
            print (money)
        else:
            print ("Your money is $"+str(round(money))+ " in CD")
            change=input("what form of transcation you want to use? (cash/check)")
            while (change!="check") and (change!="cash"):
                print ("we dont accept that form of transaction")
                change=input("what form of transcation you want to use? (cash/check)")
            if change=="cash":
                print ("your fee is "+str(round(money*0.05, 2)))
                print (currency2)
            elif change=="check":
                print ("your fee is "+str(round(money*0.01, 2)))
                print (currency2)
            start=input("Start again or Quit?")    
            currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
            currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
            money=int(input("How much money you want to change?"))
            print (money)

    elif (currency1=="US") and (currency2=="Euro"):
        """for converting US to Euro"""
        print ("Converting from : US dollars")
        print (str(money)+ " US Dollars")
        money=money*0.78
        if (money<=0):
            print("Invalid numbers")
            start=input("Start again or Quit?")    
            currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
            currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
            money=int(input("How much money you want to change?"))
            print (money)
        else:
            print ("Your money is "+str(round(money))+" Euros")
            change=input("what form of transcation you want to use? (cash/check)")
            while (change!="check") and (change!="cash"):
                print ("we dont accept that form of transaction")
                change=input("what form of transcation you want to use? (cash/check)")
            if change=="cash":
                print ("your fee is "+str(round(money*0.05, 2)))
                print (currency2)
            elif change=="check":
                print ("your fee is "+str(round(money*0.01, 2)))
                print (currency2)
            start=input("Start again or Quit?")    
            currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
            currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
            money=int(input("How much money you want to change?"))
            print (money)

    elif (currency1=="Euro") and (currency2=="CD"):
        """for converting Euro to CD"""
        print ("Converting from : US dollars")
        print (str(money)+ " US Dollars")
        money=money*1.46
        if (money<=0):
            print("Invalid numbers")
            start=input("Start again or Quit?")    
            currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
            currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
            money=int(input("How much money you want to change?"))
            print (money)
        elif change=="check":
            print ("Your money is "+str(round(money))+" Euros")
            change=input("what form of transcation you want to use? (cash/check)")
            while (change!="check") and (change!="cash"):
                print ("we dont accept that form of transaction")
                change=input("what form of transcation you want to use? (cash/check)")
            if change=="cash":
                print ("your fee is "+str(round(money*0.05, 2)))
                print (currency2)
            elif change=="check":
                print ("your fee is "+str(round(money*0.01, 2)))
                print (currency2)
            start=input("Start again or Quit?")    
            currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
            currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
            money=int(input("How much money you want to change?"))
            print (money)


    elif (currency1=="Euro") and (currency2=="US"):
        """for converting Euro to US"""
        print ("Converting from : US dollars")
        print (str(money)+ " US Dollars")
        print ("You are converting from " + str(money)+ " Euros")
        money=money*1.13
        if (money<=0):
            print("Invalid numbers")
            start=input("Start again or Quit?")    
            currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
            currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
            money=int(input("How much money you want to change?"))
            print (money)
        else:
            print ("Your money is "+str(round(money))+" Euros")
            change=input("what form of transcation you want to use? (cash/check)")
            while (change!="check") and (change!="cash"):
                print ("we dont accept that form of transaction")
                change=input("what form of transcation you want to use? (cash/check)")
            if change=="cash":
                print ("your fee is "+str(round(money*0.05, 2)))
                print (currency2)
            elif change=="check":
                print ("your fee is "+str(round(money*0.01, 2)))
                print (currency2)
            start=input("Start again or Quit?")    
            currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
            currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
            money=int(input("How much money you want to change?"))
            print (money)



    elif (currency1=="CD") and (currency2=="Euro"):
        """for converting CD to Euro"""
        print ("Converting from : US dollars")
        print (str(money)+ " US Dollars")
        print ("You are converting from " + str(money)+ " CD dollars")
        money=money*0.69
        if (money<=0):
            print("Invalid numbers")
            start=input("Start again or Quit?")    
            currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
            currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
            money=int(input("How much money you want to change?"))
            print (money)
        else:
            print ("Your money is "+str(round(money))+" Euros")
            change=input("what form of transcation you want to use? (cash/check)")
            while (change!="check") and (change!="cash"):
                print ("we dont accept that form of transaction")
                change=input("what form of transcation you want to use? (cash/check)")
            if change=="cash":
                print ("your fee is "+str(round(money*0.05, 2)))
                print (currency2)
            elif change=="check":
                print ("your fee is "+str(round(money*0.01, 2)))
                print (currency2)
            start=input("Start again or Quit?")    
            currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
            currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
            money=int(input("How much money you want to change?"))
            print (money)


    elif (currency1=="CD") and (currency2=="US"):
        """for converting CD to US"""
        print ("Converting from : US dollars")
        print (str(money)+ " US Dollars")
        print ("You are converting from " + str(money)+ " CD dollars")
        money=money/1.29
        if (money<=0):
            print("Invalid numbers")
            start=input("Start again or Quit?")    
            currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
            currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
            money=int(input("How much money you want to change?"))
            print (money)
        else:
            print ("Your money is "+str(round(money))+" Euros")
            change=input("what form of transcation you want to use? (cash/check)")
            while (change!="check") and (change!="cash"):
                print ("we dont accept that form of transaction")
                change=input("what form of transcation you want to use? (cash/check)")
            if change=="cash":
                print ("your fee is "+str(round(money*0.05, 2)))
                print (currency2)
            elif change=="check":
                print ("your fee is "+str(round(money*0.01, 2)))
                print (currency2)
            start=input("Start again or Quit?")    
            currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
            currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
            money=int(input("How much money you want to change?"))
            print (money)

    elif (currency1=="US") and (currency2=="US"):
        print ("This type of conversion cant takeplace")
        start=input("Start again or Quit?")    
        currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
        currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
        money=int(input("How much money you want to change?"))
        print (money)

    elif (currency1=="CD") and (currency2=="CD"):
        print ("This type of conversion cant takeplace")
        start=input("Start again or Quit?")    
        currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
        currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
        money=int(input("How much money you want to change?"))
        print (money)

    elif (currency1=="Euro") and (currency2=="Euro"):
        print ("This type of conversion cant takeplace")
        start=input("Start again or Quit?")    
        currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
        currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
        print (money)

    else:
        print (" We dont accept any currencies ohter than US, euros, or CD")
        start=input("Start again or Quit?")    
        currency1=input("Enter the currency you want to change from (US/CD/Euro)= ")
        currency2=input("Enter the currency you want to change to (US/CD/Euro)= ")
        money=int(input("How much money you want to change?"))
        print (money)



