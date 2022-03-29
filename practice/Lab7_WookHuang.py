print('-----------------------------------------------------------')
print("1. Display any 5 strings in one line using the print() command")
print('Information System Analysis Quality Management')
print('-----------------------------------------------------------')

print("2. Display any 5 integers in one line using the print() command")
print(000,111,222,333,444,555)
print('-----------------------------------------------------------')

print("3. Display any 5 float numbers in one line using the print() command")
print(0.009,1.11,22.2,3.33,44.40,55.005)
print('-----------------------------------------------------------')

print("4. Display a combination of integers and strings in one line")
print('I came to Canada in', 1991, 'and lived in and out of Canada until', 2004, '. I worked for samsung from', 2004, 'to', 2020 , ' and return to Vancouver.')
print('-----------------------------------------------------------')

print("5. Define a few variables and give an example on how to use f'' formatting strings (display strings and numeric variables)")
x,y=1991, 2004
sentence1 = 'and lived in and out of Canada until'
print(f'I came to Canada in {x} {sentence1} {y}')
print('-----------------------------------------------------------')
# f - formatting is to insert string or integer within script
print("6. Display in one print command 5 strings, 5 integers, 5 float numbers, and 2 Boolean values together")
print('The best 5 semiconductor companies (like(True)/dislike(False)): ', 1,'TSMC',124.71,True,2,'NVIDIA',258.24,True, 3,'ASML',656.88,True, 4,'Broadcom',591.36, False, 5,'Intel', 48.86,False)
print('-----------------------------------------------------------')
print("7. Combine print and input together in one line")
print(f'After ISAQM program, I want to work for  {input("Which company do you want work for in Vancouver?: ")}')
print('-----------------------------------------------------------')
print("8. Provide multiple inputs in one go")
a, b, c, d = input('Enter four different values separated by space: ').split()
print(a,b,c,d)
print('-----------------------------------------------------------')
print("9. Reversing a string in Python")
food = input('Enter your favorite food : ')
print('revered food name:',food[::-1])
print('-----------------------------------------------------------')
print("10. In-Place Swapping Of Two Numbers")
x, y = 1700000, 50
print(x, y)
x, y = y, x
print(x, y)
print('-----------------------------------------------------------')
print('11. Check The Memory Usage Of the Variable')
import sys
CanAnthem = ' O Canada! Our home and native land! True patriot love in all of us command. With glowing hearts we see thee rise,'\
            'The True North strong and free! From far and wide, O Canada, We stand on guard for thee.'\
            'God keep our land glorious and free! O Canada, we stand on guard for thee.'
print(CanAnthem)
print(f'Canada Anthems Memory Usage in bytes: {sys.getsizeof(CanAnthem)}')
print('-----------------------------------------------------------')
print(" 12. Print string N times")
n = 3
c = 'O Canada!'
s = ' '
print((c + s) * 3)
print('-----------------------------------------------------------')
print(" 13. Splitting a string into a list")
conf_msg = 'Information System Analysis and Quality Management'
print(conf_msg)
conf_msg_split = conf_msg.split()
print(conf_msg_split)
print('-----------------------------------------------------------')

print("14. Display multiple input values in a single line")
name, color, q = input('Enter first name, favorite color and height(cm) separated by space: ').split()
print(f'First Name: {name}, Color: {color}, Quantity:{q}','cm' )
print('-----------------------------------------------------------')
print("15. Give 3 incorrect names of the variables")
print("1. starting with number :  1agent  000party etc ")
print("2. starting with special character  :  $$$moneytaker , @$%834$$%%, %(*")
print("2. starting with foreign character  :  한국korea, 떡볶이Ricecake, 치킨chicken")

print('-----------------------------------------------------------')
print("16. Give 3 correct names of the variables")
print("1. var0001 (lower case with number) 2.Var_1, (underscore) 3.var1234_hw (combination) ")
print('-----------------------------------------------------------')
print("17. What is the purpose of using variables?")
print('Variables is used to store data for programming.The user place useful information in the variables.')
print('The purpose is to wirte flexible programs. (reduce repetion, scaling, proces different data sets and types)')
print('-----------------------------------------------------------')
print("18. How can we define a constant variable? Give an example.")
print("A constant is a type of variable whose value cannot be changed.")
print("To distinguish, UPPER CASE LETTERS ARE USED FOR CONSTANTS")
print(" Example: HOURS_OF_A_DAY, DAYS_IN_YEAR, PI")
print('-----------------------------------------------------------')
print(" 19. What reserved Python keywords we can't use to define variables? Provide as many examples as you can.")
print(" False	def	if	raise None	del	import	return True	elif in	try and	else is	while as except	lambda	with")
print(" assert	finally	nonlocal yield break for not	class from or continue	global	pass")
print('-----------------------------------------------------------')
