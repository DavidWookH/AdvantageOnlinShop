#Loop in Python
#1 : For Loop
# In python .. For loops are used to iterate over a sequence (String, list, or tuple, or set)
# # 1. PRint individual letters of a string
# word ='Python'
# for letter in word:
# #     print(letter)
#
# for x in range (10):
#     print(f'{x} Hello,World')

# word ='Python'
# for x in range(len(word)):
#     print(x,word[x])
#
#
# word2=input('Please enter a word:')
# for l in word2:
#     print(l)

# 3. Use for loop to iterate over Python list of tuple
# # make a list with [] square breackets
# music_genres = ['Electronic','Jazz','Classical','Oldies','Blues']
# for g in music_genres:
#     print(g)
#
# for g in music_genres:
#     print(f'--------{g}------------')
#     for l in g:
#         print(l)
#
# music_tuple = ('Electronic','Jazz','Classical','Oldies','Blues')
# for i in range(len(music_tuple)):
#     print(f'{i},{music_tuple[i]}')

# # list example
# tropical_list=['Durian','Mango','Jackfruit','Cherimoya','Lychee']
# for i in range(len(tropical_list)):
#     print(f'{i},{tropical_list[i]}')
#
# for i in range(1,3):
# #     print(f'{i},{tropical_list[i]}')
#
# # WE can use the loop with else statement
# digit_list=[6,4,5,8,9,1,7,3]
# print(f'Start of List.')
# for i in digit_list:
#     print(i)
# else:
#     print(f'End of List.')
#
# grades ={'James':90,'Julie':89,'Brandon':93}
# student_name =input('Please enter student Name:')
# for student in grades:
#     if student == student_name:
#         print(f'{student_name} grade is : {grades[student]}')
#         break
# else:
#         print(f'Studen {student_name} grade is : {grades[student]}')

# #2. While loop #####################
# # While loop in Python is used to iterate over a block of code
# # as long as the test expression (or condition) is true(of false, depends on what we check)
# number =10
# var =10
#
# while var != number: #while number is true
#         var = var + 1
#         print(var)

# Simple program to start at 1 and stop at 100

# num=1
# step = 3
#
# while num < 100 :
#     num = num+step
# #     print(num)
# print('-----Simple program to start at 1 and stop at 100 ---------------')
# num=1
# step = 20

# while num < 100 :
#     #num = num+step #legacy method to add number
#     num +=step  #more modern method
#     print(num)

# Program to add number up to ..
# take a number from a use
## n=int(input('Enter a number: '))

# #initialize total and counter
# total=0
# counter = 1
# print(f'Before Total: {total}, Before Counter: {counter}\n')
# while counter <= n:
#     total += counter
#     counter += 1
#     print(f'Total: {total}, Counter: {counter}\n')
# print(f'This is our total: {total}')





# #Make a counter program using while loop
# counter = 0
# step = int(input('Enger number of iteration: '))
#
# while counter <= step:
#     print(f'This is inside loop. Iteration number is {counter}')
#     counter += 1
# else: print(f'done checked !!!! ')


# num1 = 0
#
# for num1 in range(0,3):
#     print(f'-------Number 1: {num1}----------')
#     for num2 in range(0,3):
#         print(f'Number 2: {num2}')

# program that check if the number is in the given range
# program requirement:
# check if the entry is integer
# check if the entry is in rage
# keep prompting to enter a number until
# the correct value is entered

valid_flag = False

while not valid_flag:
    number = int(input('Please enter a number from 1 to 10: '))
    while number > 0 and number <=10:
        print(f'All is good! Your number is {number} is from 1 to 10')
        valid_flag=True
        break
    else:
        print(f'Your number is {number} is not from a given range. Please try again')

