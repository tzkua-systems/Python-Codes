# this is a test program
print('Hello, World!')
print('This is my first program')

# strings
word1 = "Hello,"
word2 = "World!"
word3 = "Good Morning!"
word4 = "This is gonna be a great day."
word5 = "You are welcome."
sentence = word3 + " " + word4 + " " + word5
print(sentence)
print(word1, word2)
# methods . . . plus boolean
print(word4.islower())
print(word4.title())

word6 = "Tobi"
print(word6 * 5)
# length
print("lenght of word6 is:", len(word6))
# type
print("word6 class type is:", type(word6))

# add integer & string
number = 7
street = "Uncle Oluyeba Street"
area = "Ikosi-Ketu"
# print(type(number))
address = str(number) + ", " + street + ", " + area
print(address)
print("word1 id number is:", id(word1))
print("word2 id number is:", id(word2))

print("the number type is:", type(number))
convert = float(number)
print("number is converted to float:", convert)

import math  # import math as m

x = math.sqrt(25)  # x = m.sqrt(25)
print(x)
print(math.floor(2.9))  # round figure down
print(math.ceil(2.2))  # round figure up


###############################################################
def month_days(month, days):
    print(month + " has " + str(days) + " days ")

month_days("June", 30)
month_days("July", 31)
