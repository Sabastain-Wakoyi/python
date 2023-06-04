# modules are code written for reusebility

# random
# import allow you to import the content from the library or module.
# from is a keyword in python allowing you to import

# import random

from random import choice # this is specific with the usage of the keyword from

#coin = random.choice(["heads", "tails"])
coin = choice(["heads", "tails"])
print(coin)


#random.randint
#random.randint(a,b)

import random

number = random.randint(1,10)
print(number)