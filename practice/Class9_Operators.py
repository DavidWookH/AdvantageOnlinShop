# #VARIABLE TYPES a type casting review
# # when we convert one variable to another in Python, it's called Type Casting
# int() # to covert/cast to integer
# float() # to convert/cast to floating point number
# str() # to convert/cast to string
# bool () # to convert/cast into boolean (logical variable type)
#
# #Example 1 Convert data type to integers
# a =int('5')
# b=int(3.14159)
# c= int(9)
#
# print(a, b, a*2)
#
# #Example 2 Convert data type to integers
# d = float('1')
# e = float(9.69)
# f = float('2022')
# g = float('20349.923')
# print(d,e,f,g)
#
# #Example 3. Convert data type into string
# h = str('gh234')
# i = str(89)
# j = str(56.0*2)
# k = str(True*3)
# print(h,i,j,k)

# #Example 4. We want to control decimal points in floating point numbers
# pi=3.14159
# print('Hello %s' % 'World')
# print('The number of pi is :%f' % pi)
# print('The number of pi is :%.2f' % pi)
# print('The number of pi is :%.3f' % pi)
# print(round(pi))

## ------------------ PYTHON OPERATORS -----------------------
## Assignment / Re-assignment operators
## Assignment '=' single eual sign
# # 1. Single Assignment
# college ='CCTB'
# number_of_students =30
# duration_of_class =45
# in_session = True
# print(f'College name', college)
# print(f'Number of Student in class:{number_of_students}')
# print(f'Duration of class:{duration_of_class}')
# print(f'Class is currently in session:{in_session}')

# #2.
# # Basic math operator in multiplication
# #  * - single multiplication
# print (2*5)
# print (2**5)  # 2*2*2*2*2  2 to the power 5
#
# # / - regular division / float division -single forward slash
#
# print (100/2)
# print (234.6/3)
#
# # // - integer division - two forward slashes
# print (100//2)
# print(23.666//3)
#
#
# print(10%4)
#
# print(15%12)

#PEMDAS
# P - Parenthesis
# E - Exponents
# MD - Multiplication, Division, left to right
# AD - Addition, Subtraction, left to right

# PEMDAS
print((10/2)**3 + 25 - 100)
