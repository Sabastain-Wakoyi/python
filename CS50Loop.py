#loop is a block of code doing something again and again
# print("meow")
# print("meow")
# print("meow")
# print("meow")

#while is one keyword that can help us to programme a loop
# i = 3
# while i != 0:
#     print("meow")
#     i = i - 1

# i = 0
# while i < 3:
#     print("meow")
#     # i = i + 1
#     i += 1


#for loop
#list is a data type in python containing a list of things

# for i in [0, 1, 2]: #[] (sqaure braket represents a list of itemss)
#     print("meow")

#range is a function in python
# for i in range(3):
#     print("meow")


# use _ (under score) when you don't care about a variable blc, it will not be used in the programme
# for _ in range(3):
#     print("meow")

# print("meow\n" * 3, end="") #end="" eliminates the extra line at the end of output

#
# while True:
#     n = int(input("what's n?"))
#     if n > 0:
#         break
#
# for _ in range (n):
#     print("meow")

# def main():
#     number = get_number()
#     meow(number)
#
# def get_number():
#     while True:
#         n = int(input("what's n? "))
#         if n > 0:
#             break
#
#         return n
#
#
# def meow(n):
#     for _ in range(n):
#         print("meow")
#
# main()

# students = ["Her", "Har", "Ron"]

# print(students[0])
# print(students[1])
# print(students[2])

# for student in students:
#     print(student)


# len in python tells you the length of a list
# for i in range (len(students)):
#     print(i + 1, students[i])



# dict, stands for dictionary is associated with others , keys and values

# students = {
#     "Mbe": "Ako",
#     "Edu": "Ako",
#     "Wako": "Ako",
#     "Suh": "Berabe"
# }

# print(students["Mbe"])
# print(students["Edu"])
# print(students["Wako"])
# print(students["Suh"])

# for student in students:
#     print(student, students[student], sep=", ")

#[] indicate a list, {} indicate a dictionary
# students = [
#     {"name": "Nfor", "house": "Ndu", "title": "Shufai"},
#     {"name": "Ngala", "house": "Kungi", "title": "Nji"},
#     {"name": "Shey", "house": "Nkambe", "title": "Nwabeh"},
#     {"name": "Serkwi", "house": "Binju", "title": None}
# ]
#
# for student in students:
#     print(student["name"], student["house"], student["title"], sep=", ")



def main():
        print_square(3)

#for each row in square
def print_square(size):
        for i in range(size):
                print(size)
                #for each brick in row
                # for j in range(size):
                        #print brick
                        # print("#", end="")
                print()

#         print_row(4)
# def print_row(width):
#         print("?" * width)

#         print_column(3)
#
# def print_column(height):
#         print("#\n" * height, end="")

main()
