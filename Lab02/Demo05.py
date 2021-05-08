def isPrimeNumber(n):
    if n < 2:
        return False

    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    else:
        return True


def main():
    n = int(input('Enter a integer number: '))
    prime_number = isPrimeNumber(n)
    print(prime_number)


if __name__ == "__main__":
    main()