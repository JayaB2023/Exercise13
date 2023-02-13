#
import random

def generate_lottery_number():
  # Generate a random 6-digit lottery number
  lottery_number = ""
  for i in range(1):
    lottery_number += str(random.randint(1, 50))
  return lottery_number

print(generate_lottery_number())
#
# # generates random number between one and 50
# import random
# print(random.randint(0,50))


# for lottery_number in range (0,50):
#     print(lottery_number)
# import random
# print(random.randint(0,50))


# for number in range(3):
#     print(number)
#     # range below
#     zero, one, two = range(3)
#
#     print(zero, one, two)

# this will print a random 6 digit number
# import random
#
# fixed_digits = 6
#
# print(random.randrange(111111, 999999, fixed_digits))



# for number in range(1, 50):
#     print(number)
# break

# display 6 unique random numbers 1-50




# this is the help function
# info = help()
# print(info)

# video help code
import random
# this below is an empty list which will store 6 random numbers
lotteryNumbers = []
# for loop will generate 6 random numbers
for i in range (0,6):
  # randint will print a random integer between 1 and 50
  number = random.randint(1,50)
  # this checks if the number is in the list of lottery numbers
  while number in lotteryNumbers:
    number = random.randint(1,50)
  # if a number hasn't been picked before, it can be appended to the list
  lotteryNumbers.append(number)
# once we have the six numbers, the list is sorted
lotteryNumbers.sort()
# ask the user to input their numbers from their lottery ticket
# below initialises a new empty list
userNumber = []
# use a for loop to ask for 6 numbers
for i in range (0,6):
  # int function converts input to an integer
  number = int(input("Please enter a number between 1 and 50:"))
  # while loop below will ensure no repeats of the same number
  while (number in userNumber or number<1 or number>50):
    print("Invalid number, please try again.")
    number = int(input("Please enter a number between 1 and 50"))

  #     if number is valid it will append to list of userNumber
  userNumber.append(number)
# then we are printing the below and displaying the list in print(lotteryNumbers)
print(">>>Today's lottery numbers are: ")
print(lotteryNumbers)

# this will display user selection
print(">>> Your selection")
print(userNumber)

# count how many of the numbers appear in both lists
counter = 0
for number in userNumber:
  if number in lotteryNumbers:
    counter +=1

print("You guessed" + str(counter) + " numbers(s) correctly.")

import random
# this below is an empty list which will store 6 random numbers
lotteryNumbers = []
# for loop will generate 6 random numbers
for i in range (0,6):
  # randint will print a random integer between 1 and 50
  number = random.randint(1,50)
  while number in lotteryNumbers:
    number = random.randint(1,50)
  lotteryNumbers.append(number)
lotteryNumbers.sort()
print(">>>Today's lottery numbers are: ")
print(lotteryNumbers)