for i in range(100):
    count = i + 1
    print(count)

    if count % 3 == 0:
        print ('fizz')
    elif count % 5 == 0:
        print('buzz')
    else:
        print('count')
