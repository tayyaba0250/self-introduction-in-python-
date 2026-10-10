# everything in python 

name = "xxxxxx"
age = 16
course = "Python"
favorite coding= "python."
 
print(name)
print(age)
print(course)
print (favorite coding)ß

#login checker 

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    


# multiplication table
number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)

#number guessing game 

import random

secret = random.randint(1, 10)

guess = int(input("Guess a number from 1 to 10: "))

if guess == secret:
    print("Correct!")
else:
    print("Wrong!")
    print("The number was", secret)
