# 1. Read content from text-file
def read_file(file_name):
    file = open(file_name, "r")
    string = file.read()
    file.close()
    return string


# 2. Write content to text-file
def write_file(file_name, string):
    file = open(file_name, "w")
    file.write(string)
    file.close()


# 3. Uppercase all content
def uppercase(string):
    str_result = string.upper()
    return str_result


# 4. Lowercase all content
def lowercase(string):
    str_result = string.lower()
    return str_result


# 5. Uppercase with the character in head of sentence
def upper_first_letter(string):
    string.strip()  # remove white-space in head or end of sentence
    str_result = ""
    for i in range(0, len(string)):
        if i == 0:
            str_result += string[i].upper()
        elif string[i - 1] == "." or string[i - 1] == "?" or string[i - 1] == "!":
            str_result += string[i].upper()
        elif string[i - 1] == " " and (string[i - 2] == "." or string[i - 2] == "?" or string[i - 2] == "!"):
            str_result += string[i].upper()
        else:
            str_result += string[i]
    else:
        return str_result


# 6. Find substring in content
def find_substring(string, sub_string):
    str = string.lower()
    sub = sub_string.lower()

    for i in range(0, len(str)):
        flag = True
        for j in range(0, len(sub)):
            if str[i + j] != sub[j]:
                flag = False
                break
        if flag:
            return i
    else:
        return -1


# 7. Get substring from start to end in content
def get_substring(string, start, end):
    str_result = ""
    if start < 0 or start > end:
        return str_result
    elif len(string) < start or len(string) < end:
        print("Length of string is invalid input between start and end index")
        return str_result

    for i in range(start, end):
        str_result += string[i]
    else:
        return str_result


# 8. Break-line: Insert break-line character (\n) after end of sentence
def insert_break_line(string):
    str_result = ""
    for i in range(0, len(string)):
        if string[i] == " " and (string[i - 1] == "." or string[i - 1] == "!" or string[i - 1] == "?"):
            str_result += "\n"
        else:
            str_result += string[i]
    else:
        return str_result


# 9. Enter a integer number is called N, Break-line maximum N character in line
def insert_break_line_with_number_per_line(string, number):
    arr_word = split_word(string)
    str_result = ""
    length = 0
    for item in arr_word:
        if length + len(item) > number:
            str_result += "\n"
            length = 0
        str_result += item + " "
        length += len(item)
    return str_result


# 10. Copy all content of source-file to dest-file
def copy_file(src_file_name, des_file_name):
    string = read_file(src_file_name)
    write_file(des_file_name, string)


# 11. Count the number of word "I"
def count_word(string, word):
    arr_word = split_word_fix(string)
    count = 0
    for item in arr_word:
        if word.lower() == item.lower():
            count += 1
    else:
        return count


# 12. Split word (not duplicate)
def is_exist_word(arr_word, word):
    for item in arr_word:
        if item == word:
            return False
    else:
        return True


def split_word_not_duplicate(string):
    arr_word = []
    word = ""
    for i in range(0, len(string)):
        if string[i] == " ":
            if is_exist_word(arr_word, word):
                arr_word.append(word)
                word = ""
        elif string[i] != "." or string[i] != "," or string[i] != ";" or string[i] != "?" or string[i] != "!":
            word += string[i]
    else:
        if is_exist_word(arr_word, word):
            arr_word.append(word)
            return arr_word


# 13. Statistic frequency for each word
def count_word(arr_word, word):
    count = 0
    for item in arr_word:
        if item == word:
            count += 1
    return count


def statistic_frequency_word(string):
    arr_word = split_word_not_duplicate(string)
    arr = split_word_fix(string)
    dic = {}
    for word in arr_word:
        dic[word] = count_word(arr, word)
    else:
        return dic


# 14. Filter the number in content
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def split_number_in_content(string):
    arr_word = split_word_fix(string)
    arr = []
    for item in arr_word:
        if is_int(item) or is_float(item):
            arr.append(item)
    else:
        return arr


# 15. Split word
def split_word(string):
    arr_word = []
    word = ""
    for i in range(0, len(string)):
        if string[i] == " ":
            arr_word.append(word)
            word = ""
        else:
            word += string[i]
    else:
        arr_word.append(word)
        return arr_word


# 16. Split word without punctuation
def split_word_fix(string):
    arr_word = []
    word = ""
    for i in string:
        if i == " ":
            arr_word.append(word)
            word = ""
        elif i != '.' or i != ',' or i != ';' or i != '?' or i != '!' \
                or i != '(' or i != ')' or i != '{' or i != '}' or i != '[' \
                or i != ']' or i != '-':
            word += i
    else:
        arr_word.append(word)
        return arr_word
