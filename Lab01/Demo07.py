# loop command on python
def demoFOR(arr):
    for i in arr:
        print(i)
    else:
        print("End of FOR")


def demoWHILE(arr):
    i = 0
    while i < len(arr):
        print(arr[i])
        i += 1
    else:
        print("End of WHILE")


def main():
    arr = [1, 2, 3, 4, 5]
    demoFOR(arr)
    demoWHILE(arr)


if __name__ == "__main__":
    main()