"""
String in python
"""
from Module.Module08 import *


def main():
    file_input = "Data/input.txt"
    file_output = "Data/output.txt"

    string = read_file(file_input)
    print(string)
    str_upper = uppercase(string)
    print(str_upper)
    str_lower = lowercase(str_upper)
    print(str_lower)
    str_upper = upper_first_letter(string)
    print(str_upper)

    sub_string = "in THE present AgE"
    int_result = find_substring(str_upper, sub_string)
    if int_result != -1:
        print(f"Substring '{sub_string}' is started at {int_result}")
    else:
        print(f"Substring '{sub_string}' is not exist")

    str_result = get_substring(str_upper, 100, 200)
    print(str_result)

    str_result = insert_break_line(str_upper)
    print(str_result)
    str_result = insert_break_line_with_number_per_line(str_upper, 100)
    print(str_result)

    count_word(str_upper, "in")

if __name__ == "__main__":
    main()