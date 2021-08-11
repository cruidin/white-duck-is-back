import time
import random


# Answers to yes or no questions
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# Rock, Paper, Scissors variables
options = ["rock", "paper", "scissors"]
winner = ["user", "duck"]


# Instructions

# Start


def intro():
    '''
    This is the introduction. White Duck is beginning to talk and asks the user's name.
    '''
    silly_names = ["Bibo Holiday!", "Catacata Plum!", "Carrot Bunch III!", "Pot Pot Mc Pot!", "Porcini Bambini!", "Baba", "Poo", "Silly Billy", "Banana Show"]

    reaction_to_name = ["Interesting name!", "What a lovely name!", "Where did you get that name? *chuckles*", "Nice", "*yawns* Sorry, I find your name a bit boring. *yawns again*"]

    answer = input("Oh, hello there! Nice to meet you! Or have we met before? (Y/N) ")

    if answer in yes:
        print("Oh that’s right! I remember you now.")
        time.sleep(1)
        print("But what’s your name again? Wait, don’t tell me! It starts with… ")
        time.sleep(3)
        print("It's... ")
        time.sleep(2)
        print(random.choice(silly_names))
        time.sleep(1)
        answer = input("Oh, did I get it wrong? (Y/N) ")

        if answer in yes:
            name = input("Well, why don't you tell me your name then? ")

            if name in silly_names:
                print("*chuckles* You do have a funny name! ")

            else:
                print(name.capitalize() + "... " + random.choice(reaction_to_name))

        elif answer in no:
            print("*chuckles* You do have a funny name! ")

        else:
            print("You were meant to say 'yes' or 'no'... But it doesn't really matter.")

    elif answer in no:
        print("Let me introduce myself then. I’m White Duck! ")
        name = input("What’s your name? ")
        if name in silly_names:
            print("*chuckles* You do have a funny name! ")

        else:
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
    print("Anyway...")
    time.sleep(1)
    print("What was I saying?")
    time.sleep(1)
    print("Oh yes, I know. So, my dear friend...")
    time.sleep(1)
    print("\nLet's have a little chat now.")
    time.sleep(1)
    print("If you want, of course.")
    time.sleep(1)
    print("I'm not going to force you to do anything you don't want to. *winks*")
    time.sleep(1)
    answer = input("So you want to have a chat, right? Y/N ")
    if answer in yes:
        print("Great.")
        time.sleep(1)
        print("I'm a bit of a chatterbox sometimes.")
        time.sleep(1)
        print("But sometimes I just go quiet.")
        time.sleep(1)
        print("One time I went quiet for a whole year. And then the next year I just couldn't stop talking!")
        print("But after a couple of months I felt really exhausted!")
        time.sleep(1)
        print("But enough of talking about me for now.")
        time.sleep(1)
        print("Let's talk about you!")
        time.sleep(1)

    elif answer in no:
        print("What do you mean, you don't want to have a chat?")
        time.sleep(1)
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


#def chat_continues():


def game_rules():
    """
    Before the game starts White Duck explains the rules
    """
    print("But I'm getting a bit bored now.")
    time.sleep(1)
    print("What do you say, we play a little game of Rock, Paper, Scissors?")
    time.sleep(2)
    print("That was just a rethoric question.")
    time.sleep(1)
    print("I tell you what.")
    time.sleep(1)
    print("We play one round just to get you used to the rules and we see how it goes! ")
    time.sleep(2)
    print("So it won't really matter who wins this round, ok? It's just for fun.")
    time.sleep(2)
    print("Let's get started! You know the rules, right? Rock beats Scissors beats Paper beats Rock. Very simple!")
    time.sleep(2)


# game of rock, paper, scissors
def first_round():
    """
    This is when the first round starts
    """
    user_choice = input("What would you like to choose: Rock, Paper or Scissors? ")
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


def chat_before_game():
    print("Well done. Let's now play it again but this time it matters who wins.")
    time.sleep(2)
    print("And the winner will get a prize!")
    time.sleep(2)
    print("But before we continue can I just remind you that at the end of the day, it doesn't really matter who wins or loses.")
    time.sleep(2)
    print("In other words, I just need you to promise that you will keep your cool in case you lose, ok?")
    time.sleep(2)


def second_round():

        duck_choice = random.choice(options)

        user_choice = input("What would you like to choose: Rock, Paper or Scissors? ")

        print(f"\nThis time you chose {user_choice}, and I chose {duck_choice}.\n")
        time.sleep(1)
        print("Sorry, I always need a bit of time to think about it...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("!")
        time.sleep(1)

        if user_choice == duck_choice:
            print("Oh! It's a tie! We have to play it again.")
            second_round()

        elif user_choice == "rock":

            if duck_choice == "scissors":
                duck_lost()

            else:
                duck_won()

        elif user_choice == "paper":

            if duck_choice == "rock":
                duck_lost()

            else:
                duck_won()

        elif user_choice == "scissors":

            if duck_choice == "rock":
                duck_won()

            else:
                duck_lost()


def duck_won():

    print("I won! No hard feelings, right? *grins*")

def duck_lost():

    print("Noooooo! I don't accept it!")
    print("Aaaaaaaaaaaaaaarrrgghhh!!!!!")
    time.sleep(2)
    print("*White Duck trods on the computer*")
    time.sleep(1)
    print("*White Duck is having a wobbly*")
    time.sleep(1)
    print("*White Duck is extremely angry... He's gone red all over*")
    time.sleep(1)
    print("*This is not a pretty sight!*")
    time.sleep(3)
    print("...")
    time.sleep(2)
    print("Err... Excuse me, this is the developer speaking now.")
    time.sleep(1)
    print("Listen, I'm so sorry about White Duck's lack of sportsmanship.")
    print("He hates losing. He loses his mind whenever that happens.")



# nervous breakdown
# def nervous_breakdown()

# end
# def end()


def main():
    intro()
    chat()
    game_rules()
    first_round()
    chat_before_game()
    second_round()


# Intro
print("Guess who's back?")

print("...")
time.sleep(2)
print("It's White Duck!")
time.sleep(3)
print("...")
time.sleep(1)

print("Welcome to White Duck Is Back!")


main()
