#######################################################
#
# COSC 140 Homework 3: ghost
#
#######################################################

import random
import time

def load_wordlist():
    '''
    Function written for you that reads contents of words.txt and 
    returns a list of words, each word in uppercase.
    '''
    wordlist = []
    with open("words.txt") as infile:
        for line in infile:
            wordlist.append(line.strip().upper())
    return wordlist


def getLetter(playerNumber, robotInTurn):
    isValid = False
    while(not(isValid)):
        if not robotInTurn:
            letter = input("Player " + str(playerNumber) + ", how about a letter: ")
        else:
            time.sleep(1)
            letters = "ABCDEFGHIJKLMNOPQRZTUVWXYZ"
            letter = letters[random.randint(0, len(letters)-1)] # randomly choose a letter
        
        if ((not letter.isalpha()) or len(letter) > 1):
            print("Please only enter one letter")
        else:
            isValid = True
    return letter.capitalize()


def checkFrag(fragment, wordList):
    canBeWord = False
    for word in wordList:
        if fragment.startswith(word):
            if len(fragment) > 3 and len(word) > 3: #only check validity if over size 3
                return True
        if word.startswith(fragment):
            canBeWord = True
    if not canBeWord:
        return True #the fragment cannot make any valid word
    return False


def main():
    words = load_wordlist()
    print(f"{len(words)} words loaded.")
    fragment = ""
    didLose = False
    playerNumber = 1
    robot = False
    robotInTurn = False


    ai = input("Would you like to play against a robot? ")
    if ai.lower() == "yes":
        print("Robot mode activated!")
        robot = True


    while(not didLose):
        letter = getLetter(playerNumber, robotInTurn)
        fragment += letter
        if not robotInTurn:
            print("Player " + str(playerNumber) + " chose " + letter + ", giving fragment " + fragment + ".")
        else:
            print("Robot chose " + letter + ", giving fragment " + fragment + ".")

        if (checkFrag(fragment, words)):
            print("Player " + str(playerNumber) + " just lost.")
            didLose = True
        if playerNumber == 2:
            playerNumber = 0
        playerNumber +=1
        if robot:
            if robotInTurn:
                robotInTurn = False
            else:
                robotInTurn = True


if __name__ == "__main__":
    main()
