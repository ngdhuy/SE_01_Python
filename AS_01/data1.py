# import required modules
import random

# define global variables
max_adult = 7
max_child = 7
min_adult = 1
min_child = 0
min_patient = 0
max_days = 21
min_days = 14
allergies_list = ['nut', 'lactose', 'none']


def data_p1(local_max_adult, local_min_adult, local_max_child, local_min_child,
            local_min_patient, local_max_days, local_min_days, local_allergies_list):
    """
    This function will generate data for p1
    :param local_max_adult: maximum number of adults in each household
    :param local_min_adult: minimum number of adults in each household
    :param local_max_child: maximum number of children in each household
    :param local_min_child: minimum number of children in each household
    :param local_min_patient: minimum number of patients in each household
    :param local_max_days: maximum number of days they have to stay in
    :param local_min_days: minimum number of days they have to stay in
    :param local_allergies_list: list of all possible allergies
    :return: data for p1
    """
    local_house_id = random.randint(10000, 99999)
    local_no_adult = random.randint(local_min_adult, local_max_adult)
    local_no_child = random.randint(local_min_child, local_max_child)
    local_no_days = random.randint(local_min_days, local_max_days)
    local_allergies = random.choice(local_allergies_list)
    local_no_patient = random.randint(local_min_patient, local_no_adult)  # note max here is local_no_adult

    return local_house_id, local_no_adult, local_no_child, local_no_days, local_allergies, local_no_patient


# test function
# house_id, no_adult, no_child, no_days, allergies, no_patient = data_p1(max_adult, min_adult, max_child, min_child,
#                                                                       min_patient, max_days, min_days, allergies_list)
# print(house_id, no_adult, no_child, no_days, allergies, no_patient)
