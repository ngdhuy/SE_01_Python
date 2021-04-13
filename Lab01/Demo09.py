# dictionary in python
def demoSet():
    mySet = {1, "Hello", 2.1}
    print(mySet)
    print(list(mySet)[1])


def demoDictionary():
    dic = {'id': 1, 'Name': 'iPhone 12', 'Price': 1.8}
    print(dic)
    print(dic['id'])
    print(dic['Name'])
    print(dic['Price'])


def demoMultipleDictionary():
    listOfCategory = [
        {
            'id': 1,
            'cat_name': 'Cell phone',
            'products': [
                {
                    'product_id': 1,
                    'product_name': 'iPhone 12 Pro Max'
                },
                {
                    'product_id': 2,
                    'product_name': 'iPhone 11 Pro'
                },
                {
                    'product_id': 3,
                    'product_name': 'iPhone XS'
                }
            ]
        },
        {
            'id': 2,
            'cate_name': 'Tablet'
        }
    ]

    for cat in listOfCategory:
        if 'products' in cat:
            for p in cat['products']:
                print(p)



def main():
    # demoSet()
    # demoDictionary()
    demoMultipleDictionary()


if __name__ == "__main__":
    main()