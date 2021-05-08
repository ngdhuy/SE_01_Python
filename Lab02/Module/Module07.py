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
# 8. Find the second largest
# 9. Sort array with positive decrease first, negative increase, zero
# 10. Find number have sum of digit largest