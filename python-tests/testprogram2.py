# this is an assignment program
# x = float(input("Enter the 1st number:"))
# y = float(input("Enter the 2nd number:"))
# z = float(input("Enter the 3rd number:"))
# print("The max value is:", max(x, y, z))

# quiz on assign & modify variable
reservoir_volume = 4.445e8
rainfall = 5e6
# tasks
rainfall -= (0.1 * rainfall)
# rainfall *= 0.9
reservoir_volume += rainfall
# reservoir_volume += rainfall
reservoir_volume += (0.05 * reservoir_volume)
# reservoir_volume *= 1.05
reservoir_volume -= (0.05 * reservoir_volume)
# reservoir_volume *= 0.95
reservoir_volume = reservoir_volume - 2.5e5
# reservoir_volume = reservoir_volume - 2.5e5
print(rainfall)
print(reservoir_volume)

# BOOLEAN ALGEBRA
sf_pop, sf_area = 864816, 231.89
rio_pop, rio_area = 6453682, 486.5
sf_pop_den = sf_pop / sf_area
print(sf_pop_den)
rio_pop_den = rio_pop / rio_area
print(rio_pop_den)

print("is sf denser than rio:", sf_pop_den > rio_pop_den)
print("is rio denser than sf:", sf_pop_den < rio_pop_den)
print("is sf denser than rio:", sf_pop_den < rio_pop_den)
print("is rio denser than sf:", sf_pop_den > rio_pop_den)

if sf_pop_den > rio_pop_den:
    print(True)
else:
    print(False)

##########################################################################

