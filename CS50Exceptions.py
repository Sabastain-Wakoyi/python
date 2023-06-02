#SyntaxError must be solved by the developer
#run time erros occur while your code is running

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

#ValueError, an due to no abiding to data type

#NameError,