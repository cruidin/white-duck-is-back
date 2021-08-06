import time
import random

# Intro
print("Guess who's back?")

print("...")
time.sleep(2)
print("It's White Duck!")
time.sleep(3)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)

# Instructions

# Start

answer = input("Oh, hello there! Nice to meet you! Or have we met before? (Y/N) ")

silly_names = ["Bibo Holiday!", "Catacata Plum!", "Carrot Bunch III!", "Pot Pot Mc Pot!", "Porcini Bambini!"]

if answer.capitalize() == "Y":
    print("Oh that’s right! I remember you now. But what’s your name again? Wait, don’t tell me! It starts with…")
    time.sleep(5)
    print("It's... ")
    time.sleep(2)
    print(random.choice(silly_names))
    answer = input("Oh, did I get it wrong? (Y/N)")


if answer.capitalize() == "N":
    print("Let me introduce myself then. I’m White Duck!")
    name = input("What’s your name? ")

else:
    print("C'mon! That was a simple question that required a simple answer!") 
    answer = input("please just say Y or N")