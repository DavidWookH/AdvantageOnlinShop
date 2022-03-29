# #Conditional Statements in Pytho
#
# # Comparison operators
#
# # When we use comparison operators the result
# # is true or Force
#
# print (3<5)
# print (5<3)
# #less than equal
# print (6<=9)
# print (6<=6)
# print (6<=4)
#
# # greater than
# print (10>2)
# print (2<10)
# # greater than or equal >=
# print (10>=9)
# print (10>=20)
#
# # Equal ==
# # Assignment operator single equal sign var = val
# # Comparison operator double equal sign var == val
#
# print (5==5)
#
# # not equal !=
#
# print(5!=5)  # expect false
# print (5!=6)  # giveus true
#

# example 1 .
#expected_title = 'CCTB - Welcome!'
#actual_title = '404- Page Not Found'


#print(expected_title==actual_title)
# if [condition] :
#     code to excution if the condition statement is true
     #
     # elif
     # elif
     # else :
             #code to excute for any other situtation

# indent - tab
# unindent - shift + tab
# expected_title = 'CCTB - Welcome!'
# actual_title = 'CCTB - Welcome!'
#
# if expected_title == actual_title:
#     print(f'Yey! CCTB Website is launched')
# else:
#     print(f'Website is down ! Contact your system admin')


# age = 15
# age =int(input('Please enter your age :'))
#
# if age > 20 and age <= 40:
#     print(f'Your age is {age} not bad!, you can play following games : G1,G2, G3' )
# elif age > 11 and age <= 20:
#     print(f'Your age is {age} cool!, you can play following games : G4,G5, G6')
# else:
#     print('have a nice day')

# if your_age.isnumeric():
#    if age > int(your_age):
#        print(f'Your age {your_age} is less than {age}')
#    elif age < int(your_age):
#        print(f'Your age {your_age} is less than {age}')
#        int(your_age)> 0 and int(your_age)<=age: # 0 - 15
#        print(f'your_age)
# # =int (your_age)
# print (your_age)
#
# if type(your_age) != str:
#     if age >= your_age:
#         print(f'Your age {your_age} is less than or equal {age} ')
#     elif age < your_age:
#         print(f'Your age {your_age} is greater than than or equal {age} ')
#     else:
#         print('Please enter number')
#
# age = 18
# your_age = input('Please enter your age:')
# if your_age.isnumeric() or your_age[0] == '-':
#     if age > int(your_age) and int(your_age) > 0:
#         print(f'Your age {your_age} is less than {age}')
#     elif age < int(your_age):
#         print(f'Your age {your_age} is greater than {age}')
#     elif age == int(your_age):
#         print(f'Your age {your_age} is equal to {age}')
#     else:
#         print(f'Your age is not valid.')
# else:
#     print(f'Your age is not number try again.')

lang_dictionary = {
    'English' : 'Hello',
    'Persian' : 'Salam'
}
national = input("enter your nationality:")
if lang_dictionary.keys().__contains__(national):
    print(lang_dictionary.get(national))
else:
    print("not here")