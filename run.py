import time
import random


# Answers to yes or no questions
yes = ["y", "yes"]
no = ["n", "no"]


# List with options for Rock, Paper, Scissors game
options = ["rock", "paper", "scissors"]

# Scores
user_count = 0
duck_count = 0


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
    answer = answer.lower()

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
        answer = answer.lower()

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
    answer = answer.lower()

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
            print("\nThat's the spirit!")
        elif answer in yes:
            print("\nQUACK!")
            game_rules()
        else:
            print("\nBut that's not what I asked! Try again.")
            chat()
    else:
        print("\nOk, back to the beginning. But answer the question next time.")
        chat()


def chat_continues():

    answer = input("\nDo you like cooking?")
    answer = answer.lower()

    if answer in yes:
        print("\I don't! But I love eating and I've got a great recipe here...")

    elif answer in no:
        print("\nThat's too bad.")

    else:
        chat_continues()


def game_rules():
    """
    Before the game starts White Duck explains the rules
    """
    answer = input("\nBut I'm getting a bit bored now. What do you say, we play a little game of Rock, Paper, Scissors?")
    answer = answer.lower()

    if answer in yes:
        time.sleep(2)

        answer = input("\nDo you know the rules? Y/N ")
        answer = answer.lower()

        if answer in yes:
            print("\nGood. Let's play it! We play one round and see how it goes. So it won't really matter who wins this round, ok? It's just for fun.")
        elif answer in no:
            print("\nRock beats Scissors beats Paper beats Rock. Very simple!")
        else:
            answer = input("\nPlease say Y or N ")
            answer = answer.lower()
    
    elif answer in no:
        print("\nOh really? I'm a bit disappointed... We can do something else instead.")
        answer = input("\nWould you like me to tell you a story? Y/N ")
        answer = answer.lower()

        if answer in yes:
            print("\nOnce upon a time bla bla bla")

        if answer in no:
            print("\nHmmm... Looks like you're not really in the mood for anything.")
            print("\nIn which case let's finish this at once! But I'll give you one last chance to change your mind...")
            answer = input("\nWould you like to start over? Y/N ")
            answer = answer.lower()

            if answer in yes:
                print("Great! I'm glad I asked all the same. Let's start again.")
                time.sleep(2)
                game_rules()

            elif answer in no:
                print("\nWell... It was nice meeting you.")
                time.sleep(3)
                end()

            else:
                print("\nInvalid answer. I'll take that as a no.")
                time.sleep(3)
                end()
            

    else:
        game_rules()


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
    print("\nAnd if you want to end the game please just type 'stop' at any time.")
    print()


