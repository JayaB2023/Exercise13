message = "Goodbye Python"

print(message)

# square brackets access elements in a tuple., list,  value once we povide a key in a dictionary

# this gives the 0th character (G f goodbye)
print(message[0])

# this will peint 'b' (4th character, 0-4)
print(message[4])

# this prints character 4-7 - 'bye'
print(message[4:7])

# this will print 'python' as a slice of the string or message
print(message[8:14])

# start the slice at 8 - leave blank, will print the rest of the message string
print(message[8: ])

# this will print the word 'good' - characters 0-4
print(message[:4])

# this will also print 'good'
print(message[-7])

# this will print p t o - every second character from the 6th from the end?
print(message[-6::2])

# STRING METHODS - SPLIT AND JOIN
# S

address_parts = [1, "High Street", "Townsville", "Greater London", "xx123"]

address = ""

for item in address_parts:
    address = address + str(item) + " "

print(address)

# concatenated_address = ", ".join(address_parts)
# print(concatenated_address)

# BREAKOUT ROOM 2 - STRINGS JOIN PRACTICE
# avatar::0:0:The super-user (zero):/root:/bin/sh - the below will print this
# line = ':'.join(elems) this line combines with avatar and the super user
# integers 0 and 4 are the location of the letters ?
#




line = 'root::0:0:superuser:/root:/bin/sh'
# this shows you the user
elems = line.split(':')
# elems is a variable which means elements. this is assigned a list, created as a result of line.split
# splits up into component parts, using the component as a separator

elems[0] = 'avatar'
# ^take out the elemtn root and replace with the number four, take out the term avatar and replace with
elems[4] = 'The super-user (zero)'
line = ':'.join(elems)
# join the strings using the colon separator
print(line)

