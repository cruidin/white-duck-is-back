import time
import random


# Answers to yes or no questions
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

# Rock, Paper, Scissors variables
options = ["rock", "paper", "scissors"]
winner = ["user", "duck"]


def intro():
    '''
    This is the introduction. White Duck is beginning to talk and asks the 
    user's name.
    '''
    silly_names = ["Bibo Holiday!", "Catacata Plum!", "Carrot Bunch III!", 
    "Pot Pot Mc Pot!", "Porcini Bambini!", "Baba", "Poo", "Silly Billy", 
    "Banana Show"]

    reaction_to_name = ["Interesting name!", "What a lovely name!", 
    "Where did you get that name? *chuckles*", "Nice", 
    "*yawns* Sorry, I find your name a bit boring. *yawns again*"]

    answer = input("\nOh, hello there! Nice to meet you! Or have we met before? (Y/N) ")

    if answer in yes:
        print("\nOh that’s right! I remember you now.")
        time.sleep(1)
        print("\nBut what’s your name again? Wait, don’t tell me! It starts with")
        time.sleep(3)
        print("\nIt's... \n")
        time.sleep(2)
        print(random.choice(silly_names))
        time.sleep(1)
        answer = input("\nOh, did I get it wrong? (Y/N) ")

        if answer in yes:
            name = input("\nWell, why don't you tell me your name then? ")

            if name in silly_names:
                print("\n*chuckles* You do have a funny name! ")

            else:
                print(name.capitalize() + "... " 
                + random.choice(reaction_to_name))

        elif answer in no:
            print("\n*chuckles* You do have a funny name! ")

        else:
            print("\nYou were meant to say 'yes' or 'no'... But nevermind.")

    elif answer in no:
        print("\nLet me introduce myself then. I’m White Duck! ")
        name = input("\nWhat’s your name? ")
        if name in silly_names:
            print("\n*chuckles* You do have a funny name! ")

        else:
            print(name.capitalize() + "... " + random.choice(reaction_to_name))

    else:
        print("\nC'mon! That was a yes or no type of question!")
        intro()


# chat continues
def chat():
    """
    This is where the main chat happens
    """
    print("\nAnyway...")
    time.sleep(1)
   
    print("\nLet's have a little chat now.")
    
    answer = input("\nSo you want to have a chat, right? Y/N ")
    if answer in yes:
        print("\nGreat. I'm a bit of a chatterbox sometimes.")
        time.sleep(1)
        print("\nBut sometimes I just go quiet.")
        time.sleep(1)
        print("\nOne time I went quiet for a whole year. And then the next year I just couldn't stop talking!")
        print("\nBut after a couple of months I felt really exhausted!")
        time.sleep(1)
        print("\nBut enough of talking about me for now.")
        time.sleep(1)
        print("\nLet's talk about you!")
        time.sleep(1)

    elif answer in no:
        print("\nWhat do you mean, you don't want to have a chat?")
        time.sleep(1)
        answer = input("\nOk, are you really sure you don't want to have a chat? Y/N")
        if answer in no:
            print("That's the spirit!")
        elif answer in yes:
            print("QUACK!")
        else:
            print("But that's not what I asked! Try again.")
            chat()
    else:
        print("\nOk, back to the beginning. But answer the question next time.")
        chat()


# def chat_continues():


def game_rules():
    """
    Before the game starts White Duck explains the rules
    """
    print("\nBut I'm getting a bit bored now. What do you say, we play a little game of Rock, Paper, Scissors?")
    time.sleep(2)
    answer = input("\nDo you know the rules? Y/N ")
    if answer in yes:
        print("\nGood. Let's play it! We play one round and see how it goes. So it won't really matter who wins this round, ok? It's just for fun.")
    elif answer in no:
        print("\nRock beats Scissors beats Paper beats Rock. Very simple!")
    else:
        answer = input("\nPlease say Y or N ")


