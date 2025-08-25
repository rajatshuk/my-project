print("Hello, World!")
print("*" * 20)
2 + 3
x = 1
students_count = 1000
print(students_count)
course_name = "Python Programming"
print(course_name)
course = "Python's Course for Beginners"
print(course)
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:5])
print(course[:])
first = "Rajat"
last = "Shukla"
full = first + " " + last
print(full)
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("yth"))
print(course.replace("Beginners", "Absolute Beginners"))
print("Python" in course)
print(10 + 3)
print(round(2.9))
x = input("x: ")
y = int(x) + 1
print(y)
print(type(x))
print(bool("False"))
print("bag" == "bag")
print("bag" > "apple")
temperature = 15
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
else:
    print("It's not a hot day")

age = 22
if age >= 18:
    print("You are eligible to vote ")
else:
    print("You are not eligible to vote ")

# age should be between 18 and 65 to work
age = 22
if age >= 18 and age < 65:
    print("Eligible")

# quiz
if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")

for number in range(3):
    print("Attempt", number)

# nested loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

for item in ["a", "b", "c"]:
    print(item)

for char in "hello":
    print(char)

# while loop
number = 100
while number > 0:
    print(number)
    number = number // 2

# ---------------
command = ""
while command != "quit":
    command = input(">")
    print("ECHO", command)

# ---------------
# print even number between 1 to 10
count = 0
for number in range(1, 11):
    if number % 2 == 0:
        print(number)
        count = count + 1
    else:
        print(f"Odd number: {number}")

print(f"Count is {count}")

# --------Functions-----------


def greet():
    print("Hi there")
    print("Welcome aboard")


greet()


def greet1(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet1("Rajat", "Shukla")
