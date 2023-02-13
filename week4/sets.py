# SETS
# Sets aren't sequences, so will maintain the unique items but not the order when we print it
# wiggly braces create a set {}
# print type will show what kind of code is running - <class 'set'>
animals_A = {'cat', 'dog', 'rabbit', 'snake'}
print(type(animals_A))
print(animals_A)

names = ['Mary', 'Dolly', 'Mary']
print(names)
# this will print a unique list
# because it is a set, it will only print Mary once
unique_names = list(set(names))
print(unique_names)

# this will add hamster to my animals_A set
animals_A.add('hamster')
print(animals_A)

# this is a set because it is within {}
animals_B = {'cat', 'horse', 'pig'}

# intersection (intersection between a and b is cat)
# and plus and operator
# this will print the intersection between the two tuples which is cat
print(animals_A & animals_B) #operator syntax
print(animals_A.intersection(animals_B))  #method syntax

# Union - give me everything from both sets, but won't print intersections twice (only prints cat once)
# pipe operator is an or
print(animals_A | animals_B)  #operator syntax
print(animals_A.union(animals_B))  #method syntax

# difference
# will print everything other than cat
print(animals_A - animals_B)

# symmetric difference
# will print items which occur in one set only
# therefore will not print cat (the intersection)
print(animals_A ^ animals_B)

# Dictionary Values
# keys
# values
# what is the code doing
# dictionary because it has curly braces
# first key value pair has a key of UK and a list with UK cities
mydict = {'UK':['London', 'Wigan', 'Macclesfield', 'Bolton'],'US':['Miami', 'Springfield', 'New York', 'Boston']}
print(mydict['UK'] [2])

homer = 1
print(mydict['US'] [homer])

# country is the key
mydict['FR'] = ['Paris', 'Lyon', 'Bordeaux','Toulouse']
for country in mydict.keys():
    print(country, ' :', mydict[country])


# keys, values and items method of a dictionary