def isPerfectNumber(n):
    if n < 0:
        return False

    for i in range(1, n // 2 + 1):
        if i ** 2 == n:
            return True
    else:
        return False

def main():
    n = int(input('Enter a integer number: '))
    perfect_number = isPerfectNumber(n)
    print(perfect_number)


if __name__ == "__main__":
    main()