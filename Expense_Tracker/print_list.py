def print_expense_list(list):
    for dict in list:
            for key , values in dict.items():
                print(f"{key} : {values}")
            print()