def pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, ' ', end = '')
        print('')

def main():
    n = int(input('Enter a integer number = '))
    pyramid(n)

if __name__ == "__main__":
    main()