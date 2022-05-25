# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
    km = miles * 1.6  # approximately 1.6 km in 1 mile
    return km


my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = my_trip_miles * 1.6
convert_distance(55)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
round_trip = my_trip_km * 2
print("The round-trip in kilometers is " + str(round_trip))


####################################################################

# This function compares two numbers and returns them
# in increasing order.


def order_numbers(number1, number2):
    if number2 > number1:
        return number1, number2
    else:
        return number2, number1


# 1) Fill in the blanks so the print statement displays the result
#    of the function call


smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)


##########################################################


def lucky_number(name):
    number = len(name) * 9
    result = "Hello " + name + ". Your lucky number is " + str(number)
    return result


print(lucky_number("Kay"))
print(lucky_number("Cameron"))


############################################################


def is_positive(range):
    for index in range:
        if index > 0:
            print(f"index is: {index} state is: {True}")
        else:
            print(f"index is: {index} state is: {False}")
    return range


is_positive(range(-16, 16, 2))

# another method
x = range(-10, 10, 2)
print(x)
while x <= 10:
    if x > 0:
        print(f"number is: {x} state is: {True}")
    else:
        print(f"number is: {x} state is: {False}")

print("Done")


############################################################
# If a filesystem has a block size of 4096 bytes,
# this means that a file comprised of only one byte will still use 4096 bytes of storage.
# A file made up of 4097 bytes will use 4096*2=8192 bytes of storage.
# Knowing this, can you fill in the gaps in the calculate_storage function below,
# which calculates the total number of bytes needed to store a file of a given size?

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = block_size * 2
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = full_blocks % filesize
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return full_blocks
    return block_size


print(calculate_storage(1))  # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192


###################################################
# Complete the function by filling in the missing parts.
# The color_translator function receives the name of a color,
# then prints its hexadecimal value. Currently,
# it only supports the three additive primary colors (red, green, blue),
# so it returns "unknown" for all other colors.

def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color


print(color_translator("blue"))  # Should be #0000ff
print(color_translator("yellow"))  # Should be unknown
print(color_translator("red"))  # Should be #ff0000
print(color_translator("black"))  # Should be unknown
print(color_translator("green"))  # Should be #00ff00
print(color_translator(""))  # Should be unknown


###################################################
# Complete the body of the format_name function.
# This function receives the first_name and last_name parameters
# and then returns a properly formatted string.

def format_name(first_name, last_name):
    # code goes here
    # string = first_name, last_name
    if first_name != str("") and last_name != str(""):
        # print(f"Name: {last_name}, {first_name}")
        string = f"Name: {last_name}, {first_name}"
    elif first_name != str("") and last_name == str(""):
        # print(f"Name: {first_name}")
        string = f"Name: {first_name}"
    elif first_name == str("") and last_name != str(""):
        # print(f"Name: {last_name}")
        string = f"Name: {last_name}"
    else:
        # print(f" ")
        string = f" "
    return string


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"
print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"
print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"
print(format_name("", ""))


# Should return an empty string

##############################################

def sum(x, y):
    return x + y


print(sum(sum(1, 2), sum(3, 4)))


############################################


def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    # keep just the fractional part of the quotient
    # if numerator == 0 or denominator ==0:
    if numerator != 0 and denominator != 0:
        result = (numerator / denominator) % 1
        return result
    # return 0
    else:
        # result = (numerator / denominator) % 1
        return 0
    # return result


print(fractional_part(5, 5))  # Should be 0
print(fractional_part(5, 4))  # Should be 0.25
print(fractional_part(5, 3))  # Should be 0.66...
print(fractional_part(5, 2))  # Should be 0.5
print(fractional_part(5, 0))  # Should be 0
print(fractional_part(0, 5))  # Should be 0


###############################################
# Fill in the blanks to make the print_prime_factors function print all the prime factors of a number.
# A prime factor is a number that is prime and divides another without a remainder.

def print_prime_factors(number):
    # Start with two, which is the first prime
    factor = 2
    # Keep going until the factor is larger than the number
    while factor <= number:
        # Check if factor is a divisor of number
        if number % factor == 0:
            # If it is, print it and divide the original number
            print(factor)
            number = number / factor
        else:
            # If it's not, increment the factor by one
            factor += 1
    return "Done"


print_prime_factors(100)


# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT


#####################################################################

def is_power_of_two(n):
    # Check if the number can be divided by two without a remainder
    while n % 2 == 0:
        n = n / 2
        if n == 0:
            return False
    # If after dividing by two the number is 1, it's a power of two
    if n == 1:
        return True
    return False


print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False


#################################################################
# The multiplication_table function prints the results of a number passed to it multiplied by 1 through 5.
# An additional requirement is that the result is not to exceed 25, which is done with the break statement.
# Fill in the blanks to complete the function to satisfy these conditions.


def multiplication_table(number):
    # Initialize the starting point of the multiplication table
    multiplier = 1
    # Only want to loop through 5
    while multiplier <= 5:
        result = multiplier * number
        # What is the additional condition to exit out of the loop?
        if result >= 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the variable for the loop
        multiplier += 1


multiplication_table(3)
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15
multiplication_table(5)
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
multiplication_table(8)


# Should print: 8x1=8 8x2=16 8x3=24

######################################################################


def sum_divisors(n):
    # divisor = [0]
    divisor = 0
    for i in range(1, n):
        if n % i == 0:
            # divisor.append(i)
            divisor += 1
    # Return the sum of all divisors of n, not including n
    # return sum(divisor)
    return divisor


print(sum_divisors(0))
# 0
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# 114

# another method
def sum_divisors(n):
    sum = 0
    div = 1
    while div < n:
        if n % div == 0:
            sum += div
            div += 1
        else:
            div += 1
    # Return the sum of all divisors of n, not including n
    return sum


print(sum_divisors(0))
# 0
print(sum_divisors(3))  # Should sum of 1
# 1
print(sum_divisors(36))  # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))  # Should be sum of 2+3+6+17+34+51
# 114


#################################################################

#Fill in the gaps of the sum_squares function, so that it returns the sum of all the squares of numbers between 0 and x (not included).
# Remember that you can use the range(x) function to generate a sequence of numbers from 0 to x (not included).

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += n*n
    return sum

print(sum_squares(10)) # Should be 285


#############################################################

def validate_users(users):
  for user in users:
    if len(user) > 3:
      print(user + " is valid")
    else:
      print(user + " is invalid")

validate_users(["purplecat", "purple", "cat"])

# OR

def validate_users(user):
  if len(user) > 3:
      print(user + " is valid")
  else:
      print(user + " is invalid")

validate_users("purplecat")


###############################################################

from array import *

arr = array('i', [])  #empty integer array
y = int(input("Enter the length of the array: "))

for i in range(y):
    x = int(input("Enter the array's values: "))
    arr.append(x)

print(arr)

val = int(input("Enter the search value: "))
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k += 1

print(arr.index(val))

rem = int(input("Enter the value to delete: "))
r = 0
for j in arr:
    if j == rem:
        print(r)
        arr.remove(rem)
        break
    r += 1

print(arr)

###################################################################

