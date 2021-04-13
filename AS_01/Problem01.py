import math
from data1 import *

def calculate_delivery_box(house_id, no_adult, no_child, no_days, allergies, no_patient):
    sum_food_portion = math.ceil(((no_adult + (no_child * 0.7)) * 3) * no_days)
    if allergies == 'lactose':
        sum_almond_milk = math.ceil((((no_adult - no_patient) * 0.5) + (no_child * 2)) * no_days)
        sum_cow_milk = 0
    else:
        sum_cow_milk = math.ceil((((no_adult - no_patient) * 0.5) + (no_child * 2)) * no_days)
        sum_almond_milk = 0
    sum_treatment_milk = math.ceil(no_patient * 0.5 * no_days)
    sum_tolet_paper = math.ceil(no_patient * (no_days / 2)) + math.ceil(no_child * (no_days / 3)) + math.ceil((no_adult - no_patient) * (no_days / 4))
    print(f'Household id {house_id} will get {sum_food_portion} food portions, {sum_cow_milk} liter(s) of cow milk, {sum_almond_milk} liter(s) of almond milk, {sum_treatment_milk} liter(s) of treatment milk, and {sum_tolet_paper} toilet paper rolls.')


def inputData(local_max_adult, local_min_adult, local_max_child, local_min_child,
            local_min_patient, local_max_days, local_min_days, local_allergies_list):
    local_house_id = int(input("Enter HouseHold ID: "))
    local_no_adult = int(input(f"Enter local adult between {local_min_adult} and {local_max_adult}: "))
    local_no_child = int(input(f"Enter local child between {local_min_child} and {local_max_child}: "))
    local_no_days = int(input(f"Enter num of days inside between {local_min_days} and {local_max_days}: "))
    local_allergies = input(f"Enter allergies is one of item: '{allergies_list[0]}, '{allergies_list[1]}, {allergies_list[2]}': ")
    local_no_patient = int(input(f"Enter num of patient in family between {local_min_patient} and {local_no_adult}: "))

    return local_house_id, local_no_adult, local_no_child, local_no_days, local_allergies, local_no_patient


def main():
    house_id, no_adult, no_child, no_days, allergies, no_patient = inputData(max_adult, min_adult, max_child, min_child,
                                                                           min_patient, max_days, min_days,
                                                                           allergies_list)

    calculate_delivery_box(house_id, no_adult, no_child, no_days, allergies, no_patient)


if __name__ == '__main__':
    main()