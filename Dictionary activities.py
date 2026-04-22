# Activity 1
student = {
    "name": "Rocelyn",
    "age": 20,
    "course": "IT"
}

print(student["name"])  # Output: Rocelyn


# Activity 2
student = {"name": "Rocelyn", "age": 22}

student["grade"] = 95   # add
student["age"] = 22     # update (same pa rin since 22 ka na)

print(student)


# Activity 3
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}

for key, value in car.items():
    print(key, ":", value)


# Activity 4 (Mini Phonebook)
phonebook = {
    "Riana": "09123456789",
    "Jaharra": "09234567890",
    "Cedrick": "09345678901",
    "John": "09456789012"
}

name = input("Enter a name: ")

if name in phonebook:
    print("Phone number:", phonebook[name])
else:
    print("Name not found.")