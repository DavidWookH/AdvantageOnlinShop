# # Four collection data types : LIST SET TUPLE DICTIONARY
# #----------------------------------------------------------
# # 1. List
# # 2.
# #list_of_something = [ ]
#
# list_of_names = ['Luke','Leia','Aniken', 'Padme']
#
# print(list_of_names)
#
# print(list_of_names[0])
#
# list_of_names[2]='Darth Vader'
#
# print(list_of_names)
#
# list_of_names.append('Ray')
#
# print(list_of_names)
#
# tropical_list = ['Durian','Mangosteen','Cherimoya','Lychee']
# #
# print(tropical_list)
# # if=0
#
# for fruit in tropical_list:
#     print(fruit)
#
# print('-----------------------------')
# for i in range(len(tropical_list)):
#     print(f'{i}:{tropical_list[i]}')
#------------------------------------------
# 2. Tuples.. Two in pair
# Tuples are unchangeable, you cannot add, remove items from the tuple
# think of tuples as  a list of constants
# if you need to change a tuple, you can convert it
# to a list then change, then convert back to tuple
#

print('-----------------------------')
yummy_tupple =('apple','banana','mange','grapes','pear')
print(yummy_tupple)

# print items from tuple on the new line using for lop
for yt in yummy_tupple:
    print(yt)

#print a second item from the tuple (index starts with zero)
print(yummy_tupple[1])

yummy_list=list(yummy_tupple)
print(yummy_list)

yummy_list.pop(4) # remove 5th item
print(yummy_list)
print ('------------------set Example -----------------')

yummy_set ={'apple','pear','plum','melon','grapes','pear'}
print('yummy set=', yummy_set)

for ys in yummy_set:
    print(ys)
print ('------------------End Example -----------------')

