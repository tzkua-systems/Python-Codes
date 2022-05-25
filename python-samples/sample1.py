# import this
phrase = "TZKUA Systems Limited"
print(phrase)
print(phrase.islower())
print(phrase[4])
print(phrase.replace("Systems", "Limited"))

number = 5
print(str(number) + " is my number")
print(type(phrase))

# from math import *
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, " + name + " is my name" + " & I am " + age + " years old!")

print("Tobi\'s d \"Taiwo\" Laptop")
# print("Tobi's d "Taiwo" Laptop")
print(r'c:\docs\tobi')

# Calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
# result = int(num1) + int(num2)
result = float(num1) + float(num2)
print(result)

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
fwends = ["Patience", "Peter", "Mary", "Martha"]
values = [2, 4, 6, 8]
values.insert(0, 1)
values.extend([3, 5, 7, 9])
valuable_fwends = (fwends + values)
print(valuable_fwends)
print(sum(values))
enemies = fwends.copy()
print(enemies)

a=5
b=6
#swap the two numbers
a,b = b,a
print(a)
print(b)

x = int(input("Enter 1st value: "))
y = int(input("Enter 2nd value: "))
z = (x + y)
print(z)

ch = input("Enter a char: ")[0]
print(ch)

result = eval(input('enter an expr: '))
print(result)


number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])
for row in number_grid:
    for col in row:
        print(col)

#############################################
