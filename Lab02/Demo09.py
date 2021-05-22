import random
def f_encrypt(adn):
    strResult = ""
    for c in range(len(adn)):
        char = adn[c]
        flag = random.randint(0, 1)
        if flag == 0:
            encrypt = str(random.randint(0, 9))
        else:
            temp = random.randint(0, 26)
            arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W', 'X', 'Y', 'Z']
            encrypt = arr[temp]
        strResult += char + encrypt
    return strResult


def f_decrypt(adn):
    strResult = ""
    for i in range(len(adn)):
        if i % 2 == 0:
            strResult += adn[i]
    return strResult


def main():
    adn = "ATUGC"
    str_encrypt = f_encrypt(adn)
    print(str_encrypt)
    str_decrypt = f_decrypt(str_encrypt)
    print(str_decrypt)




if __name__ == "__main__":
    main()