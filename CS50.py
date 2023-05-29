# functions are actions or verbs that let you do something in the programme
# the print function, prints what you want it to do
# arguments are inputs into functions that influence the function behavior
# functions have side effects, i.e those actions they display, be it text or visual
# bugs are problems or mistakes in a code

# function
# print("hello, world")


#input
# input("what's your name? ")
# print("Hello, David")
#return values are the values you get back from your variable

# variable is a container for values in programming which are used to hold values of text, images or videos
#Ask user for their name
name = input("what's your name? ")

#Say hello to user
# print("Hello")
# print(name)
#print("Hello, " + name) # this is one function
print("Hello,", name) # this takes multiple arguments

#comments are notes for the programmer or other programmers
#Comments can form a to do list for you
#pesudocode allows you to outline your program  algorithmatically or logically

#str is short form of string. It's use in converting integres to strings
#docs.python.org, official python documentation
#print(*objects, sep=' ', end='\n', file=None, flush=False)
#*objects means the function can take any number of arguments
#sep='', sep means separator
#end='\n', the \n tells the computer to move to a new line


#parameters are variables or placeholders defined in the function or method declaration
# that represent the values or data that a function expects to receive when it is called or invoked
#arguments are the values that are passed to a function or method when it is called or invoke.
#functions take arguments which implement their behaviours

name = input("What's your name? ")
print("hello, ", end="")
print(name)
print("hello,", name, sep="???")