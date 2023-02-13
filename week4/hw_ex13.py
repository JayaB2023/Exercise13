# open and edit a file called pelican txt

append = open('pelican.txt', 'a')

line = append.write("A wonderful bird is the pelican\n")
print(line)

line2 = append.write("His bill holds more than his belican\n")
print(line2)

# 6.
# writelines method will add (append) below to pelican.txt

# output = open('myfile', 'w')
# append = open ('logfile', 'a')
# num = output.write("He can take in his beak, \n", "Enough food for a week, \n", "But I'm damned if I see how the helican. \n")
# output.writelines(list)

# n\", - new line
list = ["He can take in his beak, \n", "Enough food for a week, \n", "But I'm damned if I see how the helican. \n"]
append.writelines(list)


