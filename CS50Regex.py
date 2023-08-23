# Regexes stands for regular expressions.
# Regular expressions are used in matching pattern

#
# email = input("what's your email").strip()
#
# if "@" in email and "." in email:
#     print("valid")
#
# else:
#     print("Invalid")


email = input("what's your email? ").strip()

username, domain = email.split("@")

if username:
    print("Valid")

else:
    print("Invalid")