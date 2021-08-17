# White Duck Is Back!
# By Patricia Melo
# https://github.com/cruidin


# Imports
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
    # variable with random names when Duck tries to guess user's name
    silly_names = ["Bibo Holiday!", "Catacata Plum!", "Carrot Bunch III!",
                   "Pot Pot Mc Pot!", "Porcini Bambini!", "Baba", "Popo",
                   "Silly Billy", "Banana Show"]
    # random reactions by Duck to user's name
    reaction_to_name = ["Interesting name!", "What a lovely name!",
                        "Where did you get that name? *chuckles*", "Nice",
                        "*yawns* Sorry, boring name. *yawns again*"]
    # Presentation
    print("Guess who's back?")
    print("...")
    time.sleep(2)
    print("It's White Duck!")
    time.sleep(3)
    print("...")
    time.sleep(1)

    # White Duck greets user
    print("\nOh, hello there! Nice to meet you!")
    print("\nOr have we met before? (Y/N)\n")
    answer = input()
    answer = answer.lower()
    # Duck tries to 'remember' user's name
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
        # White Duck asks for user's name
        if answer in yes:
            print("\nWell, why don't you tell me your name then?\n")
            name = input()
            # In case user types one of the random names Duck reacts to it
            if name in silly_names:
                print("\n*chuckles* You do have a funny name! ")

            else:
                print(name.capitalize() + "... " +
                      random.choice(reaction_to_name))

        elif answer in no:
            print("\n*chuckles* You do have a funny name! ")
        # It's not really relevant if user doens't answer correctly
        else:
            print("\nYou were meant to say 'yes' or 'no'... But nevermind.")
    # White Duck introduces himself in case user doesn't know him
    elif answer in no:
        print("\nLet me introduce myself then. I’m White Duck! ")
        # He asks for user's name
        print("\nWhat’s your name?\n")
        name = input()
        if name in silly_names:
            print("\n*chuckles* You do have a funny name! ")

        else:
            print(name.capitalize() + "... " + random.choice(reaction_to_name))
    # Replay function in case of incorrect input
    else:
        print("\nC'mon! That was a yes or no type of question!")
        intro()


# chat continues
def chat():
    """
    There are two main chat functions. This is the first part
    """
    # Duck asks if user wants to have a chat
    print("\nAnyway...")
    time.sleep(1)
    print("\nLet's have a little chat now.")
    print("\nSo you want to have a chat, right? (Y/N)\n")
    answer = input()
    answer = answer.lower()
    # White Duck talks for a bit
    if answer in yes:
        print("\nGreat. I'm a bit of a chatterbox sometimes.")
        time.sleep(2)
        print("\nBut sometimes I just go quiet.")
        time.sleep(3)
        print("\nOne time I went quiet for a whole year.")
        time.sleep(3)
        print("\nAfter that I just couldn't stop talking!")
        time.sleep(3)
        print("\n...")
        time.sleep(3)
        print("\nBut enough of that for now. Let's talk about you!")
        time.sleep(2)
        # The chat will continue if user wishes so
        print("\nIf you want? (Y/N)\n")
        answer = input()
        answer = answer.lower()
        if answer in yes:
            print("\nGood stuff!")
            time.sleep(1)
            print("\nSo...")
            time.sleep(1)
            chat_continues()
        # Otherwise he proposes they play a game
        elif answer in no:
            print("\nOh ok then. Let's play a little game instead.")
            time.sleep(1)
            game_intro()
        # Chat replay if invalid answer is given
        else:
            print("\nWrong answer!")
            chat()
    # Duck gets a bit cross if user doesn't want to chat
    elif answer in no:
        print("\nWhat do you mean, you don't want to have a chat?")
        time.sleep(1)
        # User is given another chance to change their mind
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
    # If user likes to cook White Duck will continue chatting
    if answer in yes:
        print("\nOh good! Because I don't!")
        time.sleep(1)
        print("\nBut I love eating and I rather fancy something sweet.")
        time.sleep(2)
        print("\nI was wondering if you'd make it for me? Please? (Y/N)\n")
        answer = input()
        answer = answer.lower()
        # White Duck talks for a bit before moving on to game_intro
        if answer in yes:
            print("Thanks! Can you make me a giant rainbow profiterole tower?")
            time.sleep(3)
            print("You can google it. Shouldn't be too difficult!")
            time.sleep(5)
            print("Several hours later...")
            time.sleep(3)
            print("That was okay but could you make it crispier next time?")
            time.sleep(2)
            print("\n...")
            time.sleep(2)
            print("\nThanks pal!")
            time.sleep(2)
            print("\nOk. We move on!")
            time.sleep(2)
            game_intro()
        # They move on to game_intro if user doesn't want to cook for Duck
        elif answer in no:
            print("\nOh, that's a bit mean...")
            time.sleep(2)
            print("\nLet's do something else now.")
            time.sleep(2)
            game_intro()
        # chat_continues is replayed in case of invalid input
        else:
            print("Start again!")
            chat_continues()
    # If user doesn't like cooking they move on to game_intro
    elif answer in no:
        print("\nThat's too bad.")
        print("\nLet's do something else now.")
        time.sleep(2)
        game_intro()
    # chat_continues is replayed in case of invalid input
    else:
        print("\nWrong answer. Try again!")
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
    # If user wants to play game
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
    # If user doesn't want to play game they can choose to have a story or not
    elif answer in no:
        print("\nOh really? I'm a bit disappointed. We can do something else.")
        time.sleep(2)
        print("\nWould you like me to tell you a story? (Y/N)\n")
        answer = input()
        answer = answer.lower()
        # If so then they move on to story_duck_language
        if answer in yes:
            story_duck_language()
        # If not, user has one last chance to change mind or else the app ends
        elif answer in no:
            print("\nHmmm. Looks like you're not in the mood for anything.")
            print("\nIn which case let's finish this at once! (Y/N)\n")
            answer = input()
            answer = answer.lower()
            if answer in no:
                print("\nGreat! Let's start again.")
                time.sleep(2)
                game_intro()
            # A polite farewell from Duck
            elif answer in yes:
                print("\nWell... It was nice meeting you.")
                time.sleep(3)
                end()
            # At this point, Duck is a bit pissed off so doens't give user
            # a chance to replay in case of invalid input and app ends
            else:
                print("\nInvalid answer. I'll take that as a no.")
                time.sleep(3)
                end()
        # See previous comment
        else:
            print("\nInvalid answer. I'll take that as a no.")
            time.sleep(3)
            end()
    else:
        print("\nTry again!")
        game_intro()


