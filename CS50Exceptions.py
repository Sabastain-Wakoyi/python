#SyntaxError must be solved by the developer
#run time erros occur while your code is running

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

#ValueError, an due to no abiding to data type

#NameError,In Python, a NameError occurs when you try to use a variable
# or a function name that hasn't been defined or is not accessible within the current scope.
# It means that Python cannot find the reference to the name you are trying to use.

# def main():
#     x = get_int()
#     print(f"x is {x}")


# def get_int():
#     while True:
#         try:
#             return int(input("what's x? "))
          #  x = int(input("What's x? "))

        # except ValueError:
        #     print("x is not an integer")

        #else:
           # return x
            #break
    # return x

#main()


#pass

def main():
    x = get_int("what's x? ")
    print(f"x is {x}")
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            pass
main()

# raise, you can use the keyword raise  to raise your exceptions

