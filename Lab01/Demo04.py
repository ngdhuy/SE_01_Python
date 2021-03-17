def main():
    value = int(input('Enter an integer number: '))

    if value % 2 == 0:
        print(f'{value} is Even')
    else:
        print(f'{value} is Odd')

    if value == 1:
        print('One')
    elif value == 2:
        print('Two')
    elif value == 3:
        print('Three')
    elif value == 4:
        print('Four')
    elif value == 5:
        print('Five')
    elif value == 6:
        print('Six')
    elif value == 7:
        print('Seven')
    elif value == 8:
        print('Eight')
    elif value == 9:
        print('Nine')
    else:
        print('Invalid number')


if __name__ == '__main__':
    main()