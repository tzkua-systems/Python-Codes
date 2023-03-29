# this is a test program
a = (7 // 2)
b = (9 % 2)
c = a + b
print(a, b)
print(c)

# float and integers
mv_pop = 74735
# mv_pop = mv_pop + 4000 - 600
mv_pop += 4000 - 600
print(float(mv_pop))
print(type(float(mv_pop)))
print(int(mv_pop))
print(type(int(mv_pop)))

# list
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
print(months)
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
print(days)
year = [months, days]
print(year)
birthday = months[10], days[20]
print(birthday)
days.append(31)
# days.insert(30,31)
print(days)

# days.remove(31) or # days.pop(30) or # del days[2:]
# days.extend([32, 33, 34, 35])

# indexing
print(months[0], months[-12])
print(months[-1], months[11])
print(months[-3], months[9])
print(months[6], months[-6])
# slicing
first_half = months[:6]
print(first_half)
second_half = months[6:]
print(second_half)
q3 = months[6:9]
print(q3)
print(max(months))


###############################################################################

