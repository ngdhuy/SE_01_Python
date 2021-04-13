# Tuples in python
def swap(m, n, k):
    temp = m
    m = n
    n = k
    k = temp
    return m, n, k


def main():
    a = (1, "iPhone 12 Pro Max", 1.8, 1)
    print(a)
    print(a[1])
    print(a.index(1.8))
    print(a.count(1))

    b = a + (999, 888)
    print(b)

    m = 1
    n = 2
    k = 3
    m, n, k = swap(m, n, k)
    print(m, n, k)


if __name__ == "__main__":
    main()