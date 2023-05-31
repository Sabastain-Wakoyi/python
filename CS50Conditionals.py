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


score = int(input("Score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score <80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")