def story_duck_language():
    '''
    White Duck mistakenly tell the story in duck language but offers the
    option of telling the story in English afterwards or playing the game
    There's an option to end the game altogether if user doesn't want to
    continue
    '''
    # A relatively speaking long text with input at the end
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
    # Option to play story in English
    if answer in yes:
        story_english()
    # User is given option to change mind about playing game
    elif answer in no:
        print("\nHave you changed your mind about playing a game then?")
        time.sleep(1)
        print("(Y/N)")
        answer = input()
        answer = answer.lower()
        # If so, they go back to game_intro
        if answer in yes:
            print("\nGreat. Let's go back to the beginning!")
            time.sleep(1)
            game_intro()
        # If not, app ends
        elif answer in no:
            print("\nThen it's time to say bye!")
            time.sleep(1)
            end()
        # App ends if invalid input is given
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
    # This is basically a repetition of the previous function
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
    # Duck randomly choses from options variable
    duck_choice = random.choice(options)
    # Function to be repeated after each round

    def calculating_result():
        # This prints user's choice and Duck's choice
        print(f"\nOK. You chose {user_choice}, and I chose {duck_choice}.\n")
        time.sleep(1)
        print("\nCalculating result...")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("!")
        time.sleep(1)
    # They must play again in case of a tie
    if user_choice == duck_choice:
        calculating_result()
        print("\nOh! It's a tie! We have to play it again.")
        first_round()
    # They move on to chat_before_game in either of these scenarios:
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
    # Replay first_round in case of invalid input
    else:
        print("\nPlease type a valid option!\n")
        first_round()


def chat_before_game():
    '''
    A blurb about how the game will be played. Whoever scores 3 points
    first wins the game.
    There's an option to stop the game at any point if user wants
    '''
    # Best of 5
    print("\nWell done. Let's now play it for real.")
    print("And the winner will get a prize!")
    time.sleep(3)
    print("\nWhoever gets 3 points first wins the game!")
    time.sleep(3)
    print("\nCan I just remind you that at the end of the day")
    print("it doesn't really matter who wins or loses.")
    time.sleep(2)
    print("\nLose with dignity, in other words. *winks*")
    time.sleep(1)
    print("\n...")
    time.sleep(5)
    print("\n(If you want to end the game please type 'stop' at any time)")
    time.sleep(3)
    # Moving on to second_round
    second_round()


def second_round():
    '''
    This is the main game. There are as many rounds as needed until
    one of the players scores 3 points
    There's a score count and for each game won the player gets one point
    '''
    # Variables holding scores
    user_count = 0
    duck_count = 0
    # While loop for determining number of rounds
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
        # Tie.
        if user_choice == duck_choice:  # neither players score when they tie
            calculating_result()
            print("\nOh! It's a tie! We have to play it again.")
            # neither players score when they tie
            user_count == 0
            duck_count == 0
            # Score count is displayed after each turn
            print(f'White Duck: {duck_count} - You: {user_count}')

        elif user_choice == "rock":
            calculating_result()
            if duck_choice == "scissors":
                print("\nI lost!")
                # Score is being counted accordingly
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
        # If user wants to stop, game stops and the score is displayed
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
        # Game continues in case of invalid input, doesn't affect score count
        else:
            print("\nPlease type a valid option!\n")
            continue
        # A different function is played according to the result
        if user_count == 3:
            duck_lost()

        elif duck_count == 3:
            duck_won()
    # Score
    print(f'\nWhite Duck: {duck_count} - You: {user_count}')
    print()


