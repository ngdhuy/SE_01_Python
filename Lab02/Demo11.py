
def main():
    shopping_list = ["apple", "orange", "kiwi", "orange", "apple", "apple"]
    price_dict = {
        "apple": [59.9, 0.4],
        "orange": [29.9, 0.0],
        "kiwi": [69.9, 0.1]
    }

    total = 0.0
    for item in shopping_list:
        price = price_dict[item][0]
        discount = price_dict[item][1]
        total += price * (1.0 - discount)
    print(f"Total is {total}")

    # -- Calculate max frequency of shopping_item
    frequency_shopping_item = {}
    for item in shopping_list:
        flag = False
        for f_item in frequency_shopping_item:
            if item == f_item:
                frequency_shopping_item[f_item] += 1
                flag = True
                break
        if not(flag):
            frequency_shopping_item[item] = 1
    # print(frequency_shopping_item)
    max = 0
    item_name = ""
    for item in frequency_shopping_item:
        if frequency_shopping_item[item] > max:
            max = frequency_shopping_item[item]
            item_name = item
    print(f"number of {item_name} is {frequency_shopping_item[item_name]}")




if __name__ == "__main__":
    main()