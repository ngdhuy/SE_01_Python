def revertNumber(n):
    result = 0
    while n != 0:
        result = (result * 10) + (n % 10)
        n = n // 10
    else:
        return result


def main():
    n = int(input('Enter a integer number: '))
    result = revertNumber(n)
    print(result)


if __name__ == "__main__":
    main()