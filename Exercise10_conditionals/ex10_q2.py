# python program which emulates mechanism to create a pin code

# use below input for user to type in a pin
# int converts a string into an integer - input always returns a string unless specified
supplied_pin = int(input("Enter your PIN: "))

# create a variable (pin) and assign it to the pin (1234) to be checked against
pin = 1234

# variable which restricts number of attempts to 3
attempts = 3

# IF ELSE STATEMENT
# print a message for success and a message for failure
# include number of attempts left
# == is a comparison
# LOOP needed to restrict attempts to 3

for attempt in range(attempts):
    if pin == supplied_pin:
        print("correct pin")
        break
    else:
        attempts -=1
        print("incorrect pin")
        if attempts != 0:

            print('number of attempts left '+ str(attempts))
            supplied_pin = (int(input("Enter your PIN: ")))
        else:
            print("no attempts left")









