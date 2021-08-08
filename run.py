import time
import random

# Answers to yes or no questions
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# Rock, Paper, Scissors variables
user_score = int()
duck_score = int()
final_score = 3


# Intro
print("Guess who's back?")

print("...")
time.sleep(2)
print("It's White Duck!")
time.sleep(3)
print("...")
time.sleep(1)

# Instructions

# Start

silly_names = ["Bibo Holiday!", "Catacata Plum!", "Carrot Bunch III!", "Pot Pot Mc Pot!", "Porcini Bambini!", "Baba", "Poo", "Silly Billy", "Banana Show"]

reaction_to_name = ["Interesting name!", "What a lovely name!", "Where did you get that name? *chuckles*", "Nice", "*yawns* Sorry, I'm a bit tired... I didn't sleep that well last night. Ok. \nSorry again but that was a lie. To tell you the truth I find your name a bit boring. *yawns again*"]


def intro():
    '''
    This is the intro=duction. White Duck is beginning to talk and asks the user's name.
    '''
    answer = input("Oh, hello there! Nice to meet you! Or have we met before? (Y/N) ")

    if answer in yes:
        print("Oh that’s right! I remember you now. But what’s your name again? Wait, don’t tell me! It starts with…")
        time.sleep(3)
        print("It's... ")
        time.sleep(2)
        print(random.choice(silly_names))
        answer = input("Oh, did I get it wrong? (Y/N)")
        if answer in yes:
            name = input("Well, why don't you tell me your name then? ")

            if name in silly_names:
                print("*chuckles* You do have a funny name!")
            
            else:
                print(name.capitalize() + "... " + random.choice(reaction_to_name))

    elif answer in no:
        print("Let me introduce myself then. I’m White Duck!")
        name = input("What’s your name? ")
        print(name.capitalize() + "... " + random.choice(reaction_to_name))

    else:
        print("C'mon! That was a simple question that required a simple answer!")
        print("But have no fear. Let's start again.")
        intro()


# chat continues
def chat():
    """
    This is where the main chat happens
    """
    print("Well, my dear friend " + name + "." "Let's have a little chat now. If you want, of course. I'm not going to force you to do anything you don't want to. *winks*")
    answer = input("So you want to have a chat, right? Y/N")
    if answer in yes:
        print("Great.")
    elif answer in no:
        print("What do you mean, you don't want to have a chat?")
        answer = input("Ok, I'm feeling generous today so I'll give you another chance to say yes, ok? You want to have a chat, don't you? Y/N")
        if answer in yes:
            print("That's the spirit!")
        elif answer in no:
            print("QUACK!")
        else:
            print("But that's not what I asked! Try again.")
            chat()
    else:
        print("Ok, back to the beginning. But answer the question next time.")
        chat()

def game_rules():
    """
    Before the game starts White Duck explains the rules
    """
    print("I'm getting a bit bored now. What do you say, we play a little game of Rock, Paper, Scissors?")
    time.sleep(2)
    print("That was just a rethoric question. I tell you what, we play one round just to get you used to the rules and we see how it goes! ")
    time.sleep(2)
    print("So it won't really matter who wins this round, ok? Then we can play best of three afterwards.")
    time.sleep(2)
    print("Let's get started! The rules are bla blab bka")
    time.sleep(2)

# game of rock, paper, scissors
def first_round():
    user_choice = input("What would you like to choose: Rock, Paper or Scissors? ")
    options = ["rock", "paper", "scissors"]
    duck_choice = random.choice(options)
    print(f"\nOK. You chose {user_choice}, and I chose {duck_choice}.\n")
    time.sleep(1)
    print("Hmm... What does that mean? Let me think...")
    time.sleep(2)

    if user_choice == duck_choice:
        print("Oh! It's a tie! We have to play it again.")
        first_round()
    elif user_choice == "rock":
        if duck_choice == "scissors":
            print("Drat! I guess you won this turn.")
        else:
            print("I win!")
    elif user_choice == "paper":
        if duck_choice == "rock":
            print("Oh no! I lost!")
        else:
            print("I win!")
    elif user_choice == "scissors":
        if duck_choice == "rock":
            print("I win")
        else:
            print("I lost... :(")

def 

def best_of_three():
    while user_score or duck_score != final_score:


# nervous breakdown
# def nervous_breakdown()

# end
# def end()


intro()
#chat()
first_round()