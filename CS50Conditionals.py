# >, greater than sign
# >= greater than or equal to
# < less than
# <= less than or equal to
# == represents equality comparing the left and the right
# != not equal to

# if condition
# x = int(input("What's x? "))
# y = int(input("What's y? "))
#
# if x < y:
#     print("x is less than y") #line 12 should only be executed if line 11 is true. A Boolean situation here
#
# if x > y:
#     print("x is greater than y")
#
# if x == y:
#     print("x is equal to y")


# elif (else if) condition
# x = int(input("What's x? "))
# y = int(input("What's y? "))
#
# if x < y:
#     print("x is less than y")
#
# elif x > y:
#     print("x is greater than y")
#
# elif x == y:
#     print("x is equal to y")


# else condition

# x = int(input("What's x? "))
# y = int(input("What's y? "))
#
# if x < y:
#     print("x is less than y")
#
# elif x > y:
#     print("x is greater than y")
#
# else:
#     print("x is equal to y")

# or condition
# x = int(input("What's x? "))
# y = int(input("What's y? "))
#
# if x < y or x > y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")
#
# x = int(input("What's x? "))
# y = int(input("What's y? "))
#
# if x != y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")


# and
# score = int(input("Score"))
# if score >= 90 and score <= 100:
#     print("Grade: A")
# elif score >= 80 and score < 90:
#     print("Grade: B")
# elif score >= 70 and score <80:
#     print("Grade: C")
# elif score >= 60 and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")


# score = int(input("Score: "))
#
# if 90 <= score and score <= 100:
#     print("Grade: A")
# elif 80 <= score and score < 90:
#     print("Grade: B")
# elif 70 <= score and score <80:
#     print("Grade: C")
# elif 60 <= score and score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")


# score = int(input("Score: "))
#
# if 90 <= score <= 100:
#     print("Grade: A")
# elif 80 <= score < 90:
#     print("Grade: B")
# elif 70 <= score <80:
#     print("Grade: C")
# elif 60 <= score < 70:
#     print("Grade: D")
# else:
#     print("Grade: F")



# score = int(input("Score: "))
#
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 60:
#     print("Grade: D")
# else:
#     print("Grade: F")

#parity

# +
# -
# *
# /
# %

# x = int(input("what's x? "))
#
# if x % 2 == 0:
#     print("Even")
# else:
#     print("odd")




# def main():
#     x = int(input("what's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("odd")
#
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
#
# main()

#simplified way of solving the above problem
# def main():
#     x = int(input("what's x? "))
#     if is_even(x):
#         print("Even")
#     else:
#         print("odd")
#
# def is_even(n):
#         #return True if n % 2 == 0 else False
#         return n % 2 == 0
#
# main()


#match

# name = input("what's your name? ")
# if name == "Harry":
#     print("Gry")
# elif name == "Hermione":
#     print("Gry")
# elif name == "Draco":
#     print("Sly")
# else:
#     print("Who? ")

#simplified version of the above
# name = input("what's your name? ")
# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gry")
# elif name == "Draco":
#     print("Sly")
# else:
#     print("Who? ")


#using the keyword match
#python 3.8 does not support match
name = input("what's your name? ")

#match name:
    # case "Harry":
    #     print("Gry")
    # case "Hermione":
    #     print("Gry")
    # case "Ron":
    #     print("Gry")
    # case "Draco":
    #     print("Sly")

match name:
    case "Harry" | "Her" | "Ron":
                print("Gry")
    case "Draco":
        print("Sly")
    case _:
        print("Who")

