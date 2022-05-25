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
