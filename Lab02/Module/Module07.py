def create_array():
    n = int(input('Enter a number of array: '))
    arr = []
    for i in range(1, n + 1):
        temp = int(input(f"a[{i}] = "))
        arr.append(temp)
    return arr


def print_array(arr):
    for i in arr:
        print(i, end='\t')
    else:
        print()


def array_increase(arr):
    i = 0
    while i < (len(arr) - 1):
        j = i + 1
        while j < len(arr):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1


def array_decrease(arr):
    i = 0
    while i < (len(arr) - 1):
        j = i + 1
        while j < len(arr):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            j += 1
        i += 1


# 1. Print Even number
def print_even_number(arr):
    print('Even items of array:')
    for item in arr:
        if item % 2 == 0:
            print(item, end='\t')
    print()


# 2. Print ODD number
def print_odd_number(arr):
    print('Odd items of array:')
    for item in arr:
        if item % 2 != 0:
            print(item, end='\t')
    print()


# 3. Find the second Even number
def find_second_even_number(arr):
    flag_first_even = False
    index = 0
    for item in arr:
        if item % 2 == 0:
            if not flag_first_even:
                flag_first_even = True
            else:
                return index
        index += 1
    else:
        return -1


# 4. Find the second last ODD number
def find_second_last_odd_number(arr):
    flag_first_last_odd = False
    index = len(arr) - 1
    while index >= 0:
        if arr[index] % 2 != 0:
            if not flag_first_last_odd:
                flag_first_last_odd = True
            else:
                return index
        index -= 1
    else:
        return -1


# 5. Print run-lane increase -> [1, 2, 3, 4, 0, 5, 6, 2, 8, 19] => 1, 2, 3, 4 | 0, 5, 6 | 2, 8, 19
def print_run_lane_increase(arr):
    i = 0
    while i < len(arr) - 1:
        print(arr[i], end='\t')
        if arr[i] > arr[i + 1]:
            print()
        i += 1
    print(arr[i])


# 6. Find the longest run-lane increase -> [1, 2, 3, 4, 0, 5, 6, 2, 8, 19] => 1, 2, 3, 4
def find_longest_run_lane_increase(arr):
    arr_longest = []
    a = []
    i = 0
    while i < len(arr) - 1:
        a.append(arr[i])
        if arr[i] > arr[i + 1]:
            if len(a) > len(arr_longest):
                arr_longest.clear()
                for item in a:
                    arr_longest.append(item)
            a.clear()
        i += 1
    a.append(arr[i])
    if len(a) > len(arr_longest):
        arr_longest.clear()
        for item in a:
            arr_longest.append(item)

    return arr_longest

# 7. Find the third smallest
def sort_three_item(arr, a, b, c):
    if arr[a] < arr[b] < arr[c]:
        return a, b, c
    if arr[a] < arr[c] < arr[b]:
        return a, c, b
    if arr[b] < arr[a] < arr[c]:
        return b, a, c
    if arr[b] < arr[c] < arr[a]:
        return b, c, a
    if arr[c] < arr[a] < arr[b]:
        return c, a, b
    if arr[c] < arr[b] < arr[a]:
        return c, b, a

    return a, b, c


def find_the_third_smallest(arr):
    if len(arr) <= 3:
        return -1

    first_smallest_index = 0
    second_smallest_index = 1
    thirst_smallest_index = 2

    first_smallest_index, second_smallest_index, thirst_smallest_index = sort_three_item(arr, first_smallest_index, second_smallest_index, thirst_smallest_index)

    index = 3
    while index < len(arr):
        if arr[index] < thirst_smallest_index:
            thirst_smallest_index = index
            first_smallest_index, second_smallest_index, thirst_smallest_index = sort_three_item(arr,
                                                                                                 first_smallest_index,
                                                                                                 second_smallest_index,
                                                                                                 thirst_smallest_index)
        index += 1
    print(first_smallest_index, ' ', second_smallest_index, ' ', thirst_smallest_index)
    return thirst_smallest_index


# 8. Find the second largest
def find_the_second_largest(arr):
    if len(arr) < 2:
        return -1

    max = 0
    for i in range(1, len(arr)):
        if arr[max] < arr[i]:
            max = i

    if max == 0:
        second = 1
    else:
        second = 0

    for i in range(0, len(arr)):
        if (arr[second] < arr[i]) and (i != max):
            second = i
    return second


# 9. Sort array with positive decrease first, negative increase, zero
def split_pos_neg_zero_array(arr):
    pos_arr = []
    neg_arr = []
    zero_arr = []
    for item in arr:
        if item > 0:
            pos_arr.append(item)
        elif item == 0:
            zero_arr.append(item)
        else:
            neg_arr.append(item)
    return pos_arr, neg_arr, zero_arr


def sort_pos_neg_zero_array(arr):
    pos_arr, neg_arr, zero_arr = split_pos_neg_zero_array(arr)
    array_decrease(pos_arr)
    array_increase(neg_arr)
    arr_result = []

    for item in pos_arr:
        arr_result.append(item)

    for item in neg_arr:
        arr_result.append(item)

    for item in zero_arr:
        arr_result.append(item)

    return arr_result


def sort_pos_neg_zero(arr):
    array_decrease(arr)

    zero_index = 0
    for i in range(1, len(arr)):
        if arr[i] == 0:
            zero_index = i
            break
        i += 1

    for i in range(0, (len(arr) - zero_index) // 2):
        arr[zero_index + i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[zero_index + i]
        i += 1


# 10. Find number have sum of digit largest
def sum_digit(n):
    sum = 0
    while n > 0:
        sum = sum * 10 + (n % 10)
        n = n // 10
    return sum


def find_sum_digit_largest(arr):
    max = sum_digit(arr[0])
    max_index = 0
    for i in range(1, len(arr)):
        digit_value = sum_digit(arr[i])
        if max < digit_value:
            max = digit_value
            max_index = i
        i += 1
    return max_index
