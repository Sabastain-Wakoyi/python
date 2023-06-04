# modules are code written for reusebility

# random
# import allow you to import the content from the library or module.
# from is a keyword in python allowing you to import

# import random

#random.choice, allows you to make a choice between two things
from random import choice # this is specific with the usage of the keyword from

#coin = random.choice(["heads", "tails"])
coin = choice(["heads", "tails"])
print(coin)


#random.randint
#random.randint(a,b) takes 1 to 10

import random

number = random.randint(1,10)
print(number)

#random.shuffle(x) allows you get a list and shuffle it

import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)