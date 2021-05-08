import math
from data3 import *

def data_check(house_id, no_adult, no_child, no_days, allergies, no_patient):
    error_type = []

    if no_patient > no_adult:
        error_type.append(1)
        print('Number of patient cannot larger than number of adult in family!')

    if no_adult <= 0 and no_child > 0:
        error_type.append(2)
        print('The family cannot have no adult while have only child!')

    if no_days < 14:
        error_type.append(3)
        print('Number of days to stay inside must larger than 14 days!')

    if type(house_id).__name__ != 'int':
        error_type.append(4)
        print('House_id must be Integer')

    if type(no_adult).__name__ != 'int':
        error_type.append(4)
        print('no_adult must be Integer')

    if type(no_child).__name__ != 'int':
        error_type.append(4)
        print('no_child must be Integer')

    if type(no_days).__name__ != 'int':
        error_type.append(4)
        print('no_days must be Integer')

    if type(no_patient).__name__ != 'int':
        error_type.append(4)
        print('no_patient must be Integer')

    if str.lower(allergies) != 'nut' and str.lower(allergies) != 'lactose' and str.lower(allergies) != 'none':
        error_type.append(4)
        print('The allergies must be in nut, lactose or none')

    return house_id, error_type


def main():
    house_id, no_adult, no_child, no_days, allergies, no_patient = data_p3(max_adult, min_adult, max_child, min_child,
                                                                           min_patient, max_days, min_days,
                                                                           allergies_list)
    print(house_id, no_adult, no_child, no_days, allergies, no_patient)
    print(data_check(house_id, no_adult, no_child, no_days, allergies, no_patient))


if __name__ == '__main__':
    main()