def main():
    my_list = [1, "Hello", True, 4, 5]
    my_dict = {"firstname": "Gaston", "lastname": "Climent"}

    super_list = [
        {"firstname": "Gaston", "lastname": "Climent"},
        {"firstname": "Pepe", "lastname": "Rodriguez"},
        {"firstname": "Juan", "lastname": "logo"},
        {"firstname": "Damian", "lastname": "niz"},
        {"firstname": "Juana", "lastname": "Lopez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2,],
        "floating_nums": [1.2, 4.6, 7.34]
    }


    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i["firstname"], "-", i["lastname"])


if __name__ == '__main__':
    main()