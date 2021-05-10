'''
Input a list integer number. Sort Increase or Decrease
'''

from Module.Module07 import *


def main():
    # arr = create_array()
    arr = [8, 2, 4, 3, 6, 9, 5, 1, 7, 0]
    print_array(arr)
    array_increase(arr)
    print_array(arr)
    array_decrease(arr)
    print_array(arr)

    arr = [1, 2, 3, 4, -1, 5, 6, 2, 8, 19, 0, -2, -5, 0, -6, 0]
    print_even_number(arr)
    print_odd_number(arr)
    index = find_second_even_number(arr)
    if index != -1:
        print(f'The second even number is {arr[index]}')

    index = find_second_last_odd_number(arr)
    if index != -1:
        print(f'The second last odd number is {arr[index]}')
    print_run_lane_increase(arr)

    arr_longest = find_longest_run_lane_increase(arr)
    print("The Longest run-lane increase: ", end="\t")
    print_array(arr_longest)

    print_array(arr)

    third_smallest_index = find_the_third_smallest(arr)
    if third_smallest_index != -1:
        print(f"The third smallest value: {arr[third_smallest_index]}")

    second_largest_index = find_the_second_largest(arr)
    if second_largest_index != -1:
        print(f"The second largest value: {arr[second_largest_index]}")

    print(sort_pos_neg_zero_array(arr))
    sort_pos_neg_zero(arr)
    print(arr)

    sum_digit_largest = find_sum_digit_largest(arr)
    print(f"The max sum_digit: {arr[sum_digit_largest]}")

if __name__  == "__main__":
    main()