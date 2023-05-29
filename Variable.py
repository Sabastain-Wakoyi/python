# variable, a variable is a container for a value, it holds a value

#string data type variable

f_name = "Evi"
l_name = "Je"
full_name = l_name + " " + f_name

print("Good morning" + " " + full_name)
print(" Hello " + f_name)
print(type(f_name)) #this prints the data type in python

#int data type variable
age = 21
age = age + 2
# age += 1 as the next line above
print(age)
print(type(age)) #this prints the data type in python
print("Your age is " + str(age)) # this converts an int type into a string type

#float data type

height = 250.5
print(height)
print(type(height))
print("Your height is: " + str(height) +"cm")


#boolean, true or false
human = True
print(human)
print(type(human))
print("Are you a human: "+str(human))

print("hello, world")