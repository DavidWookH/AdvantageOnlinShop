import random
#Program 4 import Faker
from faker import Faker
fake = Faker(locale='en_CA')


print("*-------------------------------------------------------*")
print(" Lab12 Assignment  functions and Import  by Wook Huang ")
print("*-------------------------------------------------------*")

print("Program 1: Create a program with addition between number (no arguments) ")

def func_add():
    x= 15
    y= 20
    z= x + y
    print(f'The addition between number {x} and {y} is {z}')
func_add()

print("*----------------------------------------------'---------*")
print("Program 2: Create a program, define a function with arguments")
print("         : and calculate multiplication between numbers.")

def calc_mult(num1, num2):
    num_mult = num1*num2
    print(f'the product of {num1} and {num2} is : {num_mult}')

calc_mult (10,5)
calc_mult (1,0)
calc_mult (100,1000)

print("*----------------------------------------------------------------------*")
print("Program 3: random calculation between 2 numbers.        ")
print("           Prompt a user to enter number 1, then number 2")
print("           list[] of math operators (+,-,*,/,//) ")
print("           use random.choice() function to select a random op")
print("           complete the calculation with friendly message " )
print("           --- Use random library import.")
print("           --- Use try, except, finally to catch a ny input errors.")
print("*-----------------------------------------------------------------------*")

def prompt(n):
    return int(input(f'Enter a number {n}: '))

def calc_opr_random(a1_num, a2_num):
    math_op_list = ['+', '-', '*', '/', '//']
    try:
        print(f'Your first numbers is {a1_num}, and second number is {a2_num}' )
        # print(" input condition : inputs must be greater than or equal to 0")
        op_sign = random.choice(math_op_list)
        if op_sign == '+':
            print(f'The Random choice of math operation is "Addition".')
            print(f'The result of {a1_num} + {a2_num} is  {a1_num + a2_num}')
            print('---------------------------------------------------------')
        elif op_sign == '-':
            print(f'The Random choice of math operation is "Subtraction".')
            print(f'The result of {a1_num} - {a2_num} is  {a1_num - a2_num}')
            print('---------------------------------------------------------')
        elif op_sign == '*':
            print(f'The Random choice of math operation is "Multiplication".')
            print(f'The result of {a1_num} * {a2_num} is  {a1_num * a2_num}')
            print('---------------------------------------------------------')
        elif op_sign == '/':
            print(f'The Random choice of math operation is "Float Division".')
            print(f'The result of {a1_num} / {a2_num} is  {a1_num / a2_num}')
            print('---------------------------------------------------------')
        elif op_sign == '//':
            print(f'The Random choice of math operation is "Integer Division".')
            print(f'The result of {a1_num} // {a2_num} is  {a1_num // a2_num}')
            print('---------------------------------------------------------')
        else:
            print(f'Something is wrong, Please check ! ')
    except ValueError as e1:
          print(f'There is non-integer in your input. Please to run code again') # raise an error if a non integer value is entered
          print(f'Error message:{e1}')
    except ZeroDivisionError as e2:
          print(f'Your are not allow to divide by zero : {e2}')
    finally:
          print('-*-The Program is ended, so is Program 3  ----------*-')

    #print(f'The result {a1_num + a2_num}')
    #print(math_op_list)
#calc_opr_random(10,15)
#calc_opr_random(0,1)

calc_opr_random(prompt(1),prompt(2))

#
print("*---------------------------------------------------------------------------*")
print("Program 4: define a function for a random password based on ")
print("           the user-provided number of characters using the Faker library.")
print("           Use import and initialize the Faker library. ")
print("           Use try, except, finally to catch any input errors.")
print("*---------------------------------------------------------------------------*")


def prom_len(n):
    return int(input(f'Please enter the length for your password {n} : '))

#programs to generate a password based on user input


def ran_pwd(len1):
    try:
        if len1 > 0:
           print(f'Your password is length of  {len1} .')
           pwd = fake.password(length=len1)
           print(f'Here is your password: {pwd}')
        else:
           print(f'Your number is {len1} is not from a given range. Good Bye')

    except ValueError as e:
           print(f'You entered non integer. Please try again')
           print(f'Error message:{e}')
    finally:
            print('*-Program 4 is ended -------------------------------------*')
    #  valid_flag1=True
    # pwd = fake.password(length=len1)
    # print(f'Here is your password: {pwd}')
print("*---------------------------------------------------------------------------*")

ran_pwd(prom_len(1))