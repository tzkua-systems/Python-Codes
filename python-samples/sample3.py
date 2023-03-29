# Looping
i = 1
while i <= 10:
    print(i)
    i += 2

print("End of Loop")

# WhileLoop
secret = "tzkua"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Game Over, You Lose!")
else:
    print("Voila, You win!")

#

secret_number = 12
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("You lost!")


# ForLoop
for letter in "Tobi Taiwo":
    print(letter)

siblings = ["Seyi", "Dare", "Tobi"]
for name in siblings:
    print(name)
for index in range(len(siblings)):  #same as above
    print(siblings[index])

numbers = [0, 2, 4, 6, 8]
for digit in numbers:
    print(digit)

for index in range(1, 10, 2):
    print(index)

# way1
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        #result = result * base_num
        result *= base_num
    return result

print("Answer is:", raise_to_power(2, 3))

#way2 with Exception
try:
    def power_function():
        num1 = float(input("Enter base number: "))
        num2 = float(input("Enter power number: "))
        result = num1 ** num2
        return result

    print(power_function())
except ValueError:
    print("Invalid Input")

#whileloop
i = 1
while i <= 5:
    print("Tobi ", end="") #don't start print on new line
    j = 1
    while j <= 4:
        print("Taiwo ", end="") #don't start print on new line
        j = j+1

    i = i+1
    print() #start print on new line

#translate
def translate(phrase):
    translation = ""
    for letter in phrase:
        #if letter in "AEIOUaeiou":
        if letter.lower() in "aeiou":
            if letter.isupper():
                #translation = translation + "G"
                translation += "G"
            else:
                #translation = translation + "g"
                translation += "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

####################################################

#remove duplicate in list

numbers1 = [2, 2, 4, 6, 3, 4, 6, 1]
numbers2 = []
for number in numbers1:
    if number not in numbers2:
        numbers2.append(number)
print(numbers2)

###################################################

# Dictionary

file_counts = {
    "jpg": 10,
    "csv": 7,
    "txt": 5,
    "py": 3,
}

print(file_counts.keys())
print(file_counts.values())

for key in file_counts.keys():
    print(key)
for value in file_counts.values():
    print(value)

for keys, values in file_counts.items():
    print(f"There are {values} number of files with the .{keys} extensions")

###

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("dictionary"))
print(count_letters("This is a very long string with a lot of letters"))

###################################################

class Piglet:
    name = "name"
    def speak(self):
        return f"Oink! I'm {self.name}, Oink!"

hamlet = Piglet()
hamlet.name = "Hamlet"
print(hamlet.speak())

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return f"hi, my name is {self.name}"

# Create a new instance with a name of your choice
person1 = Person('Tobi')
person2 = Person('Martha')
# Call the greeting method
print(person1.greeting())
print(person2.greeting())

########################################

class FunEvent:
    def __init__(self, tags, year):
        self.tags = tags
        self.year = year

    def __str__(self):
        return f"FunEvent(tags={self.tags}, year={self.year})"


tags = ["google", "ml"]
year = 2022
bootcamp = FunEvent(tags, year)
tags.append("bootcamp")
year = 2023
print(bootcamp)

############################################

class BaseLayer:
    def __init__(self, name=""):
        self.name = name

    def __repr__(self):
        return f"{self.name}Layer"


class ActionLayer(BaseLayer):
    def __init__(self, size):
        super().__init__("Activation")
        self.size = size


class FCLayer(BaseLayer):
    def __init__(self, size):
        super().__init__("FullyConnected")
        self.size = size

print(FCLayer(42))
print(ActionLayer(26))
print(BaseLayer())

###############################################


