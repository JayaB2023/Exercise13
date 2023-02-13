import random
# this below is an empty list which will store 6 random numbers
lotteryNumbers = []
# for loop will generate 6 random numbers
for i in range (0,6):
  # randint will print a random integer between 1 and 50
  number = random.randint(1,50)

  # this checks if the number is in the list of lottery numbers
  # A "While" Loop is used to repeat a specific block of code an unknown number of times, until a condition is met
  while number in lotteryNumbers:
    number = random.randint(1,50)
  #     if the number meets the conditions of being between 1-50 and not entered before it will be added to the list
  lotteryNumbers.append(number)
#   once we have the six numbers the list is sorted
lotteryNumbers.sort()
print(">>>Today's lottery numbers are: ")
print(lotteryNumbers)