# String method

def main():
    name = 'MiKe'
    first_name = 'Peter'
    last_name = "Driscoll"
    mutiple_line = '''Nguyen
                    Duc
                    Huy'''
    print(name)
    print(first_name, last_name)
    print(mutiple_line)

    num = 5
    sNum = str(num)
    s = '''
        abc\b -> \\b
        \n -> \\n
        \r -> \\r
        \t -> \\t
    '''
    print(s)

    name = 'nguyen duc huy'
    print(name.capitalize())
    print(name.upper())
    print(name.lower())

    print(dir('.'))

    my_str = 'This is a string of words'
    print(my_str)

    arrString = my_str.split('s')
    print(arrString)

    print('Welcome %s - %s' % (first_name, last_name))
    print('Welcome %(first)s %(last)s - %(first)s' % {'last': last_name, 'first': first_name })
    age = 18
    print('Hello {}, You must be at least {} to continue!'.format(name, age))
    print('Hello {age}, You must be at least {name} to continue!'.format(**{'name': name, 'age': age}))

    my_string = 'this is the sentence.'
    print('It is \'{:>40}\' OK'.format(my_string))
    print('It is \'{:<40}\' OK'.format(my_string))
    print('It is \'{:^40}\' OK'.format(my_string))

    a = 10
    b = 8.8

    print(f'Mr {name} have {a} point and {b} money')

    # define anonymous object
    my_dict = {'id': 1, 'name': 'Harry Potters'}
    str_my_dict = f'This is book with title {my_dict["name"]} with ID = {my_dict["id"]}'
    print(str_my_dict)

    full_name = first_name + ' ' + last_name
    print(full_name)

    full_name = ''.join([first_name, ' ', last_name])
    print(full_name)

    print(full_name[0:4])
    print(full_name[:4])
    print(full_name[4:])
    print(full_name[-4:])


if __name__ == '__main__':
    main()