# 1. Create a new program in PyCharm where you will check the current weather and
#    display funny messages based on user input.
# 2. If the user enters integer values more than 0 but less than 15 degrees,
#    display a message to wear something related to that weather condition.
# 3. If the user enters integer values more than 15 but less than 35 degrees,
#    display a message to wear something related to that weather condition.
# 4. If the user enters integer values more than 35 degrees,
#    display a message to wear something related to that weather condition.
# 5. If the user enters integer values less than 0 degrees,
#    display a message to wear something related to that weather condition.

current_temp = float(input('Please enter current outside temperature of your area (in degree Celcius):'))

if current_temp > 0 and current_temp <= 15:
    print(f'The current temperature is {current_temp} degree Celcius.'
           'It\'s still cold outside, Pack your parka, jacket or leather jacket to keep you warm.')
elif current_temp > 15 and current_temp <= 35:
    print(f'The current temperature is {current_temp} degree Celcius.'
           'Wear something light. Your favorite jeans, sandals, and printed T-shirts with your artist')
elif current_temp > 35:
    print(f'The current temperature is {current_temp} degree Celcius.'' You know it is hot summer! don\'t forget your sunglasses and sunblocks with your mini or maxi dress ')
else:
    print(f'The temperature is below 0 degree, It is cold enough to go skiing on Cypress Mountain!')

