"""
# Hangman.py
# Author: Isha Sharma
# November 20, 2017
"""

from random import *

def word():
    """This function returns a random word from a list of words
       args:none
       returns: a random word"""

    ListOfWords=["fast","car","cat","dog","computer"]   #ListOfWords is a list of random words 
    randomWord=randint(0,len(ListOfWords))              #randomWord chooses one of tha random words from ListOfWords
    randomWord=ListOfWords[randomWord]
    randomWordFromList=randomWord
    return randomWordFromList                           #randomWordFromList is the random word

def hangman(wordSelected,letter):
    """This function takes two arguments and returns if the player has won or lost.
    This function also print out which body part has been drawn. This function is the play function.
    args: a random word selected, the letter input by the player
    returns: none"""
    lengthOfTheWord=len(list(wordSelected))                 #lengthOfTheWord is the length of the word in numerical value.
    guessWord="_"*lengthOfTheWord                           #guessWord is the number of dashes according to the random word.
    guessWord=list(guessWord)
    chances=0                                               #chances is to keep the track of the wrong guesses.
    boolean=True
    while chances<6 and boolean:                            #This while loop is to keep the track of the wrong guesses and if the letter is in the selected word or not.
        for x in range(len(wordSelected)):                  #this for loop is to check the letters in the random word
            if wordSelected[x] == letter:                   #this if statement is to check if the letter input by the user is in the random word
                guessWord[x]=letter
                dash="_"
                print (str(guessWord))
                if dash not in guessWord:               #this if statement is to check if anymore dashes are there in the word which is supposed to be guessed.
                    print ("You  win!")
                    boolean=False
                else:
                    letter=input("Guess a letter: ")
        if letter not in  wordSelected:
            bodyParts=["head","body", "left arm", "right arm", "left leg", "right leg"]     #this list is to tell the body parts, which are used in the hangman game
            if chances==0:
                drawn=bodyParts[0]
            if chances==1:
                drawn=bodyParts[1]
            if chances==2:
                drawn=bodyParts[2]
            if chances==3:
                drawn=bodyParts[3]
            if chances==4:
                drawn=bodyParts[4]
            if chances==5:
                drawn=bodyParts[5]
            chances+=1
            print(guessWord)
            print ("draw body part: "+ str(drawn))                   #starting from the head to the right leg, body parts are drawn if the user guesses wrong letter for the random word.
            letter=input("Guess a letter: ")
    if chances==6:                                                    #only 6 wrong chnaces are given to the user, after that the correct word is shown.
        print ("You are hanged! The word was "+ wordSelected)

def main():    
    print ("Welcome to the game of Hangman. Here is your word: ")
    wordSelected=word()                                #this is to call the word function, which will return the random word
    lenghtOfWord=len(wordSelected)
    dashes="_"*lenghtOfWord
    print (dashes)                                      #this tells the user about the length of the random word
    letter=input("Guess a letter: ")                    #this input statement is to input the letter user will guess
    play=hangman(wordSelected,letter)                   #this is to call the hangman function, where all the game will happen                  
    print (play)
main()
