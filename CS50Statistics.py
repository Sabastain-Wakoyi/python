# import statistics
#
# print(statistics.mean([100, 90]))

#command-line argument

import sys

#execution with the trying method

# try:
#     print("Hello, my name is", sys.argv[1])
#
# except IndexError:
#     print("Too few arguments")


#check for errors
# #sys.exit, exit at the line it's implemented
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")
#print name tags
#slice, it's a subset of a list
# for arg in sys.argv[1: ]:
#     print("hello, my name is", sys.argv[1])



import sys


name = input("Enter a name: ")

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", name)


