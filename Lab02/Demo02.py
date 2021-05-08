def SumDigit(n):
    sum = 0
    while n != 0:
        sum = sum + (n % 10)
        n = n // 10
    else:
        return sum


def main():
    n = int(input('Enter a integer number = '))
    sum = SumDigit(n)
    print(sum)


if __name__ == "__main__":
    main()