def duck_won():
    '''
    Duck is a bit cheeky when he wins
    '''
    print("\nI won! No hard feelings, right? *grins*\n")
    time.sleep(3)
    duck_wins()


def duck_lost():
    '''
    Duck reacts quite badly when he loses
    '''
    # Long text
    print("\nNoooooo! I don't accept it! Aaaaaaaaaaaaaaarrrgghhh!!!!!")
    time.sleep(3)
    print("\n*White Duck trods on the computer*")
    time.sleep(2)
    print("\n*White Duck is throwing a wobbly*")
    time.sleep(2)
    print("\n*White Duck is extremely angry... He's gone red all over*")
    time.sleep(2)
    print("\n*This is not a pretty sight!*")
    time.sleep(3)
    print("\n...")
    time.sleep(3)
    # The developer interferes
    print("\nErr... Excuse me, this is the developer speaking now.")
    time.sleep(3)
    print("\nListen, I'm so sorry about White Duck's lack of sportsmanship.")
    time.sleep(2)
    print("\nCan I just suggest that you play one more round?")
    time.sleep(3)
    print("\nI know it's not fair though cause you won")
    print("and you deserve a prize but...")
    time.sleep(3)
    # User can grant White Duck another round
    print("\nWill you give White Duck another chance? (Y/N)\n")
    answer = input()
    answer = answer.lower()
    # If so then user is invited to guess if Duck wants to play again
    # Obviously it's a bit irrelevant so it's just for fun
    if answer in yes:
        print("\n*footsteps approaching*")
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
    # If not, then user can collect their prize
    elif answer in no:
        print("\nFair enough. You can claim your prize now.")
        time.sleep(3)
        # White Duck is grunting some rude noise
        print("\nQUACKQUACKQUACKQUACK ---DSIHDHS %^%$£^$(HIUIYTFCFghufyde^&%r")
        time.sleep(3)
        print("...")
        print("\nOh nevermind that noise.")
        time.sleep(3)
        prize()


def last_round():
    '''
    This code is very similat to first_round. The difference being
    that if they tie the round ends and both players must share the prize
    '''
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
        # Go to tie_prize
        tie_prize()
    elif user_choice == "rock":
        calculating_result()
        if duck_choice == "scissors":
            print("\n:(")
            # Go to duck_defeated
            duck_defeated()
        else:
            print("\nI win!")
            # Go to duck_wins
            duck_wins()
    elif user_choice == "paper":
        calculating_result()
        if duck_choice == "rock":
            print("\nOh no! I lost!")
            # Go to duck_defeated
            duck_defeated()
        else:
            print("\nI win!")
            # Go to duck_wins
            duck_wins()
    elif user_choice == "scissors":
        calculating_result()
        if duck_choice == "rock":
            print("\nI win")
            # Go to duck_wins
            duck_wins()
        else:
            print("\nI lost... :(")
            # Go to duck_defeated
            duck_defeated()
    # They play the round again in case of invalid input
    else:
        print("\nPlease type a valid option!\n")
        last_round()


def prize():
    '''
    Winner is congratulated and given a prize
    '''
    print("\nCongratulations!")
    time.sleep(2)
    print("\nHere's your special prize for winning a game of")
    print("Rock Paper Scissors!\n")
    time.sleep(2)
    print("\n*drums*")
    time.sleep(2)
    print("\n...\n")
    time.sleep(3)
    # A list with a selection of silly prizes
    prize = ["A SLICE OF CAKE!", "A RUBBER DUCK!",
             "A PAIR OF FAKE EYELASHES!", "A PINK UMBRELLA!",
             "A PAIR OF READING GLASSES!", "A RECIPE BOOK!",
             "A ROMANTIC DINNER IN A FANCY RESTAURANT!",
             "A RIDE ON A ROLLERCOASTER!"]
    # Prints a random prize from the list
    print(random.choice(prize))
    time.sleep(3)
    # Go to end
    end()


def tie_prize():
    '''
    Both players are winners. Function called from last_round
    '''
    print("\nEverybody is a winner!")
    time.sleep(1)
    print("\nYou need to share the prize though.")
    time.sleep(2)
    # Go to prize
    prize()


def duck_wins():
    '''
    Duck claims his prize
    '''
    print("\nI am here to collect my prize!")
    time.sleep(2)
    prize()


def tie():
    '''
    The user has the option to play one more round
    Function called from second_round in the event of a tie
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


# Play
main()
