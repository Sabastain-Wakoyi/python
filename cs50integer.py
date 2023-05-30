# x = input("what's x? ")
# y = input("what's y? ")
# z = int(x) + int(y)
# print(z)

#nested functions
# x = int(input("what's x?"))
# y = int(input("what's y?"))
# print(x + y)

#float allow for decimal points

# x = float(input("what's x?"))
# y = float(input("what's y?"))
# print(x + y)

#round, rounds the number up to the nearest integer
#round(number[, ndigits])

# x = float(input("what's x?"))
# y = float(input("what's y?"))
# z = round(x + y)
# print(f"{z:,}") # :, output a value separated by the , (command)


x = float(input("what's x?"))
y = float(input("what's y?"))
# z = round(x/y, 2) # rounds the answer to two decimal places
# print(z)

z = x/y
print(f"{z:.2f}") # rounds the answer to two decimal places as well