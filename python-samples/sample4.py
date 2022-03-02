class Customer:
    def __init__(self, name, type):
        self.name = name
        self.type = type

a = Customer("Tobi", "Gold")
print(a.name, a.type)

b = Customer("Martha", "Silver")
print(b.name, b.type)

#reading files
#text_file = open("readme.txt", "w")    #write function (overwrite all the existing content)
#text_file = open("readme2.txt", "w")     #open/create new file
text_file = open("readme.txt", "a")    #append function (add to the existing content)
#text_file = open("readme.txt", "r+")   #read & write function
#text_file = open("readme.txt", "r")    #read function
text_file.write("\nTobi Taiwo")

print(text_file.read())
print(text_file.readline())
for line in text_file.readlines():
    print(line)

text_file.close()

#open/create a new file
html_file = open("index.html", "w")
html_file.write("<!DOCTYPE html>")
html_file.write("\n<html>\n<head>\n</head>\n<body>\n</body>\n</html>")

html_file.close()
