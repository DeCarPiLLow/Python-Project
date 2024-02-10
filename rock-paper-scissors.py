import random
import math

def computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def player_choice():
    choices = ["rock", "paper", "scissors"]
    player = None
    
    while player not in choices:
        player = input("ROCK-PAPER-SCISSORS: ").lower()
    else:
        return player 

choice = "y"
while choice == "y":
    plc = player_choice()
    cpc = computer_choice()

    if plc == cpc:
        print("Lets GO AGAIN!!")
        choice = "y"
    elif plc == "rock":
        if cpc == "paper":
            print("You Got WRAPPED!!")
            choice = input("Wanna go again?(y/n): ").lower()
        else:
            print("You BROKE into Pieces!!")
            choice = input("Wanna go again?(y/n): ").lower()
        print("\n")
    elif plc == "paper":
        if cpc == "scissors":
            print("You were CUT to Pieces!!")
            choice = input("Wanna go again?(y/n): ").lower()
        else:
            print("You WRAPPED It!!")
            choice = input("Wanna go again?(y/n): ").lower()
        print("\n")
    elif plc == "scissors":
        if cpc == "rock":
            print("You BROKE to Pieces!!")
            choice = input("Wanna go again?(y/n): ").lower()
        else:
            print("You CUT it to Pieces!!")
            choice = input("Wanna go again?(y/n): ").lower()
        print("\n")
    



