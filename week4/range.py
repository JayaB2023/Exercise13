#
# # below is a for loop which will print 0 1 2 (3 is the stop value)
for number in range(3):
    print(number)
# range below
zero, one , two = range(3)

print(zero, one, two)


# this will print numbers 0-2
# for number in range(1, 3):
#     print(number)
# # below will print numbers 0-9
# for number in range(1, 10):
#         print(number)
#
# # skip range?
# for number in range(1, 11, 3):
#         print(number)
#
# # below will print spam x3 times, * is an overload operator, will print words x3 times and multiple integers by 3
# word = 'spam'
# print(word * 3)
#
# # below is a tuple (comma makes it a tuple)
# # will print ('tomato', 'clemenine', x3)
# food = 'tomato', 'clementine'
# print(food * 3)
#
# # extended iterable unpacking?
# # if I try and run range of 4, and only 3 variables, it will get upset
# # this will bundle the numbers (positional placement of the asterisk changes where things will be scooped)
# # below - line 35 has a range of 10 - asterisk on 2 so the list will include [2-9]
# zero, one , *two = range(10)
# print(zero, one, two)
# print(type(zero))
# print(type(two))

# wildcard - captures the names in the middle for an iterable list of names
# print (a, b, c)- first and last part of the tuple will be outside of the list
tuple1 = 'cat', 'dog', 'python', 'mouse', 'camel'
tuple2 = 'kelp', 'crab', 'lobster', 'fish'
for a, *b, c in tuple1, tuple2:
    print (a, b, c)

tuple = "Feb 23", "Jaya", "Eyasmin", "Ellen", "3"
a, *names, b = tuple
print(a, names, b)
