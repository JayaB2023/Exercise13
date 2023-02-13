# wiggly braces mean it is a dictionary or a set
# dictionary has keys and values in it
# numbers are saying how far away Mercury is from the sun in gigametres

# the below will print <class 'dict'>
planets = {'Mercury': 57.91, 'Venus': 108.2, 'Earth': 147.597870,'Mars': 227.94}
print(planets)
print(type(planets))

# while loop - is an if statement because you don't know how long it will stop raining
# full loop - if you have a full collection, python can count how many items are in it

# this will print the planet names, which are the values, doesn't give you the numbers which are the keys
for planet in planets:
    print (planet)

# this will give a tuple
# will print - (0, 'Mercury') etc
for planet in enumerate(planets.keys()):
    print (planet)

# this will now print from 1 - 1 Mercury
for row_number, planet in enumerate(planets.keys(), 1):
    print(row_number, planet)

# when I have a dictionary, I find a word
# when I say go to the key of venus, it says the number

# this will print the planets and their values
for key in planets.keys():
    print(key)
    print(planets[key])

# break in session

# STRING FORMAT WITH A FORMAT METHOD
# go to "" and write sentence you want to be printed on the screen
# the below code runs the below
# 1 Planet Mercury Gm 57.91
# 2 Planet Venus Gm 108.2
# 3 Planet Earth Gm 147.59787
# 4 Planet Mars Gm 227.94
# this is the format method
for row_number, planet in enumerate(planets.keys(), 1):
    print("{} Planet {} distance {} Gm".format(row_number, planet, planets[planet]))

# the below is with the addition of format specifier
# specifies within sentence how to format the number of strings
# the format specifier of {:2d} shifts the code 2 digits across
# the format specifier of {:<10s} will left align
# width when it is a format specifier for a number includes the decimal point  - {:06.2f} -6 means a width of 6 including the decimal place so 6 characters, data padding of 2 and decimal place of 2 - f is float
# python documentation for help!!!!!

for row_number, planet in enumerate(planets.keys(), 1):
    print("{:2d} Planet {:<10s} distance {:06.2f} Gm".format(row_number, planet, planets[planet]))

# LITERAL STRING INTERPOLATION
# aka "f" strings - literal string interpolators
# row number which is an integer will take up two space, planet will left align by 10 spaces, distance will have 6 characters and 2 digits after the decimal space
for row_number, planet in enumerate(planets.keys(), 1):
    print(f"{row_number:2d} Planet {planet:<10s} Distance {planets[planet]: 06.2f} Gm")





# homework - for loop practice and debugger practice
