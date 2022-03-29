# Comments in Python Language are line of text preceeded with the number sign #
# if you want to comment multiple lines
# select the lines you want to comment and press ctrl+? - windows Cmd+? on Mac

# display 'Hello World' with Python

print('Hello, World!')

# printing with Python Practice
# printing is done with the built-in print() method

print('Python is awesome!')
print('The page is loaded!')
print('We ar learning Python!')

#another way to print
print('Hello', 'world', 2022, '!')
#printing string (words) and number together
#Method 1 - concatenation
# to print string and number together
# number need to be converted to the string str() -- lagacy waty to pring letters and numbers together
print('Today Year: '+ str(2022))

# Method 2 - separating values with
print('Today Year:',2022)

#practice method 2
print('Days in a week: ' + str(7)) # method 1, with str conv. space is needed
print('Days in a week:',7)  # comma provide space

# print combination of multiple strings and integers in one line
print('I came to Canada in', 1991, '. but I was in and out of Canada for the next 15years.', 'I worked for samsung from', 2004, 'to', 2020)
print('I came back to Vancouver in', 2020, 'So I have been away from Canada for', 29, 'years')

#---------------------------------------------------
# Task #1.
print('Hello!, Phython is  programming course in CCTB')
# Task #2
# Task #3
print('Squidward has', 6,'tentacles')

# Task #4
print('Does Squidward have', 8,'tentacles','?')

ty_msg = 'Thank you for buying with Advantage!'
track_num = 92384792
order_num = 39503450


print('Method 4: %s Your tracking number is %s. Your order number is %s' % (ty_msg, track_num, order_num))
n = 7
m=7
print(f'We are open {n} days a week')
print(f'What is {m}')