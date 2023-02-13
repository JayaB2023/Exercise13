# the below is a list, it is a list because they are square brackets
address_parts = [1, "High Street", "Townsville", "Greater London", "xx123"]

# syntax for a full loop
# 1) start with a loop variable (what am I targeting) - item

address = ""

for item in address_parts:
    address = address + str(item) + " "

print(address)

# strings are immutable so need to create a new box in memory whcih is the result of concatenation

print('Victoria says "hi!" to the class')
# double quotes needed because of 's
print("Victoria's peas were gross")
# three double quotes at the beginning and three double quotes at the end allows you to have speech quotes
print("""Victoria's peas were gross and she said "YUK"!""")

# STRING METHODS
word = "spam "
print(word, word, word, word)
# instead of doing the above to print 'spam' four times, you can use an operator as below
# the below will print spam 12 times with a space, because there is a space before the " in the spam print function
print(word * 12)

# + with numeric operands means add
#  + with string operands means concatenate
# * is a multipler/repeater function - repeats spam x 12 times  ^

# methods belong to objects (object is sentence, sentence is a string)
sentence = """Victoria's peas were gross and she said "YUK"!"""
# when you type sentence. you see all the string related functions the method can do
# strings are immutable
# the below will print VICTORIA'S PEAS WERE GROSS AND SHE SAID "YUK"
sentence_as_uppercase = sentence.upper()
print(sentence_as_uppercase)

# this will find where toria is
toria = sentence.find('toria')
print(toria)

not_there = sentence.find('yum')
print('yum')

# breakout room task
text = 'hello world'
# the below printed 2 because there are 2 'o's in hello world
print(text.count('o'))

if text.startswith('hell'):
    print("It's hell in there")

if text.isalpha():
    print('string is all alpha')
# print tab, and then print new row
text = ' \t\r\n'
if text.isspace():
    print('string is whitespace')


# STRING FORMATTING
