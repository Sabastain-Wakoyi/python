# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")
#
#

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")
#


# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {name}")
#
# for students in sorted(students):
#     print(students)

#
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
# student = {}
# student["name"] = name
# student["house"] = house
# students.append(student)


# def get_name(student):
#     return student["name"]
#
#
# for student in sorted(students, key=get_name, reverse=True):
#     print(f"{student['name']} is in {student['house']}")


# using lambda


# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
#
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")


# import csv
#
# students = []
#
# with open("students.csv") as file:
#     # = csv.reader(file)
#     reader = csv.DictReader(file)
#     for row in reader:
#         # students.append({"name": row[0], "house": row[1]})
#         students.append({"name": row["name"], "house": row["house"]})
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")

import csv

name = input("what's your name? ")
house = input("what's your house? ")


with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, house])