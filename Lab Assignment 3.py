def guesser():
    r3, r5, r7 = 'a', 'a', 'a'
    print('Welcome to the Flarsheim Guesser!\n')
    print('Please think of a number between and including 1 and 100.\n')
    while r3 == 'a':
        r3 = int(input('What is the remainder when your number is divided by 3 ?'))
    if r3 > 3:
        print('The value entered must be less than 3')
        r3 = 'a'
    elif r3 < 0:
        print('The value entered must be more than 0')
        r3 = 'a'
    while r5 == 'a':
        r5 = int(input('What is the remainder when your number is divided by 5 ?'))
    if r5 > 5:
        print('The value entered must be less than 3')
        r5 = 'a'
    elif r5 < 0:
        print('The value entered must be more than 0')
        r5 = 'a'
    while r7 == 'a':
        r7 = int(input('What is the remainder when your number is divided by 7 ?'))
    if r7 > 7:
        print('The value entered must be less than 3')
        r7 = 'a'
    elif r7 < 0:
        print('The value entered must be more than 0')
        r7 = 'a'
    for i in range(101):
        if i%3 == r3:
            if i%5 == r5:
                if i%7 == r7:
                    return i
cont = 'Y'
while cont == 'Y':
    print(f'Your number was {guesser()}')
    cont = input('How amazing is that?\n\nDo you want to play again? Y to continue, N to quit ==>')