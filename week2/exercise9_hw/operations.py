# Exercise 9 part 2

# the below syntax is a way of outputting a prompt to the console and getting a reply. The variable var is a reference to that reply, which is a string
# how do you enter a value?
# input () is a function that takes the input from the usr and converts into a string

# input will show me the string and wait for me to input information


# code summary - if the string is a word, it will print the word/phrase in capitals, the number of characters in the worde/phrase and false as there are no numbers in the string
# if the string is purely a number, it will print true
var = input("Please enter a value ")

uppercase = var.upper()

print(uppercase)

# var = ('my name is jaya')
print(len(var))

#  checking everything within var is a number from 0-9
# var = ('my name is jaya')
# is decimal - checking if all characters in the string are a number of base 10 (numbers between 0 and 9)
# will print true or false
print(var.isdecimal())


