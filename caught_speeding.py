speed = int(input('how fast is he going? '))
day = input('is it his birthday? ')
if day == 'yes' and speed < 36:
    print('no ticket')
elif day == 'no' and speed < 31:
    print('no ticket')
elif day == 'yes' and speed > 35 and speed < 56:
    print('small ticket')
elif day == 'no' and speed > 35 and speed < 56:
    print('small ticket')
elif day == 'yes' and speed > 55:
    print('big ticket')
elif day == 'no' and speed > 50:
    print('big ticket')
    
    
