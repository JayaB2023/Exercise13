# this is the unicode for a euro sign (get from google)
euro_as_unicode = "/u20as"

# This will literally show a euro sign
euro_as_named_symbol = "/N{euro sign}"
print(euro_as_named_symbol)

# default separator is the space
print("Hello", "World", "!!!!")

print("Hello", "World", "!!!!", sep="***")

# print is a veriadic function
# the print function takes a variable number of parameters
print("Hello", "World", "!!!!", sep="_")
print("Hello", "World", "!!!!", sep="_")
print(1)
print(1, 2)

# this will print 'It, is......Thursday'
print('it', end=", ")
print('is', end=".......")
print('Thursday')
