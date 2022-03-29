#Python Error Handlingm
# Error Handling in Python is done with Try and except Statement

#try, except, finally - keywords related to errors and exception blocks of code
# try - a block where we try to run a piece of code
# except - a block where we can intercept and handle the error
# else - a block where there is  no error
# finally - a block what happens at the end, where you can say something about your code
# break - keyword that stops the code from executing further

#1. Program to check integers
# #
# user_entry =None
# while type(user_entry)!=int:
#     try:
#         user_entry = int(input('Please input an integer: '))
#         print(f'You entered integer: {user_entry}. Program finished.')
#     except ValueError as e:
#         print(f'You entered non integer. Please try again')
#         print(f'Error message:{e}')
#

#  2. Program to check if the number is from a given ?
# check if the entry is integer
# check if the entry is in rage
# keep prompting to enter a number until
# the correct value is entered
# Keep prompting to enter a number until the correct value is entered
#
number = None
valid_flag = False

while not valid_flag:
    try:
        number = int(input('Please enter a number from 1 to 10: ')) # keep promting for a number
        while number > 0 and number <= 10:  # check the number is within the range
            # 0 < number <=10
            print(f'All is good! Your number is {number} is from 1 to 10.')
            valid_flag = True
            break
        else:
            print(f'Your number is {number} is not from a given range. Please try again')
            valid_flag = False
    except ValueError as e:
        print(f'You entered non integer. Please try again') # raise an error if a non integer value is entered
        print(f'Error message:{e}')
        valid_flag = False
    finally:
        print('------------****--------------')
#
#
# #3. Program where we can try to devide by zero
# try:
#     x=int(input('Enter numerator: '))
#     y=int(input('Enter denominator: '))
#     print(f'Divide {x} by {y} result: {round(x/y)}')
# except ZeroDivisionError as var0:
#     print(f'You cannot divide by 0: {var0}')
# except ValueError as value:
# #     print(f'You entered a non-integer value : {value}')
# # finally:
# #     print(f'The progam is done!')
#
# #4. Program to get person age based on name
#
# # Create a dictionary with names and ages
# ages = {
#     'Pam'  : 99,
#     'Kim'  : 24,
#     'Mike' : 38,
#     'Dave' : 48,
# }
#
# person = input (f'Please enter a name: ')
# try:
#     print(f'{person} is {ages[person]} years old.'')
# except KeyError as key:
#     print(f'{key} does not exist in our records! Please check the name.')
#
#