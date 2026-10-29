8772#input and calculation 


name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = 2026
age = current_year - birth_year

print(name, "is", age, "years old.")


#strings 

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

full_name = first_name + " " + last_name

print("Full name:", full_name)
print("Length:", len(full_name))

#if else 
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#basic calculator 
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


#mini calculator
a = float(input("Enter first number: "))
operator = input("Enter +, -, *, or /: ")
b = float(input("Enter second number: "))

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "/":
    print(a / b)
else:
    print("Invalid operator")
# greater number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both are equal")

#conditions and loops 
#greater calculator 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both are equal")

#countdown 

number = int(input("Enter starting number: "))

while number >= 0:
    print(number)
    number -= 1

print("Done!")

#Remove duplicates 

numbers = [1, 2, 2, 3, 4, 4, 5, 5]

unique_numbers = set(numbers)

print(unique_numbers)

#return values 
def square(number):
    return number * number

number = int(input("Enter a number: "))

result = square(number)

print("Square:", result)

#Random number generator 
import random

number = random.randint(1, 100)

print("Random number:", number)

#Error handling 

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print("Result:", a / b)

except ZeroDivisionError:
    print("You cannot divide by zero.")

except ValueError:
    print("Please enter numbers only.")

#student records 

students = []

for i in range(3):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    students.append({
        "name": name,
        "marks": marks
    })

print("\nStudent Records:")

for student in students:
    print(student["name"], "-", student["marks"])