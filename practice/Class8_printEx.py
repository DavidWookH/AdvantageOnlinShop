# #useful operation with variable in Python
# fname, lname, email ='James', 'Bond', 'agent007@gmail.com'
# print(fname)
# print(lname)
# print(email)
#
# #2. Assign the same value to 3 different variable
# price1 = price2 = price3 = 50
# print(price1)
# print(price2 / 2)
# print(price1 + price2 + price3)
#
# phrase = 'The Ultimate Answer to Life'
# num = 42
#
# print(f'Count of Characters : {len(phrase)}')
#
# # Da
#
# x=1
# y=2.0
# z='3'
#
# print (x)
# y=int(y)
# print(y)
# z=float(z)
# print(z*2)
#
# x=str(x)
# y=str(y)
# z=str(z)
#
# b=True
# print(b*2)
# f=False
# print(f*2)
#
#
# print('Hello,',input('Enter your Name: '))
# print(f"Hello,{input('Enter your Name: ')}")
# print(f'Hello,{input("Enter your Name: ")}')
# da
# 4. Dictionary
# Dictionary is a key:value pair collection type
# dictionaries are ordered (indexed), changeable, duplicates are not allowed
# created using curly braces

print('--------------- Dictionary example ---------------------')

# format # 1
student = {'name' : 'James Bond', 'id' : 1007, 'year' : 2002, 'cohort' : '3' }
student1 = {
    'name' : 'James Bond',
    'id' : 1007,
    'year' : 2002,
    'cohort' : '3'
}

# format # 2
new_user = {
    'username' : 'testuser007',
    'password' : 'Pass1',
    'firstname' : 'James',
    'lastname' : 'Bond',
    'email' : 'agent007@gmail.com'
}

# display all
print(student)
print(new_user)

# display keys only
print(student.keys())
print(new_user.keys())

# display items, key, value container
print(student.items())
print(new_user.items())

# display values only
print(student.values())
print(new_user.values())

# change the value of key
# method 1
student.update({'cohort' : 2})
new_user.update({'password' : 'Pwd3!'})

print(student)
print(new_user)

# method 2
# update value for specified key
student['year'] = 2022
new_user['email'] = 'agent_007@yahoo.com'

print(student)
print(new_user)