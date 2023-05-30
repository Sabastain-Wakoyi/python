# the keyword def let's you define your own function or innovate your own function
# def hello(to="world"): # def defines the function hello, while : let python know that everything under the indentention is under the function hello
#     print("hello,", to)
#
# hello()
# name = input("what's your name? ")
# hello(name)



# def main():
#     name = input("what's your name? ")
#     hello(name)
#
# def hello(to="world"):
#     print("hello,", to)
#
# main()

#scope refers to the context a variable exist in the context you defined it
#return the function returns a value that was pass into it


def main():
    x = int(input("what's x? "))
    print("x squared is", square(x))

def square(n):
    #return n*n
    #return n** 2 raise the value to the power 2
    return pow(n, 2)

main()