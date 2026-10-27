#Greetings 

print("Hello, Python!")
print("My name is *****.")
print("I am learning Python.")
print("My goal is to become a good programmer.")
print("My hobby is to innovate different projects in python.")

#write to a file 

note = input("Write your note: ")

with open("notes.txt", "w") as file:
    file.write(note)

print("Note saved!")