# game of rock, paper, scissors
def first_round():
    """
    This is when the first round starts
    """
    user_choice = input("\nWhat would you like to choose: Rock, Paper or Scissors? ")
    duck_choice = random.choice(options)
    print(f"\nOK. You chose {user_choice}, and I chose {duck_choice}.\n")
    time.sleep(1)
    print("\nHmm... What does that mean? Let me think...")
    time.sleep(2)
    if user_choice == duck_choice:
        print("\nOh! It's a tie! We have to play it again.")
        first_round()
    elif user_choice == "rock":
        if duck_choice == "scissors":
            print("\nDrat! I guess you won this turn.")
        else:
            print("\nI win!")
    elif user_choice == "paper":
        if duck_choice == "rock":
            print("\nOh no! I lost!")
        else:
            print("\nI win!")
    elif user_choice == "scissors":
        if duck_choice == "rock":
            print("\nI win")
        else:
            print("\nI lost... :(")


def chat_before_game():
    print("\nWell done. Let's now play it again but this time it matters who wins. And the winner will get a prize!")
    time.sleep(2)
    print("\nBut before we continue can I just remind you that at the end of the day, it doesn't really matter who wins or loses. Try to keep your cool in case you lose, ok?")
    time.sleep(2)


def second_round():

    user_count = 0
    duck_count = 0
    player = False

    while player == False:

        duck_choice = random.choice(options)
       
        print("\nIf you want to end the game please type 'stop' at any time.")
        print()

        user_choice = input("\nWhat would you like to choose: Rock, Paper or Scissors? ")

        print(f"\nThis time you chose {user_choice}, and I chose {duck_choice}.\n")
        time.sleep(1)
        print("\nSorry, I always need a bit of time to think about it...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("!")
        time.sleep(1)

        if player.lower() == "stop":
            print()
            print(f"Thanks for playing! Your final record was {user_count}-{duck_count}")
            print()
            break

        if user_choice == duck_choice:
            print("\nOh! It's a tie! We have to play it again.")
            second_round()

        elif user_choice == "rock":

            if duck_choice == "scissors":
                print("\nI lost!")
                user_count += 1

            else:
                print("\nI won!")
                duck_count += 1

        elif user_choice == "paper":

            if duck_choice == "rock":
                print("\nI lost!")
                user_count += 1

            else:
                print("\nI won!")
                duck_count += 1

        elif user_choice == "scissors":

            if duck_choice == "rock":
                print("\nI won!")
                duck_count += 1

            else:
                print("\nI lost!")
                user_count += 1

    print(f'|White Duck: {duck_count} - You: {user_count}')
    print()

def duck_won():

    print("I won! No hard feelings, right? *grins*")
    duck_wins()

def duck_lost():

    print("Noooooo! I don't accept it! Aaaaaaaaaaaaaaarrrgghhh!!!!!")
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
    print("Can I just suggest that you play one more round?")
    print("I know it's not fair though cause you won and you deserve a prize but...")
    print("I don't know... Well, I'll leave it up to you.")
    print("Will you give White Duck another chance?")

    answer = input("Y/N ")

    if answer in yes:
        print("*footsteps approaching*")
        print("Oh, I think our feathered friend is back. He must have heard you say yes.")
        print("White Duck speaking now!")
        print("Wait a second, has anyone actually dared to ask me if I want to play this silly game again?")

        random_answer = ["Of course I do!", "No, I don't!", "Hmmm maybe..."]

        print(random.choice(random_answer))

        if random_answer in random_answer[0]:
            second_round()

        elif random_answer in random_answer[1]:
            print("...")
            print("Oh well, I guess then we can declare user the winner!")
            prize()

        else:
            print("I'll do a deal with you. If you win you must share your prize with me.")
            print("And if I win... I'll share my prize with you. I promise.")
            answer = input("Do we have a deal? Y/N ")

            if answer in yes:
                print("Hooray! Let's go!")
                second_round()

            elif answer in no:
                print("Ok. Goodbye!")
                prize()

            else:
                print("Just say yes or no!")


    if answer in no:
        print("Fair enough. You can claim your prize now.")
        print("QUACKQUACKQUACKQUACK ---DSIHDHS %^%$£^$(HIUIYTFCFghufyde^&%r")
        print("Oh nevermind that noise.")


def prize():
    print("Congratulations! Here's your special prize for winning a game of Rock Paper Scissors!")
    prize = ["A SLICE OF CAKE!",
    "A RUBBER DUCK!",
    "FAKE EYELASHES!",
    ]
    print(random.choice(prize))

def duck_wins():
    print("I am here to collect my prize!")

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
