from data4 import *


def priority_cal(data):
    output = {}
    for key, value in data.items():
        priority_num = 8
        if value[0] == 'medical':
            priority_num = 1
        elif value[0] == 'military':
            priority_num = 2
        elif value[0] == 'diplomatic':
            priority_num = 3
        elif value[0] == 'essential':
            priority_num = 4
        elif value[0] == 'teacher':
            priority_num = 5
        elif value[1] > 65:
            priority_num = 6
        elif value[2]:
            priority_num = 7

        output[key] = priority_num

    return output


def main():
    data_dict = data_p4(jobs_list, data_no)
    print(data_dict)
    print(priority_cal(data_dict))


if __name__ == '__main__':
    main()