def second_round():

    user_count = 0
    duck_count = 0
    scores = {user_count: 0, duck_count: 0}

    while user_count < 3 or duck_count < 3:


        duck_choice = random.choice(options)

        user_stop = "stop"

        user_choice = input("\nWhat would you like to choose: Rock, Paper or Scissors? ")

        def calculating_result():
            print(f"\nThis time you chose {user_choice}, and I chose {duck_choice}.\n")
            time.sleep(1)

            print("\nCalculating result...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("!")
            time.sleep(1)



        if user_choice == duck_choice:
            calculating_result()
            print("\nOh! It's a tie! We have to play it again.")
            user_count == 0
            duck_count == 0

        elif user_choice == "rock":
            calculating_result()
            if duck_choice == "scissors":
                print("\nI lost!")
                user_count += 1
                print(f'White Duck: {duck_count} - You: {user_count}')


            else:
                print("\nI won!")
                duck_count += 1
                print(f'White Duck: {duck_count} - You: {user_count}')


        elif user_choice == "paper":
            calculating_result()
            if duck_choice == "rock":
                print("\nI lost!")
                user_count += 1
                print(f'White Duck: {duck_count} - You: {user_count}')


            else:
                print("\nI won!")
                duck_count += 1
                print(f'White Duck: {duck_count} - You: {user_count}')


        elif user_choice == "scissors":
            calculating_result()
            if duck_choice == "rock":
                print("\nI won!")
                duck_count += 1
                print(f'White Duck: {duck_count} - You: {user_count}')


            else:
                print("\nI lost!")
                user_count += 1
                
                print(f'White Duck: {duck_count} - You: {user_count}')

        elif user_stop == "stop":
            print()
            print(f"Thanks for playing! The final score was: \nYou: {user_count} - White Duck: {duck_count}")
            print()
            if user_count > duck_count:
                duck_lost()
            elif user_count < duck_count:
                duck_won()
            else:
                tie()
 
        if user_count == 3:
            
            duck_lost()
        
        elif duck_count == 3:
            
            duck_won()

    print(f'White Duck: {duck_count} - You: {user_count}')
    print()


def duck_won():

    print("\nI won! No hard feelings, right? *grins*\n")
    duck_wins()

def duck_lost():

    print("\nNoooooo! I don't accept it! Aaaaaaaaaaaaaaarrrgghhh!!!!!")
    time.sleep(2)
    print("\n*White Duck trods on the computer*")
    time.sleep(1)
    print("\n*White Duck is having a wobbly*")
    time.sleep(1)
    print("\n*White Duck is extremely angry... He's gone red all over*")
    time.sleep(1)
    print("\n*This is not a pretty sight!*")
    time.sleep(3)
    print("\n...")
    time.sleep(2)
    print("\nErr... Excuse me, this is the developer speaking now.")
    time.sleep(1)
    print("\nListen, I'm so sorry about White Duck's lack of sportsmanship.")
    time.sleep(2)
    print("\nCan I just suggest that you play one more round?")
    print("\nI know it's not fair though cause you won and you deserve a prize but...")
    print("\nWill you give White Duck another chance?")

    answer = input("Y/N ")
    answer = answer.lower()

    if answer in yes:
        print("\n*footsteps approaching*")
        print("\nOh, I think our feathered friend is back. He must have heard you say yes.")
        print("\nWhite Duck speaking now!")
        print("Wait a second, has anyone actually dared to ask me if I want to play this silly game again?")

        answer = input("What do you think? Does he want to play or not?" )
        answer = answer.lower()

        if answer in yes:
            print("\nYou're right! And this time I'm going to win!")
            last_round()

        elif answer in no:
            print("\nOh well, you got that wrong. I do want to play again.")
            last_round()

        else:
            print("\nI didn't get that but that's irrelevant because it turns out White Duck really wants to have one last go at this game.")


    if answer in no:
        print("\nFair enough. You can claim your prize now.")
        print("\nQUACKQUACKQUACKQUACK ---DSIHDHS %^%$£^$(HIUIYTFCFghufyde^&%r")
        print("\nOh nevermind that noise.")
        prize()


def last_round():

    print("\nThis is the last round. You've only got one last shot!")

    user_choice = input("\nWhat would you like to choose: Rock, Paper or Scissors? ")

    duck_choice = random.choice(options)

    print(f"\nOK. You chose {user_choice}, and I chose {duck_choice}.\n")
    time.sleep(1)
    print("\nHmm... What does that mean? Let me think...")
    time.sleep(2)

    if user_choice == duck_choice:
        print("\nOh! It's a tie!")
        tie_prize()
    elif user_choice == "rock":
        if duck_choice == "scissors":
            print("\n:(")

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



def prize():
    print("\nCongratulations! Here's your special prize for winning a game of Rock Paper Scissors!\n")
    time.sleep(3)
    prize = ["A SLICE OF CAKE!",
    "A RUBBER DUCK!",
    "A PAIR OF FAKE EYELASHES!",
    "A PINK UMBRELLA!",
    "A PAIR OF READING GLASSES!",
    "A RECIPE BOOK!",
    "A ROMANTIC DINNER IN A FANCY RESTAURANT!",
    "A RIDE ON A ROLLERCOASTER!"
    ]
    print(random.choice(prize))
    time.sleep(3)
    end()

def tie_prize():
    print("\nEverybody is a winner!")
    time.sleep(1)
    print("\nYou need to share the prize.")
    time.sleep(2)
    prize()


def duck_wins():
    print("\nI am here to collect my prize!")
    time.sleep(2)
    prize()


def tie():
    answer = input("It's a tie. Would you like to play one last round? Y/N ")
    answer = answer.lower()

    if answer in yes:
        
        last_round()

    elif answer in no:
        print("\nEverybody is a winner!")
        time.sleep(1)
        print("\nYou need to share the prize.")
        time.sleep(2)
        prize()

    else:
        print("\n Answer the question.")
        tie()


def duck_defeated():
    print("\n...")
    time.sleep(2)
    print("\nWhite Duck fainted... The poor fellow.")
    time.sleep(2)
    print("\nNevermind. You can claim your prize now!")
    time.sleep(2)
    prize()


def end():
    print("\nGoodbye!\n")
    exit()


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
    end()

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
