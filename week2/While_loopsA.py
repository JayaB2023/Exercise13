line = None

while line != 'done':
    line = input('Type "done" to complete:')
    line = line.lower()
    print('<', line, '>')

print("The End")