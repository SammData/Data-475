#importing datetime
import datetime
this_year = datetime.datetime.now().year 

#What is your name
name = input("What is your name? ")
print("Hello " + name)

#What is your birth year
birthyear = int(input("What is your birth year? "))

#age calculation
age = this_year - birthyear
print("You must be", age, "years old")

print("Goodbye")







