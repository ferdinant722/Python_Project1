result = int(input('Enter your Grade?: '))

if 0 <= result <= 100:
    if result > 79:
        print('Invalid grade. Please enter a value below 80.')
    elif result > 69:
        print('Your Grade is B')
    elif result > 59:
        print('Your Grade is C')
    elif result > 49:
        print('Your Grade is D+')
    elif result > 39:
        print('Your Grade is D')
    else:
        print('Your Grade is F')
else:
    print('Invalid input. Please enter a value between 0 and 100.')