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
                   "Pot Pot Mc Pot!", "Porcini Bambini!", "Baba", "Popo",
                   "Silly Billy", "Banana Show"]

    reaction_to_name = ["Interesting name!", "What a lovely name!",
                        "Where did you get that name? *chuckles*", "Nice",
                        "*yawns* Sorry, boring name. *yawns again*"]

    print("Guess who's back?")
    print("...")
    time.sleep(2)
    print("It's White Duck!")
    time.sleep(3)
    print("...")
    time.sleep(1)

    print("\nOh, hello there! Nice to meet you!")
    print("\nOr have we met before? (Y/N)\n")
    answer = input()
    answer = answer.lower()

    if answer in yes:
        print("\nOh that’s right! I remember you now.")
        time.sleep(1)
        print("\nBut what’s your name again?")
        print("\nWait, don’t tell me! It starts with...")
        time.sleep(3)
        print("\nIt's... \n")
        time.sleep(2)
        print(random.choice(silly_names))
        time.sleep(1)

        print("\nOh, did I get it wrong? (Y/N)\n")
        answer = input()
        answer = answer.lower()

        if answer in yes:
            print("\nWell, why don't you tell me your name then?\n")
            name = input()

            if name in silly_names:
                print("\n*chuckles* You do have a funny name! ")

            else:
                print(name.capitalize() + "... " +
                      random.choice(reaction_to_name))

        elif answer in no:
            print("\n*chuckles* You do have a funny name! ")

        else:
            print("\nYou were meant to say 'yes' or 'no'... But nevermind.")

    elif answer in no:
        print("\nLet me introduce myself then. I’m White Duck! ")
        print("\nWhat’s your name?\n")
        name = input()
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
    There are two main chat functions. This is the first part
    """
    print("\nAnyway...")
    time.sleep(1)
    print("\nLet's have a little chat now.")
    print("\nSo you want to have a chat, right? (Y/N)\n")
    answer = input()
    answer = answer.lower()

    if answer in yes:
        print("\nGreat. I'm a bit of a chatterbox sometimes.")
        time.sleep(2)
        print("\nBut sometimes I just go quiet.")
        time.sleep(3)
        print("\nOne time I went quiet for a whole year.")
        time.sleep(3)
        print("\nAfter that I just couldn't stop talking!")
        time.sleep(3)
        print("\nEventually I felt really exhausted!")
        time.sleep(5)
        print("\nBut enough of talking about me for now.")
        time.sleep(1)
        print("\nLet's talk about you!")
        time.sleep(1)
        print("\nIf you want? (Y/N)\n")
        answer = input()
        answer = answer.lower()
        if answer in yes:
            print("\nGood stuff!")
            time.sleep(1)
            print("\nSo...")
            time.sleep(1)
            chat_continues()

        elif answer in no:
            print("\nOh ok then. Let's play a little game instead.")
            time.sleep(1)
            game_intro()

    elif answer in no:
        print("\nWhat do you mean, you don't want to have a chat?")
        time.sleep(1)
        print("\nChange your mind time! C'mon, have a chat! (Y/N)\n")
        answer = input()
        answer = answer.lower()
        if answer in yes:
            print("\nThat's the spirit!")
            time.sleep(1)
            chat_continues()
        elif answer in no:
            print("\nQUACK!")
            time.sleep(2)
            print("\nHmmm... Let's play a little game instead.")
            game_intro()
        else:
            print("\nBut that's not what I asked! Try again.")
            chat()
    else:
        print("\nWrong answer. Back to the beginning.")
        chat()


def chat_continues():
    '''
    A rather random chat continues if user choses to do so
    '''
    print("\nDo you like cooking? (Y/N)\n")
    answer = input()
    answer = answer.lower()

    if answer in yes:
        print("\nOh good! Because I don't!")
        time.sleep(1)
        print("\nBut I love eating and I rather fancy something sweet.")
        print("\nI was wondering if you'd make it for me? Please? (Y/N)\n")
        answer = input()
        answer = answer.lower()
        if answer in yes:
            print("Thanks! Can you make me a giant rainbow profiterole tower?")
            print("You can google it. Shouldn't be too difficult!")
            time.sleep(5)
            print("Several hours later...")
            time.sleep(3)
            print("That was okay but could you make it crispier next time?")
            print("\n...")
            print("\nThanks pal!")
            time.sleep(2)
            print("\nOk. We move on!")
            time.sleep(2)
            game_intro()

        elif answer in no:
            print("\nOh, that's a bit mean...")
            time.sleep(2)
            print("\nLet's do something else now.")
            time.sleep(2)
            game_intro()

    elif answer in no:
        print("\nThat's too bad.")
        print("\nLet's do something else now.")
        time.sleep(2)
        game_intro()

    else:
        chat_continues()


def game_intro():
    """
    White Duck proposes a game of Rock Paper Scissors and offers alternatives
    if user doesn't want to play game. If user wants to play, he explains the
    rules
    There's an option to end the game altogether if user doesn't want to
    continue
    """
    print("\nWould you like to play a game of Rock, Paper, Scissors? (Y/N)\n")
    answer = input()
    answer = answer.lower()

    if answer in yes:
        time.sleep(2)
        print("\nGreat!")
        print("\nDo you know the rules? (Y/N)\n")
        answer = input()
        answer = answer.lower()

        if answer in yes:
            print("\nGood. Let's play one round and see how it goes.")
            time.sleep(2)
            print("\nThe first round is starting now!")
            first_round()
        elif answer in no:
            print("\nWe play against each other.")
            print("\nWe must choose one of these:")
            print("\nROCK")
            print("\nPAPER")
            print("\nSCISSORS")
            print("\nRock beats Scissors beats Paper beats Rock. Very simple!")
            time.sleep(2)
            print("\nThe first round is starting now!")
            first_round()
        else:
            print("\nPlease say Y or N\n")
            answer = input()
            answer = answer.lower()
            game_intro()

    elif answer in no:
        print("\nOh really? I'm a bit disappointed. We can do something else.")
        print("\nWould you like me to tell you a story? (Y/N)\n")
        answer = input()
        answer = answer.lower()
        if answer in yes:
            story_duck_language()
        elif answer in no:
            print("\nHmmm. Looks like you're not in the mood for anything.")
            print("\nIn which case let's finish this at once! (Y/N)\n")
            answer = input()
            answer = answer.lower()
            if answer in no:
                print("\nGreat! Let's start again.")
                time.sleep(2)
                game_intro()
            elif answer in yes:
                print("\nWell... It was nice meeting you.")
                time.sleep(3)
                end()
            else:
                print("\nInvalid answer. I'll take that as a no.")
                time.sleep(3)
                end()
        else:
            print("\nInvalid answer. I'll take that as a no.")
            time.sleep(3)
            end()
    else:
        game_intro()


def story_duck_language():
    '''
    White Duck mistakenly tell the story in duck language but offers the
    option of telling the story in English afterwards or playing the game
    There's an option to end the game altogether if user doesn't want to
    continue
    '''
    print("\nOnce upon a time bla bla bla")
    time.sleep(1)
    print("bla bla bla bla quack quack quack")
    time.sleep(1)
    print("quack quack quack quack quack quack")
    time.sleep(1)
    print("quack quack quack bla bla bla bla ")
    time.sleep(1)
    print("bla bla bla bla quack quack quack")
    time.sleep(1)
    print("And we all lived happily ever after.")
    time.sleep(1)
    print("THE END!")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("WHAT??? You don't seem very impressed.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Oh! My bad! I just told you the story in duck language!")
    time.sleep(1)
    print("Apologies! I can tell you the same story in English...")
    time.sleep(1)
    print("YES! NOOOOOOO!")
    answer = input()
    answer = answer.lower()
    if answer in yes:
        story_english()
    elif answer in no:
        print("\nHave you changed your mind about playing a game then?")
        time.sleep(1)
        print("(Y/N)")
        answer = input()
        answer = answer.lower()
        if answer in yes:
            print("\nGreat. Let's go back to the beginning!")
            time.sleep(1)
            game_intro()
        elif answer in no:
            print("\nThen it's time to say bye!")
            time.sleep(1)
            end()
        else:
            print("\nInvalid answer. I'll take that as a no.")
            time.sleep(3)
            end()


def story_english():
    '''
    White Duck tells the story in English and asks if user has changed
    their mind about playing the game
    There's an option to end the game altogether if user doesn't want to
    continue
    '''
    print("\nOnce upon a time...")
    time.sleep(1)
    print("I met a nice person who made me a profiterole tower.")
    time.sleep(1)
    print("Unfortunately the profiterole tower wasn't that great.")
    time.sleep(1)
    print("So I told them the truth.")
    time.sleep(1)
    print("And I hope they learned their lesson!")
    time.sleep(1)
    print("And we all lived happily ever after.")
    time.sleep(1)
    print("THE END!")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("I hope you enjoyed it! But I have a question now.")
    time.sleep(1)
    print("\nHave you changed your mind about playing a game?")
    time.sleep(1)
    print("(Y/N)")
    answer = input()
    answer = answer.lower()
    if answer in yes:
        print("\nGreat. Let's go back to the beginning!")
        time.sleep(1)
        game_intro()
    elif answer in no:
        print("\nThen it's time to say bye!")
        time.sleep(1)
        end()
    else:
        print("\nInvalid answer. I'll take that as a no.")
        time.sleep(3)
        end()


# game of rock, paper, scissors
def first_round():
    """
    This is when the first round starts
    It's just a trial to get used to playing the Rock Paper Scissors game
    """
    time.sleep(1)
    print("\nWhat would you like to choose?")
    print("\nROCK, PAPER or SCISSORS?\n")
    user_choice = input()
    user_choice = user_choice.lower()
    duck_choice = random.choice(options)

    def calculating_result():
        print(f"\nOK. You chose {user_choice}, and I chose {duck_choice}.\n")
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
        first_round()
    elif user_choice == "rock":
        if duck_choice == "scissors":
            calculating_result()
            print("\nDrat! I guess you won this turn.")
            chat_before_game()
        else:
            calculating_result()
            print("\nI win!")
            chat_before_game()
    elif user_choice == "paper":
        if duck_choice == "rock":
            calculating_result()
            print("\nOh no! I lost!")
            chat_before_game()
        else:
            calculating_result()
            print("\nI win!")
            chat_before_game()
    elif user_choice == "scissors":
        if duck_choice == "rock":
            calculating_result()
            print("\nI win")
            chat_before_game()
        else:
            calculating_result()
            print("\nI lost... :(")
            chat_before_game()

    else:
        print("\nPlease type a valid option!\n")
        first_round()


def chat_before_game():
    '''
    A blurb about how the game will be played. Whoever scores 3 points
    first wins the game.
    There's an option to stop the game at any point if user wants
    '''
    print("\nWell done. Let's now play it for real.")
    print("And the winner will get a prize!")
    time.sleep(3)
    print("\nWhoever get 3 points first wins the game!")
    time.sleep(3)
    print("\nCan I just remind you that at the end of the day")
    print("it doesn't really matter who wins or loses.")
    time.sleep(5)
    print("\n(If you want to end the game please type 'stop' at any time)")
    time.sleep(3)
    second_round()


def second_round():
    '''
    This is the main game. There are as many rounds as needed until
    one of the players scores 3 points
    There's a score count and for each game won the player gets one point
    '''
    user_count = 0
    duck_count = 0

    while user_count < 3 or duck_count < 3:

        duck_choice = random.choice(options)

        print("\nWhat would you like to choose?")
        print("\nROCK, PAPER or SCISSORS?\n")
        user_choice = input()
        user_choice = user_choice.lower()

        def calculating_result():
            print(f"\nYou chose {user_choice}, and I chose {duck_choice}.\n")
            time.sleep(1)

            print("\nCalculating result...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("!")
            time.sleep(1)

        if user_choice == duck_choice:  # neither players score when they tie
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

        elif user_choice == "stop":
            print("\nThanks for playing! The final score was: ")
            print(f"\nYou: {user_count} - White Duck: {duck_count}")
            time.sleep(4)
            if user_count > duck_count:
                duck_lost()
            elif user_count < duck_count:
                duck_won()
            else:
                tie()  # tie scenario only happens if user stops the game

        else:
            print("\nPlease type a valid option!\n")
            continue

    print(f'\nWhite Duck: {duck_count} - You: {user_count}')
    print()


def duck_won():
    '''

    '''
    print("\nI won! No hard feelings, right? *grins*\n")
    time.sleep(3)
    duck_wins()


def duck_lost():
    print("\nNoooooo! I don't accept it! Aaaaaaaaaaaaaaarrrgghhh!!!!!")
    time.sleep(3)
    print("\n*White Duck trods on the computer*")
    time.sleep(2)
    print("\n*White Duck is having a wobbly*")
    time.sleep(2)
    print("\n*White Duck is extremely angry... He's gone red all over*")
    time.sleep(2)
    print("\n*This is not a pretty sight!*")
    time.sleep(3)
    print("\n...")
    time.sleep(3)
    print("\nErr... Excuse me, this is the developer speaking now.")
    time.sleep(3)
    print("\nListen, I'm so sorry about White Duck's lack of sportsmanship.")
    time.sleep(2)
    print("\nCan I just suggest that you play one more round?")
    time.sleep(3)
    print("\nI know it's not fair though cause you won")
    time.sleep(3)
    print("and you deserve a prize but...")
    time.sleep(3)
    print("\nWill you give White Duck another chance? (Y/N)\n")
    answer = input()
    answer = answer.lower()

    if answer in yes:
        print("\n*footsteps approaching*")
        time.sleep(3)
        print("\nOh, I think our feathered friend is back.")
        time.sleep(3)
        print("Wait a second, has anyone actually asked me if")
        print("I want to play this silly game again?")
        time.sleep(3)
        print("What you think? Does he want to play again? (Y/N) ")
        answer = input()
        answer = answer.lower()

        if answer in yes:
            print("\nYou're right! And this time I'm going to win!")
            last_round()

        elif answer in no:
            print("\nYou got that wrong. I do want to play it one more time!")
            last_round()

        else:
            print("\nI didn't get that but that's irrelevant because it turns")
            print("out White Duck really wants to have one last go at it.")
            last_round()

    if answer in no:
        print("\nFair enough. You can claim your prize now.")
        time.sleep(3)
        print("\nQUACKQUACKQUACKQUACK ---DSIHDHS %^%$£^$(HIUIYTFCFghufyde^&%r")
        time.sleep(3)
        print("...")
        print("\nOh nevermind that noise.")
        prize()


def last_round():

    print("\nThis is the last round. You've only got one last shot!")

    print("\nWhat would you like to choose?")
    print("\nROCK, PAPER or SCISSORS?\n")
    user_choice = input()
    user_choice = user_choice.lower()
    duck_choice = random.choice(options)

    def calculating_result():
        print(f"\nYou chose {user_choice}, and I chose {duck_choice}.\n")
        time.sleep(1)

        print("\nCalculating result...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("!")
        time.sleep(1)

    if user_choice == duck_choice:
        calculating_result()
        print("\nOh! It's a tie!")
        tie_prize()
    elif user_choice == "rock":
        calculating_result()
        if duck_choice == "scissors":
            print("\n:(")
            duck_defeated()
        else:
            print("\nI win!")
            duck_wins()
    elif user_choice == "paper":
        calculating_result()
        if duck_choice == "rock":
            print("\nOh no! I lost!")
            duck_defeated()
        else:
            print("\nI win!")
            duck_wins()
    elif user_choice == "scissors":
        calculating_result()
        if duck_choice == "rock":
            print("\nI win")
            duck_wins()
        else:
            print("\nI lost... :(")
            duck_defeated()
    else:
        print("\nPlease type a valid option!\n")
        last_round()


def prize():
    print("\nCongratulations!")
    time.sleep(2)
    print("\nHere's your special prize for winning a game of")
    print("Rock Paper Scissors!\n")
    time.sleep(2)
    print("\n*drums*")
    time.sleep(2)
    print("\n...\n")
    time.sleep(3)
    prize = ["A SLICE OF CAKE!", "A RUBBER DUCK!",
             "A PAIR OF FAKE EYELASHES!", "A PINK UMBRELLA!",
             "A PAIR OF READING GLASSES!", "A RECIPE BOOK!",
             "A ROMANTIC DINNER IN A FANCY RESTAURANT!",
             "A RIDE ON A ROLLERCOASTER!"]
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
    '''
    The user has the option to play one more round
    '''
    print("It's a tie. Would you like to play one last round? (Y/N)\n")
    answer = input()
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
    '''
    This is the end game for duck
    '''
    print("\n...")
    time.sleep(2)
    print("\nWhite Duck fainted... The poor fellow.")
    time.sleep(2)
    print("\nNevermind. You can claim your prize now!")
    time.sleep(2)
    prize()


def end():
    print("\nGoodbye!\n")
    print("\nPlay again? (Y/N)\n")
    answer = input()
    answer = answer.lower()
    if answer in yes:
        main()
    else:
        exit()


def main():
    intro()
    chat()
    """
    game_intro()
    first_round()
    second_round()
    end()
    """


# Intro

print("Welcome to White Duck Is Back!")


main()
