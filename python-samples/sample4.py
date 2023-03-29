class Customer:
    def __init__(self, name, membership_type):
        self.name = name
        self.membership_type = membership_type

    def update_membership(self, new_membership):
        self.membership_type = new_membership

    def __str__(self):
        return self.name + " " + self.membership_type

    def print_all_customers(Customers):
        for Customer in Customers:
            print(Customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True

        return False

# a = Customer("Tobi", "Gold")
# print(a.name, a.type)
# b = Customer("Martha", "Silver")
# print(b.name, b.type)

Customers = [Customer("Tobi", "Gold"), Customer("Martha", "Silver")]
print(Customers[1].name)
print(Customers[1].membership_type)
print(Customers[0])

Customers[1].update_membership("Bronze") #update_membership function
print(Customers[1].membership_type)

Customer.print_all_customers(Customers) #print_all_customers function

print(Customers[0] == Customers[1])

##################################################

class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

Student1 = Student("Taiwo", "Engineering", 3.4, False)
Student2 = Student("Kehinde", "Law", 2.5, True)
Student3 = Student("Idowu", "Accounting", 3.1, False)
Student4 = Student("Alaba", "Business", 3.8, False)
print(Student1.name)
print(Student2.major)

print(Student3.on_honor_roll())
print(Student4.on_honor_roll())

####################################################

# reading files
# text_file = open("readme.txt", "w")    #write function (overwrite all the existing content)
# text_file = open("readme2.txt", "w")     #open/create new file
# text_file = open("readme.txt", "r+")   #read & write function

text_file = open("readme.txt", "r")  # read function
print(text_file.read())
print(text_file.readline())
for line in text_file.readlines():
    print(line)
text_file.close()

text_file = open("readme.txt", "a")  # append function (add to the existing content)
text_file.write("\nTobi Taiwo")
text_file.close()

# open/create a new file
html_file = open("index.html", "w")
html_file.write("<!DOCTYPE html>")
html_file.write("\n<html>\n<head>\n</head>\n<body>\n</body>\n</html>")
html_file.close()

#########################################

calculation = 24
unit = "hours"


def days_to_units(num_of_days):
    print(num_of_days > 0)
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation} {unit}"
    elif num_of_days == 0:
        return "Invalid Input: Zero Value"
    else:
        print(num_of_days > 0)
        return "Invalid Input: Negative Value"


def validate_user_input():
    print(user_input.isdigit())
    if user_input.isdigit():
        print(days_to_units(int(user_input)))
    else:
        print("Invalid Input: Not a Digit")


user_input = input("Hey user! Enter a number to be converted: ")
validate_user_input()

##

calculation = 24
unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation} {unit}"


def validate_user_input():
    if user_input.isdigit():
        user_number = int(user_input)
        if user_number > 0:
            print(days_to_units(user_number))
        elif user_number == 0:
            print("Invalid Input: Zero Value")
    else:
        print("Invalid Input: Negative, Float or String Value")


user_input = input("Hey user! Enter a number to be converted: ")
validate_user_input()

##

calculation = 24
unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation} {unit}"


def validate_user_input():
    try:
        user_number = int(num_of_days_element)
        if user_number > 0:
            print(days_to_units(user_number))
        elif user_number == 0:
            print("Invalid Input: Zero Value")
        else:
            print("Invalid Input: Negative Value")
    except ValueError:
        print("Invalid Input: Float or String Value")


#while True:
user_input = ""
while user_input != "exit":
    user_input = input("Hey user! Enter a number to be converted: ")
    #for num_of_days_element in user_input.split(", "):
    for num_of_days_element in set(user_input.split(", ")):
        validate_user_input()

##

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
       return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"



def validate_user_input():
    try:
        user_number = int(days_and_unit_dictionary["days"])
        if user_number > 0:
            calculated_value = days_to_units(user_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_number == 0:
            print("Invalid Input: Zero Value")
        else:
            print("Invalid Input: Negative Value")
    except ValueError:
        print("Invalid Input: Float or String Value")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user! Enter a number of days to be converted:\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_user_input()


##############################################################################

command = ""
started = False

while True:
    command = str(input("Enter your command> ")).lower()
    if command == "start":
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started... Ready to go")
    elif command == "stop":
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car stopped...")
    elif command == "help":
        print('''
start = to start the car
stop = to stop the car
quit = to quit the program
        ''')
    elif command == "quit":
        break
    else:
        print("I don't understand that command...")

###################################################################

def sum(a, *b):
#def sum(*b):
    print(a)
    print(b)
    #c = a
    for i in b:
        #c = c + i
        c = a + i
    print(c)

sum(5, 6, 34, 78)

#keyword arguments
#def person(name, *data):
def person(name, **data):
    print(name)
    print(data)

#person('Tobi', 25, 'Lagos', 803)
person('Tobi', age=25, city='Lagos', mob=803)

#or

def person(name, **data):
    print(name)

    for i, j in data.items():
        print(i,j)

person('Tobi', age=25, city='Lagos', mob=803)

####################################################

#pass a list into a function
def count(lst):
    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd

lst = [20, 25, 14, 19, 16, 24, 28, 47, 26]

even, odd = count(lst)

print("Even: {}, Odd: {}".format(even, odd))

#fibonacci series
def fib(n):
    a = 0
    b = 1

    if n == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2, n):
            if n > 0:
                c = a + b
                a = b
                b = c
                print(c)
            else:
                print("Error")

fib(10)

#########################################

def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
    #if n == 0:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for the factorial of " + str(n))
    return result

print(factorial(5))


def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f"The factorial of {n} is {f}"

print(fact(4))

#filter

def is_even(n):
    return n % 2 == 0

nums = [3, 2, 6, 8, 4, 6, 2, 9]
evens = list(filter(is_even, nums))

print(evens)

#lambda functions

nums = [3, 2, 6, 8, 4, 6, 2, 9]
evens = list(filter(lambda n : n % 2 == 0, nums))

print(evens)

#################################################

