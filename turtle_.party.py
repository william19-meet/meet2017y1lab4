strawberries = int(input('how many strawberries do you have? '))
day = input('is it weekday or weekend? ')
if day == 'weekday' and strawberries >= 39 and strawberries <= 61:
    print('fun')
elif day == 'weekend' and strawberries >= 39:
    print('fun')
else:
    print('no fun')
    
    
