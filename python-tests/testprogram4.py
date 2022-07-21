# this is a test program from Qazi tutorial
'''
import turtle

my_turtle = turtle.Turtle()
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)


def square(length, angle):
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)

for i in range(4):
    square(50, 90)

print(square)


def rectangle(angle, length):
    my_turtle.backward(length)
    my_turtle.right(angle)
    my_turtle.backward(length)
    my_turtle.right(angle)
    my_turtle.backward(length)
    my_turtle.right(angle)
    my_turtle.backward(length)

for j in range(4):
    rectangle(100, 60)

print(rectangle)
'''

#############################################################

# The email_list function receives a dictionary, which contains domain names as keys,
# and a list of users as values. Fill in the blanks to generate a list that contains
# complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
	emails = []
	for domains, users in domains.items():
	  for user in users:
	    emails.append(user + '@' + domains)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

###############################################################

# The groups_per_user function receives a dictionary,
# which contains group names with the list of users.
# Users can belong to multiple groups.
# Fill in the blanks to return a dictionary with the users as keys
# and a list of their groups as values.

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for users, groups in group_dictionary.items():
		# Now go through the users in the group
		for user in groups:
			if user in user_groups:
				user_groups[user].append(users)
			else:
				user_groups[user] = [users]
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

########################################################

# The add_prices function returns the total price of all of the groceries in the  dictionary.
# Fill in the blanks to complete this function.

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for groceries, prices in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += prices
	# Limit the return value to 2 decimal places
	return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

############################################################

# The format_address function separates out parts of the address string into new strings:
# house_number and street_name, and returns: "house number X on street named Y".
# The format of the input string is: numeric house number, followed by the street name which may contain numbers,
# but never by themselves, and could be several words long. For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive".
# Fill in the gaps to complete this function.

def format_address(address_string):
  # Declare variables
  house_number = ""
  street_name = ""
  # Separate the address string into parts
  address = address_string.split(" ", 1)
  # Traverse through the address parts
  for part in address:
    # Determine if the address part is the
    # house number or part of the street name
    if part.isdigit():
      house_number += address[0]
    else:
      street_name += address[1]
  # Does anything else need to be done
  # before returning the result?

  # Return the formatted string
  return "house number {} on street named {}".format(house_number, street_name)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

##############################################

# The highlight_word function changes the given word in a sentence to its upper-case version.
# For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day".
# Can you write this function in just one line?

def highlight_word(sentence, word):
	return(sentence.replace(word, word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

###############################################

#A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order. Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in reverse order, to get an accurate list of the students as they arrived.

def combine_lists(list1, list2):
    # Generate a new list containing the elements of list2
    # Followed by the elements of list1 in reverse order
    new_list = list2
    for i in reversed(range(len(list1))):
        new_list.append(list1[i])
    return new_list


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

##

def combine_lists(list1, list2):
    new_list = list2
    list1.reverse()
    new_list.extend(list1)

    return new_list

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

####################################################

# Use a list comprehension to create a list of squared numbers (n*n). The function receives the variables start and end, and returns a list of squares of consecutive numbers between start and end inclusively.
# For example, squares(2, 3) should return [4, 9].

def squares(start, end):
	return [n**2 for n in range(start, end+1)]

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

####################################################

# Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information about each one.

def car_listing(car_prices):
  result = ""
  for keys, values in car_prices.items():
    result += "{} costs {} dollars".format(keys, values) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

##################################################

# Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries, with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, but Rory's list has more current information about the number of guests. Fill in the blanks to combine both dictionaries into one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name is included in both dictionaries. Then print the resulting dictionary.

def combine_guests(guests1, guests2):
    #guests2.update(guests1)
    all_guest = Taylors_guests.copy()
    all_guest.update(Rorys_guests)
    return all_guest
    #return guests2
  # Combine both dictionaries into one, with each key listed
  # only once, and the value from guests1 taking precedence

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

###################################################

# Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank spaces, numbers, or punctuation. Upper case should be considered the same as lower case. For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text:
    # Check if the letter needs to be counted or not
    if letter not in result:
      result[letter.lower()] = 1
    # Add or increment the value in the dictionary
    else:
      result[letter] += 1
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

##
def count_letters(text):
    result = {}
    text = text.lower()
    # Go through each letter in the text
    for letter in text:

        # Check if the letter needs to be counted or not
        if letter.isalpha():
            # Add or increment the value in the dictionary
            count = text.count(letter)
            result[letter] = count
    return result


print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

####################################################

# The code below defines an Elevator class. The elevator has a current floor, it also has a top and a bottom floor that are the minimum and maximum floors it can go to. Fill in the blanks to make the elevator go through the floors requested.
# For the up and down methods, did you take into account the top and bottom floors? Keep in mind that the elevator shouldn't go above the top floor or below the bottom floor. To check that out, try the code below and verify if it's working as expected. If it's not, then go back and modify the methods so that this code behaves correctly.
# Now add the str method to your Elevator class definition above so that when printing the elevator using the print( ) method, we get the current floor together with a message. For example, in the 5th floor it should say "Current floor: 5"

class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current < self.top:
            self.current += 1
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current > self.bottom:
            self.current -= 1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
    def __str__(self):
        return '"Current floor: {}"'.format(self.current)


elevator = Elevator(-1, 10, 0)

elevator.up()
elevator.current #should output 1
print(elevator.current)

elevator.down()
elevator.current #should output 0
print(elevator.current)

elevator.go_to(10)
elevator.current #should output 10
print(elevator.current)

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

elevator.go_to(5)
print(elevator)

#################################################

def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout":
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'login', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)

##################################################

