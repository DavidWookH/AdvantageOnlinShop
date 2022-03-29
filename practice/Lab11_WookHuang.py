# Do the following tasks.
# 1. Create a program in Python and use try and catch/except.
# 2. Simulate error and catch it using except keyword
# 3. Use finally keyword to finalize the statement.
# b) Do not use any variable names or values from the class's code. Scripts with non-unique vars and values will be declined.

print("*--------------------------------------------------*")
print(" Lab11 Assignment try/except/finally by Wook Huang ")
print("*-------------------------------------------------*")

# number = None
valid_flag = False

Superhero_Movies = ['Iron-man', 'Hulk', 'Thor','Spider-man', 'Captain America', 'Dr.Strange', 'Black Widow']
for i in range(len(Superhero_Movies)):
    print(f'{i} {Superhero_Movies[i]}')
print("*----------------------------------------------*")

numlist=len(Superhero_Movies)

while numlist:
    try:
        number = int(input('Please enter the Movie number for you to rent : ')) # keep promting for a number
        while number >=0 and number <= numlist-1:  # check the choice \ is within the range
            print(f'Your choice is good! You chose {Superhero_Movies[number]} ')
            Superhero_Movies.pop(number)
            break
        else:
            print(f'Your number is {number} is not from a given range. Please try again')
    except ValueError as e:
        print(f'You entered non integer. Please try again') # raise an error if a non integer value is entered
        print(f'Error message:{e}')
    finally:
        print('-----------------------****--------------------------')
    for i in range(len(Superhero_Movies)):
        print(f'{i} {Superhero_Movies[i]}')
    numlist = len(Superhero_Movies)
print('Sorry No more movies to rent, Good Bye !!!!  ')
print('-----------------------------------------------------')
