def main():
    a = 5       # integer
    b = 6.5     # float
    c = a + b
    print(c)

    d = int(c)
    print(d)

    e = a + d
    f = a - d
    g = a * d
    h = a / d
    z = a % d

    print(f'e = {e}, f = {f}, g = {g}, h = {h}, z = {z}')

    i = 4       # SQRT(4, 2)
    j = 2       # 4^2

    k = i // j
    l = i ** j

    print(f'k = {k}, l = {l}')

    m = 5
    n = 2
    o = m / n
    p = int(m / n)

    print(f'o = {o}, p = {p}')

    r = 5
    r += 2
    print(f'r = {r}')

    r -= 2
    print(f'r = {r}')

    r *= 2
    print(f'r = {r}')

    r /= 2
    print(f'r = {r}')



if __name__ == '__main__':
    main()