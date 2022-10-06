if __name__ == '__main__':
    number = int(input('Enter a number: '))
    total = 0
    # print('The factors are:', end=' ')
    for divide in range(1, number):
        if number % divide == 0:
            total += divide
            print(divide, end=' ')
    print('\nThe sum of the factors is:', total)
    if total == number:
        print('It is a perfect number')
    else:
        print('It is not a perfect number.')
