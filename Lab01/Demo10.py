# from MyLib.myFunc import *

import MyLib.myFunc as f

def main():
    a = 1
    b = 2
    # c = f.sum(a, b)
    # print(c)

    d = f.getAllData()
    print(d)


if __name__ == "__main__":
    main()