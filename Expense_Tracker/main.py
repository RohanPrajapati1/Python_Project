import addList , print_list , total_amount , menu
expense_list = []

print("Welcome to Expense Tracker\n")
while(True):
    choice = menu.menu()
    if choice == 4 :
        print("Thanks for visiting")
        break
#   Adding expenses
    elif choice == 1:
        expense_list.append(addList.add_item())

#   Printing Expenses
    elif choice == 2:
        print_list.print_expense_list(expense_list)

#   Calculating Total amount
    elif choice == 3:
       amount = total_amount.print_total_amount(expense_list)
       print(f"Total Expenses : {amount}")
