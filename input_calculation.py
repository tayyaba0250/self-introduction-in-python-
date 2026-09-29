#input and calculation 


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