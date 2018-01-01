total=0
loopCount=0
userInput=input("Please enter a number: ")
while(userInput!="done"):
    print (userInput)
    userInput=float(userInput)
    total=(total)+(userInput)
    loopCount=(loopCount)+1
    userInput=input("Please enter a number or done to finish: ")
end=total/loopCount
print (end)
    
