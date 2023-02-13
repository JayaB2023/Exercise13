# how to extract a name from a list
names = ['Shade', 'Mirfat', 'Michelle']
print(type(names))
# created a variable of name and used [1] to print name 1 in list
person = names[1]
print(person)

# this will print the last name in the list (Michelle)
person2 = names[-1]
person3 = names[-2]

# replace someone's name
# this replaces name [0] (shade) with the string Shade Jones
names[0] = 'Shade Jones'
print(names)

# slicing (same as the Belgium hw from last week w/ Sara)
# this will print the first 2 names (Shade Jones and Mirfat)
print(names[0:2])

# this will print Mirfat and Michelle
print(names[-2:])

# delete names out of the list
# this will delete names 3 and 4 from the list
del names[2:4]
print(names)

# the below will add names to the end
# below is the extend method
# will add Sophie and Sara on to the original names variable
names.extend(['Sophie', 'Sara'])
print(names)

# this adds Jess as a string (no square brackets as in the extend method)
names.append('Jess')
print(names)

# shorter version of extend
names += ['Jaya', 'Ellen']
print(names)

# add a tuple into a specific position in the list
# will insert the tuple of 'Salma' into position 3 in the list
names.insert(3, 'Salma')
print(names)

# insert an item between items
# this inserts Aaliyah as a single list item at position 1 - line 52 is cleaner code
# names[1:1] = ['Aaliyah']
# print(names)
names.insert(1, 'Aaliyah')
print(names)

# this will print the string of Eyasmin at the beginning of the list
names.insert(0, 'Eyasmin')
print(names)

# remove items
# pop based on a position, or with no number, will print the last name in the list
popped = names.pop(6)
print(popped)
# this will remove the name 'ellen' from the list. If there are multiple Ellens in the list, it will remove the first one but keep the rest
names.remove('Ellen')
print(names)

print("=" * 20)
# this sorts the list in alphabetical order
names.sort()
print(names)

# this will print names in reverse alphabetical order
names.sort(reverse=True)
print(names)

# below - sort key is the length function
# this will sort names based on their length (shortest to longest)
# key and true are named parameters so need to assign the value of any function name
names.sort(key=len)
print(names)

# this will sort longest names first due to reverse=True
names.sort(key=len, reverse=True)
print(names)

sorted(names)