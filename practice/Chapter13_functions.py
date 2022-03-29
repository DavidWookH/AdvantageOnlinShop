# # Functions in Python
#
# # in Python functions are created with 'def'
#
# # define a funtion
#
# def friendly_message():
#     print('Hello from a function!')
#
# # call a function
#
# friendly_message()

#function with arguments
#information can be passed to function as arguments
# # arguments are specified after the function name insiede parentheses
# # you can have as many arguments as you need, separate arguments by comma
#
# def another_friendly_message(message):
#     print(message)
#
# # another_friendly_message('Hello again from function')
# # another_friendly_message('And hello one more time')
# # another_friendly_message('again and again')
#
# #multiple arguments
# def yet_another_message(message,count):
#     for i in range(count):
#         print(f'{i+1} - {message}')
#
# yet_another_message('Hello world!',5)
#
#
# yet_another_message('Hello world!',5)

# #.1. Calculation program using prompt or direct entry
# # program will have a function with arguments
#
# def calculation(a, b, c, d):
#     print(f'the sum of {a} and {b} is : {a + b}')
#     print(f'the product of {c} and {d} is : {c * d}')
#
# calculation (3,7,5,9)

def prompt(n):
    return int(input(f'Enter a number {n}: '))

# # calculation (prompt(1), prompt(2), prompt(3), prompt(4))
# # passing a list of values to the functions as arguments
# num_list = [5,7,9,4]
# calculation(*num_list) #use *List unpacking operator
# # example of function with if statements
# # Calculation function

def calc(a, b, sign):
    if sign == '+':
        print(f'The result of addition is " {a + b}')
    elif sign == '-':
        print(f'The result of subtraction is " {a - b}')
    elif sign == '*':
        print(f'The result of multiplication is " {a * b}')
    elif sign == '/':
        print(f'The result of float division is " {a / b} "')
    elif sign == '//':
        print(f'The result of integer division is " {a // b} "')
    else:
        print(f'Something is wrong, Please check the argumetns {a,b, sign}')

# #Addition
# cal(3,4,'+')
#
# #Subtraction
# cal(3,4,'-')
#
# #Multiplication
# cal(3,4,'*')
#
# #Float Divisiton
# cal(3,4,'/')
#
# #Integer Division
calc(prompt(1),prompt(2),'*')
#
# # calc(5,6, input(f'sign operator:'))
#
# def prompt1(n)
#     return int(input(f' Enter {n}:'))
#
# # calc(int(input('Enter a number: ')), int(input(
#
# calc(int(prompt1('number'), int(prompt1('another number')), prompt1('sign operator'))