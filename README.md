
# self-introduction-in-python-


print("Hello, Python!")
print("My name is *****.")
print("I am learning Python.")
print("My goal is to become a good programmer.")
print("My hobby is to innovate new projects in python.")

#using variables in python 

name = "Erum"
age = 16
course = "Python"
favorite coding= "Python."

print(name)
print(age)
print(course)
print(favorite coding)


#input + calculation 


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

#basic calculator 

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#if else 

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

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

#cconditions and loops 
#greater calculator 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
elif b > a:
    print(b, "is greater")
else:
    print("Both are equal")