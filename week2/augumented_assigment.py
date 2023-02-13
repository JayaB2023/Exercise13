# comppund assignment

x = 4
y = 6
z = x + y
# this adds them together
print(x)
x = x + y
# = is an assignment operator

print (x)

# compound syntax - short-hand

# long hand
# x = x + y

# short-hand syntax works with adding, subtracting, multiplying and dividing

x += y

print(x)

a = 5
b = 2
a = a * b
# ^ this is the long hand

a *= b

# ^this is the short hand syntax

# immutable types
# because it is immutable, it won't print Jaya, it will just print Abigail, doesn't need the memory box of Jaya, so the variable is now trash and it now has Abigail as the variable in memory
# create a box of memory (name)
name = "Jaya"
name = "Abigail"
print(name)

# create a box of memory (name)
name = "Victoria"


# tuple v list

names_tuple = 'Shade' , 'Sadia'
print(names_tuple)
print(type(names_tuple))
