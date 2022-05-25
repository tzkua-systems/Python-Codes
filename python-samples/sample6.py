class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "1. What colour are Apples? \n(a)Red/Green \n(b)Orange \n(c)Blue \n(d)Yellow \n",
    "2. What colour are Bananas? \n(a)Red/Green \n(b)Orange \n(c)Blue \n(d)Yellow \n",
    "3. What colour are Orange? \n(a)Red/Green \n(b)Orange \n(c)Blue \n(d)Yellow \n",
    "4. What colour are Blueberries? \n(a)Red/Green \n(b)Orange \n(c)Blue \n(d)Yellow \n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(f"{question.prompt} Enter your answer: ")
        if answer == question.answer:
            print("Correct! That's the right answer")
            score += 1
        else:
            print("Wrong! The correct answer is: " + question.answer)
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)

##########################################################################

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return __
    #return number == 1

  # Recursive case: keep dividing number by base.
  return is_power_of(__, ___)
    #return is_power_of(number//base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False


##########################################

def count_users(group):
  count = 0
  for member in get_members(group):
    #count += 1     #wrong placement
    if is_group(member):
      count += count_users(member)
    else:
        count += 1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18

###########################################

def digits(n):
    count = 0
    if n == 0:
        return 1
    while (n > 0):
        count += 1
        n = n // 10
    return count


print(digits(25))  # Should print 2
print(digits(144))  # Should print 3
print(digits(1000))  # Should print 4
print(digits(0))  # Should print 1

###################################################

# Question 4
# This function prints out a multiplication table
# (where each number is the result of multiplying the first number of its row by the number at the top of its column).
# Fill in the blanks so that calling multiplication_table(1, 3) will print out:
#
# 1 2 3
# 2 4 6
# 3 6 9

def multiplication_table(start, stop):
	for x in range (start, stop+1):
		for y in range (start, stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above

#####################################################################3

# The counter function counts down from start to stop when start is bigger than stop,
# and counts up from start to stop otherwise.
# Fill in the blanks to make this work correctly.

def counter(start, stop):
	x = start
	if x > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x > stop:
				return_string += ","
			x = x - 1
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
			x = x + 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

####################################################################3

#The even_numbers function returns a space-separated string of all positive numbers that are divisible by 2,
# up to and including the maximum that's passed into the function.
# For example, even_numbers(6) returns “2 4 6”. Fill in the blank to make this work.

def even_numbers(maximum):
	return_string = ""
	for x in range (2, maximum + 1, 2):
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

#########################################################

def first_and_last(message):
    if message == "" or message[0] == message[-1]:
        return True
    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

########################################################

