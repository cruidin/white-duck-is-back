# White Duck Is Back

[WHITE DUCK](/assets/images/white-duck-glasses2.png)

## Table of contents

1. [Introduction](#introduction)
1. [Features](#features)
    * [Technical Features](#technical-features)
    * [Content Features](#content-features)	
    * [Future Features](#future-features)
1. [Testing](#testing)
    * [Validator](#validator)
    * [Bugs](#bugs)
1. [Deployment](#deployment)
1. [Credits](#credits)
    * [Websites Consulted](#websites-consulted)
1. [Final Comments](#final-comments)
1. [Acknowledgements](#acknowledgements)
1. [About](#about)


## Introduction </a>

The character White Duck is back for another adventure but this time in a Python program. White Duck wants to have a little chat and play a game of Rock, Paper, Scissors. The format is of an interactive story where the user will be able to add some input as the story develops accordingly. 

I created this character for my last portolio project on JavaScript and decided to develop it further for my Python project.

[Back to the top](#white-duck-is-back)

## Features

[Am I Responsive?](/assets/images/amiresponsive_wdib.png)

`intro()`:

This is the introduction. White Duck is beginning to talk and asks the user's name.

`chat()`:

There are two main chat functions. This is the first part

`chat_continues()`: 

A rather random chat continues if user choses to do so

`game_intro()`:

White Duck proposes a game of Rock Paper Scissors and offers alternatives if user doesn't want to play game. If user wants to play, he explains the rules
There's an option to end the game altogether if user doesn't want to continue

`story_duck_language()`:

White Duck mistakenly tell the story in duck language but offers the option of telling the story in English afterwards or playing the game
There's an option to end the game altogether if user doesn't want to continue

`story_english()`:

White Duck tells the story in English and asks if user has changed their mind about playing the game
There's an option to end the game altogether if user doesn't want to continue

`first_round()`:

This is when the first round starts
It's just a trial to get used to playing the Rock Paper Scissors game

`calculating_result()`:

Function inside games functions

`chat_before_game()`:

A blurb about how the game will be played. Whoever scores 3 pointsfirst wins the game.
There's an option to stop the game at any point if user wants

`second_round()`:

This is the main game. There are as many rounds as needed until one of the players scores 3 points
There's a score count and for each game won the player gets one point

`duck_won()`:

Duck is a bit cheeky when he wins

`duck_lost()`:

### Technical Features

The project is written in Python (version 3.8.11).

Topics covered:

Time module

Random module

Lists

Functions

Loops

If/elif/else statements

Built in functions: input(), print()

Score count

Handling incorrect input

.lower

.capitalize


### Content Features

This is a narrative based app in which a character called White Duck interacts with the user. The Duck talks a lot before he suggests they play a game of Rock, Paper, Scissors. I tried to make it humorous and slightly nonsensical because that’s how the style I use when working on my art creations. Obviously, my main objective is to learn and apply my technical programming skills but to me this is also an opportunity to combine my own art work with coding which is kind of the point of why I’m learning to program. 

### Future Features:

There's scope for developing this project further by adding more scenarios and options of different paths and games. 
There's also the potential to explore more features and libraries to add more sophistication to the app.
Also, I believe the code can be simplified further and be made more efficient.
On a non technical note, there’s obviously room for improvement in the content and flow of story being told as the game evolves.  

    
[Back to the top](#white-duck-is-back)

## Testing

I constantly tested my code. While testing, here are some of the issues I encountered:

*The score in the function `second_round()` kept on resetting.*

I had this issue at different stages of my coding. Initially, I didn’t know how to set up the score count. Because of it I wasn’t going to include a score count but my mentor advised me to do it. When I got it set up it didn’t work well because the score was resetting each time a new round was being played. I also had to handle the issue of the number of rounds that were to be played. This was tricky to solve because it was easy to just leave it open to unlimited rounds and up to the user to stop the game at their wish. But that makes it too obvious to the user so a limit of scores was crucial.

*Handling invalid input*

It was pretty straight forward to find a solution for handling invalid inputs in yes/no situations. However, when it came to the game functions `first_round()`, `second_round()` and `last_round()`, things were less obvious. The way I had my code structured, especially in the case of the `second_round()` function in which there’s a little more complexity due to the score count and a limited number of rounds, made it tricky to add a simple 'invalid input' message and a rerun of the code. The solution for my problem in the `second_round()` function was to insert a `continue` statement inside the `else` statement in the `while` loop. Without the `continue` statement, everytime the user inserted an invalid input the score count was reset. For the other two functions there was no requirement to use the `continue` statement because the score is not being counted so a simple return to the beginning would sufice. The only difficulty was in regards to displaying the order in which the lines were being printed. For that reason, I had to add a `calculating_result()` function and insert it inside each `if`/`elif` statements to avoid an incorrect display of the text.  

*Input function*

When I started coding for this project, I initially used the `input()` function with the text inside it. While running the code in Gitpod, this method of displaying did not present any problems but once I deployed my app to Heroku I could see that this was problematic because the app was displaying the input prompt before the question. I fixed it by removing the text from the `input()` and using the `print()` function for that purpose.

*Missing code on Gitpod*

This is not technically a testing issue but while doing one of the last tests before submitting this project, I noticed that the `second_round()` function wans't running properly because the part of the code responsible for limiting the score to 3 was missing. This was possibly due to a problem I had with Gitpod in which a considerable part of my code had gone missing. Happily, I had pushed my code to Github earlier on so it looks like I was able to retrieve most of my most up to date work. As advised by Jim Morel on a Gitpod post on Slack (seems like I’m not the first person affected by this problem), I started a new workspace. Unfortunately, the new workspace also had a problem so I had to start a third one. Anyway, it's possible that the disappearance of that part of the code was caused by the confusion of having to deal with this problem.

### Validator

Passed the pep8online validator

### Bugs

*expected two blank lines pep8*

*UnboundLocalError: local variable referenced before assignment*

*E501 line too long*

*continuation line under-indented for visual indent*

*Exception has occurred: EOFError*


[Back to the top](#white-duck-is-back)

## Deployment </a>

Heroku

The deployment set up occurred smoothly without any problems or errors although it did take some time for the app to become available at Heroku.

I regret not having deployed my app at the time I started working on my project but I still deployed it in time to adjust my code to the Heroku platform. 

The link to the deployed app can be found [here](https://white-duck-is-back.herokuapp.com/).

[Back to the top](#white-duck-is-back)


## Credits


### Websites Consulted

* [W3Schools](https://www.w3schools.com/)
* [Pep8online Validator](http://pep8online.com/)
* [Replit](https://replit.com/)
* [Heroes Academy](https://intropython-fall2016.readthedocs.io/en/latest/tutorials/index.html)
* [Stack Abuse](https://stackabuse.com/getting-user-input-in-python/)
* [Ask Python](https://www.askpython.com/python/text-based-adventure-game)
* [Making an Adventure Game in Python - Leon Marsden](https://www.youtube.com/watch?v=EbAdsK8s0-U)
* [Break, Continue, and Pass Statements - Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3)
* [Real Python](https://realpython.com/python-rock-paper-scissors/)
* [The Coding Pie](https://thecodingpie.com/post/make-your-own-text-based-adventure-game-in-python3)
* [Diffchecker](https://www.diffchecker.com/diff)
* [CI - README template](https://github.com/Code-Institute-Solutions/readme-template)
* [Programiz](https://www.programiz.com/python-programming/modules)
* [Stack Overflow](http://stackoverflow.com)
* [Replit](https://replit.com/)

*Note:* Even though the best efforts have been made to acknowledge all the websites, articles and codes used for this project, it is possible that some of them haven't been listed here. If that is the case, I sincerely apologise. 

[Back to the top](#white-duck-is-back)

## Final Comments

Overall, I enjoyed working on this project. Unlike the drama and the trauma that my JavaScript project inflicted on me (lol), I was able to stay more focused and calm for most of the time. That's not to say though that this project wasn't challenging.

Initially, I realised that, due to the more abstract nature of the command line, I needed to rethink how to approach it. I spent some time exploring and learning about the Python `turtle` Library and I entertained the idea of doing my project with it. I eventually settled for an interactive story with a game of Rock, Paper, Scissors.

I want to take the opportunity here to say that things only started making sense when I started my project. It seems to me that the best way for me to learn is by blindingly diving into a completely new language and then figuring out how to navigate through it as opposed to the more classic way of learning the theory then applying it afterwards. So I took the more unorthodox approach here and it worked - I’m not saying that my project is brilliant but rather just stating that I actually learned an awful lot by doing it the way I did and I understand now every single thing that I did here which is great.

[Back to the top](#white-duck-is-back)

## Acknowledgements

I would like to thank:
* My mentor, Seun, for her help and invaluable insights
* My children, for giving me some space to work on this project

[Back to the top](#white-duck-is-back)

## About

My name is Patricia Melo. I am an artist and I am a Software Development student at the Code Institute. You can contact me by [email](mailto:contact@patriciamelo.ie).

*******

[Back to the top](#white-duck-is-back)

