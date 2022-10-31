'''
Write a program (not a function) that repeatedly takes in user input representing daily rainfall measurements
(non-negative integers) until it encounters the integer 99999. The program should output the
average of the numbers encountered before 99999. Ignore negative numbers and any user input that is not made up entirely of digits.
If no valid numbers are entered, then print out 0 instead.
'''

EXIT_INT = "99999"

count = 0
total_rainfall = 0

user_input = input("What was the daily rainfall: ")

while user_input != EXIT_INT:
    while not user_input.isdigit():
        user_input = input("Try again: ")
        if user_input == EXIT_INT:
            break
    if user_input == '0' or user_input == EXIT_INT:
        break
    count += 1
    total_rainfall += int(user_input)
    user_input = input("What was the daily rainfall: ")    

if total_rainfall == 0:
    print(0)
else:
    print(total_rainfall / count)
