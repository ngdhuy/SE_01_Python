def main():
    a = 10
    print('Value of a = ', a)

    b = int(input("Enter an integer number b = "))
    print("b = ", b)

    c = float(input("Enter a float number c = "))
    print("c = ", c)

    d = b + c
    print("d =  " + str(b) + " + " + str(c) + "  = ", d)

    t = "Marry"
    print(f'Hello {t}, this is a value of d = {d}')


if __name__ == '__main__':
    main()