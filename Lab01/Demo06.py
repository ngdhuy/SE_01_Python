# list in python
def main():
    my_list = [1, 2, 3]
    print(my_list)
    str_my_list = list('Hello mr Heo')
    print(str_my_list)

    a = []
    print(a)
    a.append(1)
    a.append(2)
    a.append(3)
    print(a)

    a.clear()
    print(a)

    a = [1, 2, 3]
    b = a
    print('a = ', a)
    print('b = ', b)

    a[2] = 8
    print('a = ', a)
    print('b = ', b)

    c = a.copy()
    print('a = ', a)
    print('c = ', c)

    a[2] = 3
    a.append(2)

    print('a = ', a)
    print('b = ', b)
    print('c = ', c)

    print('length of a = ', len(a))
    print('count of number 2 in a: ', a.count(2))
    print('Index of number 3 in a: ', a.index(3))

    b.reverse()
    print(a)

    b.insert(0, 8)
    b.insert(3, 99)
    print(b)

    a.extend(c)
    print(b)

    print(c)
    c[2] = 9999
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)

    d = a + c
    a[0] = 0
    print('d = ', d)
    print(d[-1])

    e = d.pop()
    print('d = ', d)
    print('e = ', e)

    d.remove(2)
    print('d = ', d)

    del d[1]
    print('d = ', d)

    d.sort()
    print('a = ', a)
    print('d = ', d)

    e = sorted(a)
    print('e = ', e)

    print('e[3, 6] = ', e[3:6])
    print('e[:3] = ', e[:3])
    print('e[3:] = ', e[3:])
    print('e[:-3] = ', e[:-3])
    print('e[-3:] = ', e[-3:])

    f = e[:]
    print('f = ', f)


if __name__ == '__main__':
    main()