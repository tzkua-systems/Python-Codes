# Write a python program that takes a number from the user
# and prints the divisors of that number
# and then prints how many divisors were there

n = int(input("Enter the number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
        print(i, end=",")
print("\n")
print("Total", count, "divisor")

###################################################3

# Use nested for loop to display each of the 3 groups of ash symbol patterns:
# # # #     # # # #     #
# # # #     # # #       # #
# # # #     # #         # # #
# # # #     #           # # # #

print("\n")
for i in range(4):
    for j in range(4):
        print("#", end="")
    print()

print("\n")
for i in range(4):
    for j in range(4 - i):
        print("#", end="")

    print()

print("\n")
for i in range(4):
    for j in range(i + 1):
        print("#", end="")

    print()

################################################

print("\n")
available = 5
count = int(input("Number of Candies: "))
order = 1
while order <= count:
    if order > available:
        print("Out of Stock")
        break

    print("Candy")
    order += 1

print("Bye")

print("\n")
for i in range(1, 20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

print("Bye")

print("\n")
for i in range(1, 20):
    if i % 2 != 0:
        pass
    else:
        print(i)

print("Bye")


###############################################
def factorial(n):
    result = 1
    for i in range(1, n):
        result += result * i
    return result


print(factorial(4))  # should return 24
print(factorial(5))  # should return 120


# Make the factorial function return the factorial of n.
# Then, print the first 10 factorials (from 0 to 9) with the corresponding number

def factorial(n):
    result = 1
    for x in range(1, n):
        result = result * x
    return result


for n in range(0, 9):
    print(n, factorial(n + 1))


###############################################

# Design a parking system for a parking lot.
# The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

# Implement the ParkingSystem class:
# ParkingSystem(int big, int medium, int small) Initializes object of the ParkingSystem class. The number of slots for each parking space are given as part of the constructor.
# bool addCar(int carType) Checks whether there is a parking space of carType for the car that wants to get into the parking lot.
# carType can be of three kinds: big, medium, or small, which are represented by 1, 2, and 3 respectively. A car can only park in a parking space of its carType.
# If there is no space available, return false, else park the car in that size space and return true.


# Example 1:
# Input
# ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
# [[1, 1, 0], [1], [2], [3], [1]]
# Output
# [null, true, true, false, false]

# Explanation
# ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
# parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
# parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
# parkingSystem.addCar(3); // return false because there is no available slot for a small car
# parkingSystem.addCar(1); // return false because there is no available slot for a big car. It is already occupied.

# Constraints:
# 0 <= big, medium, small <= 1000
# carType is 1, 2, or 3
# At most 1000 calls will be made to addCar


class ParkingSystem:
    def _init_(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big == 0 or carType == 2 and self.medium == 0 or carType == 3 and self.small == 0:
            return False
        elif carType == 1:
            self.big -= 1
        elif carType == 2:
            self.medium -= 1
        elif carType == 3:
            self.small -= 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


#################################################################################

# use nested for loop to achieve the pattern below
# [0|0][0|1][0|2][0|3][0|4][0|5][0|6]
# [1|1][1|2][1|3][1|4][1|5][1|6]
# [2|2][2|3][2|4][2|5][2|6]
# [3|3][3|4][3|5][3|6]
# [4|4][4|5][4|6]
# [5|5][5|6]
# [6|6]


for left in range(7):
    for right in range(left, 7):
        #print("[" + str(left) + "|" + str(right) + "]", end="")
        print(f"[{left}|{right}]", end="")
    print()

############################################################

# You have four teams that will play against each other in the league, both at home and away.
# You've stored the names of the teams in a list, like this.
# teams = [ManUtd, Chelsea, Arsenal, Liverpool]
# Write a script that will output all possible team pairings.

teams = ["ManUtd", "Chelsea", "Arsenal", "Liverpool"]
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

# Hint
# For this, the order of the names matters because for each game,
# the first name will be the home team and the second name is the away team.
# Of course, what we don't want to do is have a team playing against itself.


#######################################################################
# Recursion Examples:
# def recursive_function(parameters):
#     if base_case_condition(parameters):
#         return base_case_value
#     recursive_function(modified_parameters)


def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for the factorial of " + str(n))
    return result

print(factorial(4))


def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

##############################################################3
# Fill in the gaps in the initials function so that it returns the
# initials of the words contained in the phrase received, in upper case. For example:
# "Universal Serial Bus" should return "USB"; "local area network" should return "LAN”.

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

############################################################################

#The is_palindrome function checks if a string is a palindrome.
# A palindrome is a string that can be equally read from left to right or right to left,
# omitting blank spaces, and ignoring capitalization.
# Examples of palindromes are words like kayak and radar,
# and phrases like "Never Odd or Even".
# Fill in the blanks in this function to return True if the passed string is a palindrome, False if not.

def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string.lower():
		# Add any non-blank letters to the
		# end of one string, and to the front
		# of the other string.
		if letter != " ":
			new_string += letter
			reverse_string += letter
	# Compare the strings
	if new_string == reverse_string[::-1]:
		return True
	return False


print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True


#

def is_palindrome(input_string):
	# We'll create two strings, to compare them
	new_string = ""
	reverse_string = ""
	# Traverse through each letter of the input string
	for letter in input_string:
		# Add any non-blank letters to the
		# end of one string, and to the front
		# of the other string.
		if is_palindrome:
			new_string = input_string.strip()
			reverse_string = new_string[::-1]
	# Compare the strings
	if new_string == reverse_string:
		return True
	return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

###################################################

#The replace_ending function replaces the old string in a sentence with the new string,
# but only if the sentence ends with the old string.
# If there is more than one occurrence of the old string in the sentence,
# only the one at the end is replaced, not all of them.
# For example, replace_ending("abcabc", "abc", "xyz") should return abcxyz, not xyzxyz or xyzabc.
# The string comparison is case-sensitive, so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).

def replace_ending(sentence, old, new):
    # Check if the old string is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = sentence.rfind(old)
        new_sentence = sentence[:i] + new
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"


######################################################################

# Given a list of filenames, we want to rename all the files with extension hpp to the extension h.
# To do this, we would like to generate a new list called newfilenames, consisting of the new filenames.
# Fill in the blanks in the code using any of the methods you’ve learned thus far, like a for loop or a list comprehension.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [e.replace('.hpp','.h') for e in filenames]

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

### OR

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames=[]
for filename in filenames:
    if filename.endswith(".hpp"):
        newfilenames.append(filename.replace(".hpp",".h"))
    else:
        newfilenames.append(filename)

print(newfilenames)


#########################################################################

# Let's create a function that turns text into pig latin:
# a simple text transformation that modifies each word moving
# the first character to the end and appending "ay" to the end.
# For example, python ends up as ythonpay.

def pig_latin(text):
    say = " "
    # Separate the text into words
    words = text.split()
    latin = []
    for word in words:
        # Create the pig latin word and add it to the list
        word = word[1:] + word[0] + 'ay'
        latin.append(word)
        # Turn the list back into a phrase
    return say.join(latin)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"


#############################################################

# The permissions of a file in a Linux system are split into three sets of three permissions: read, write, and execute for the owner, group, and others. Each of the three values can be expressed as an octal number summing each permission, with 4 corresponding to read, 2 to write, and 1 to execute. Or it can be written with a string using the letters r, w, and x or - when the permission is not granted.
#  For example:
#  640 is read/write for the owner, read for the group, and no permissions for the others; converted to a string, it would be: "rw-r-----"
#  755 is read/write/execute for the owner, and read/execute for group and others; converted to a string, it would be: "rwxr-xr-x"
#  Fill in the blanks to make the code convert a permission in octal format into a string format.

def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for digits in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digits >= value:
                result += letter
                digits -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(600))  # Should be rw-------


####################################################

# The group_list function accepts a group name and a list of members,
# and returns a string with the format: group_name: member1, member2, …
# For example, group_list("g", ["a","b","c"]) returns "g: a, b, c".
# Fill in the gaps in this function to do that.

def group_list(group, users):
 members = ""
 for user in users:
   members += user + ", "
 return group + ': ' + members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

##########################################################

# The guest_list function reads in a list of tuples with the name, age, and profession of each party guest,
# and prints the sentence "Guest is X years old and works as __." for each one.
# For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer"))
# should print out: Ken is 30 years old and works as Chef. Pat is 35 years old and works as La0wyer. Amanda is 25 years old and works as Engineer.
# Fill in the gaps in this function to do that.

def guest_list(guests):
	for guest in guests:
		name, age, job = guest
		print("{} is {} years old and works as {}".format(name, age, job))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""

###########################################################

