import time # to import all functions available in time module
from time import sleep # to import only a specific function
import copy
from copy import copy
import random
from faker import Faker # to import external library Faker
fake = Faker(locale=['en_CA','en_US']) # to initialize the library in our file

# PYTHON IMPORT

# In Python if we want to use the functionality stored in other files
# we use 'import' to make code from one file (or module) available in another
# Imports in Python are important to structure the code more effectively
# and make code more maintainable

#. 1. TIME
# python module called 'time' - add to the very top of the file: import time

current_date = time.asctime()
print(f'Current date and time is: {current_date}')
print(f'Test started: {current_date}')
print(f'test step 1 is executed')
print(f'test step 2 is executed')
print(f'test step 3 is executed')
print(f'test step 4 is executed')
print(f'test step 5 is executed')
print(f'Test Finished at: {current_date}')

# create a ticking timer
# seconds = 10
# while seconds != 0:
#     print(f'Time to self-distuct: {seconds} sec')
#     seconds = seconds - 1
#     #sleep(1) # requires import: from time import sleep
#     sleep(1)
# print(f'BOOM!')

# 2. COPY
# Python module called 'copy', add to the top of the file: import copy

name_list = ['Bryan', 'Kate', 'Maria', 'Alice','Jayson']
print(name_list)
new_list = copy(name_list)
print(f'Copy of the list: {new_list}')

# 3. RANDOM
# Python module called 'random' - add to the top of the file: import random

# generate random integer
a = random.randint(111,999)
print(f'Random integer: {a}')

# Program to generate random integers based on user input

# x = int(input('Enter a number for the lowest value in range: '))
# y = int(input('Entere a number for the highest value in range: '))
# z = random.randint(x, y)
#
# print(f'Generate random integer from to {x, y}')
# print(f'The random integer is: {z}')

# generate random float
f = random.uniform(1.5, 9.8)
print(f'Radom floating point number: {f}')

# # program to generate random float numbers based on user input
# start_f = float(input('Enter a float number for the lowest value in range: '))
# stop_f = float(input('Enter a float number for the highest value in range: '))
# float_f = random.uniform(start_f, stop_f)
#
# print(f'Generate random float from to {start_f, stop_f}')
# print(f'The random float number is: {float_f}')

# picking random value from the list of values
# fruit_list = ['Apple', 'Banana', 'Pear', 'Plum', 'Grapes']
# print(f'Random choice is: {random.choice(fruit_list)}')

# program will generate the list of values based on user input
# and select a random value from the list

# fruit_list1 = []
# num = int(input(f'Enter the number of fruits in the basket: '))
# for d in range(num):
#     i = input(f'Enter fruit {d + 1} of {num}: ')
#     fruit_list1.append(i)
#
# print(f'Random choice is: {random.choice(fruit_list1)}')

# Random library summary
# for random integer - random.randint()
# for random floats - random.uniform()
# for random items from lists - random.choice()

# External library (does not come by default with Python installation)
# install additional library via Python Packages:
# 1. In Pycharm go to Python Packages, search for and install Faker library
# 2. Add to the top of the file: from faker import Faker
# 3. Initialze the library to use in our file, add to the top of the file: fake = Faker(locale='en_CA')
print('------------- Generate random values using Faker Library ---------------')
email = fake.email()
print(email)

email1 = fake.free_email()
print(email1)

address = fake.address()
print(address)

postal_code = fake.postalcode()
print(postal_code)

username = fake.user_name()
print(username)

password = fake.password()
print(password)

password30 = fake.password(length=30)
print(password30)

# program to generate a password based on user input
numchar = int(input(f'Please enter the number of characters for your password: '))
rng = int(input(f'How many passwods you want?: '))

for i in range(rng):
    pwd = fake.password(length=numchar)
    print(f'Here is your password {i + 1} of {rng}: {pwd}')
else:
    print(f'Password generation is done!')