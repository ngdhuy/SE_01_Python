import math

def item_cal(house_id, no_adult, no_child, no_days, allergies, no_patient):
    sum_food_portion = math.ceil(((no_adult + (no_child * 0.7)) * 3) * no_days)
    if allergies == 'lactose':
        sum_almond_milk = math.ceil((((no_adult - no_patient) * 0.5) + (no_child * 2)) * no_days)
        sum_cow_milk = 0
    else:
        sum_cow_milk = math.ceil((((no_adult - no_patient) * 0.5) + (no_child * 2)) * no_days)
        sum_almond_milk = 0
    sum_treatment_milk = math.ceil(no_patient * 0.5 * no_days)
    sum_toilet_paper = math.ceil(no_patient * (no_days / 2)) + math.ceil(no_child * (no_days / 3)) + math.ceil((no_adult - no_patient) * (no_days / 4))
    print(f'Household id {house_id} will get {sum_food_portion} food portions, {sum_cow_milk} liter(s) of cow milk, {sum_almond_milk} liter(s) of almond milk, {sum_treatment_milk} liter(s) of treatment milk, and {sum_toilet_paper} toilet paper rolls.')
    return house_id, sum_food_portion, sum_cow_milk, sum_almond_milk, sum_treatment_milk, sum_toilet_paper