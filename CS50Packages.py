#pypi.org
#pypi.org/project/cowsay
#pip use in installing packages

# import cowsay
# import sys
# 
# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])
#     cowsay.trex("hello, " + sys.argv[1])


import cowsay

name = input("Enter a name: ")

if name:
    cowsay.cow("hello, " + name)


