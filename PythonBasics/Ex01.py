number = int(input('Input an integer number: '))

if number < 0:
    print(f'{number} < 0')
elif number >= 0 and number <= 10:
    for i in range(number, 11):
        if i != number:
            print(' ', end='')
        print(i, end='')
    print()
elif number > 10:
    print(f'{number} > 10')
