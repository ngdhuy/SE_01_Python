def f_revert_string(string):
    str_result = ""

    middle_index = int(len(string) / 2)
    for i in range(middle_index):
        str_result += string[middle_index - 1 - i]

    if len(string) % 2 != 0:
        str_result += string[middle_index]

    for i in range(middle_index):
        str_result += string[len(string) - 1 - i]
    return str_result


def main():
    print("Revert array")
    string = "123456789"

    str_result = f_revert_string(string)
    print(str_result)


if __name__ == "__main__":
    main()