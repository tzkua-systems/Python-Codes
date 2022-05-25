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

