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
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")
#print name tags
print("hello, my name is", sys.argv[1])