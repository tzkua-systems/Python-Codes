# import this
phrase = "TZKUA Systems Limited"
print(phrase)
print(phrase.islower())
print(phrase[:4].isupper())  # checks if the first word is upper case
print(phrase[4])
print(phrase.replace("Systems", "Concepts"))  # this replaces 'Systems' with 'Concepts'
print(type(phrase))

number = 5
print(str(number) + " is my number")

# from math import *
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, " + name + " is my name" + " & I am " + age + " years old!")  # concatenation
print(f'Hello, {name} is my name & I am {age} years old!')

print("Tobi\'s d \"Taiwo\" Laptop")  # \ will ignore the apostrophe immediately after
# print("Tobi's d "Taiwo" Laptop")
print(r'c:\docs\tobi')  # print as a raw value

# Calculator
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
result1 = int(num1) + int(num2)
result2 = float(num1) + float(num2)
print(result1)
print(result2)

# madlib games
colour = input("Enter a colour: ")
noun = input("Enter a noun: ")
name = input("Enter a name: ")
print("Roses are " + colour)
print(noun + " are cool")
print("I love " + name)

# Lists
friends = ["Peter", "Patience", "Mary", "Martha"]
figures = [2, 4, 6, 8]
print(friends + figures)

# Lists
family = ["Patience", "Peter", "Mary", "Martha"]
values = [2, 4, 6, 8]
values.insert(0, 1)  # this adds number 1 to values list at index 0
values.extend([3, 5, 7, 9])  # this extends the list from last index by new list values
valuable_family = (family + values)
print(valuable_family)
print(sum(values))
enemies = family.copy()  # this copies the elements in family ans assign to enemies
print(enemies)

# swap the two numbers
a = 5
b = 6
a, b = b, a
print(a)
print(b)

x = int(input("Enter 1st value: "))
y = int(input("Enter 2nd value: "))
z = (x + y)
print(z)

ch = input("Enter a char: ")[0]  # ch = input("Enter a char: ")
print(ch)  # print(ch[0])

result = eval(input('Enter an expr: '))  # mathematical expression e.g. 1 + 2
print(result)


number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])  # print element at index 0 of column & index 0 of row

for row in number_grid:
    for col in row:
        print(col)

#############################################
