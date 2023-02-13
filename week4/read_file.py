# use the open and read methods to slurp the entire contents of pelican.txt file
# open method:
# read method:
# Slurp meaning - prints a large amount of text in terminal

# open and read method which slurps a file
# adds pelican.txt to display in the terminal
lines = open('pelican.txt').read()
print(lines)
# adding (type) will show the <class 'str'> in the terminal
print(type(lines))

# 5.
# pelican.txt as a list and output number of items within the list

# line 20 - 22 reads the pelican file into a list
# "r" = read
# readlines methods returns a list as a singular item in output
# with statement manages external resources in your programme - pelican.txt counts as external resource?
with open("pelican.txt", "r") as pelican:
	lines = pelican.readlines()
	print(lines)

# then we need to divide values into individual lists to show how many items in the list there are
# then use the split() method to divide values into a string using a separator character we specify, here we've defined 'I' as ','
# for loop below lets us read our file line by line
# below opens an empty list to be filled (pelican_line = [])
# len function shows how many elements (lines) there are - output is 6

pelican_line = []
for I in lines:
    as_list = I.split(", ")
    pelican_line.append(as_list)
    print(pelican_line)
    print("No of elements in the list are:", len(pelican_line))


