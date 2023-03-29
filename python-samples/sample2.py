# def linear_search(list, target):
#    """ Return the index position of target if found, else returns None"""

#    for i in range (0, len(list)):
#        if list[i] == target:
#            return i
#        return None

def say_hi(name, age):
    # print("Hello " + name + ", you are " + age)
    print("Hello " + name + ", you are " + str(age))
    print(f'Hello {name}, you are {age} years old!')

# say_hi("Tobi", "30")
# say_hi("Martha", "25")
say_hi("Tobi", 30)
say_hi("Martha", 25)

# print(cube(3))
def cube(num):
    return num*num*num

result = cube(4)
print(result)

# booleanconditions
is_male = True
is_tall = True

if is_male and is_tall:
#if is_male or is_tall:
    print("You are a tall male")
elif is_male and not is_tall:
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but you are tall")
else:
    print("You are not a male and you are not tall")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(22, 40, 16))

# Calculator
n1 = float(input("Enter 1st number: "))
op = input("Enter an operator: ")
n2 = float(input("Enter 2nd number: "))

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "/":
    print(n1 / n2)
elif op == "*":
    print(n1 * n2)
elif op == "**":
    print(n1 ** n2)
else:
    print("Invalid Operator")

# Dictionary: stores key value pairs
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"])
print(monthConversions.get("Jan"))

<<<<<<< HEAD
#
=======
>>>>>>> 716a8dd7a67931423b2f347f948375d3362c8762
regulator = {
    0: "lowest",
    1: "low",
    2: "middle",
    3: "high",
    4: "highest"
}

print(regulator[1])
print(regulator.get(3))

##########################################
