#Looping
i = 1
while i <= 10:
    print(i)
    i += 2

print("End of Loop")

#WhileLoop
secret = "tzkua"
guess = ""
guess_count = 0
guess_limit = 3
out_of_quesses = False

while guess != secret and not(out_of_quesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_quesses = True

if out_of_quesses:
    print("Game Over, You Lose!")
else:
    print("Voila, You win!")

#ForLoop
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

#way1
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
