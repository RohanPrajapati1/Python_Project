import addList , print_list , total_amount , menu , json

def load_expense():
    try:
        with open("expenses.txt" , 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_expense(expenses):
    with open("expenses.txt" , 'w') as file:
        json.dump(expenses , file)

expense_list = load_expense()

print("Welcome to Expense Tracker\n")
while(True):
    choice = menu.menu()
    if choice == 4 :
        print("Thanks for visiting")
        break
#   Adding expenses
    elif choice == 1:
        expense_list.append(addList.add_item())
        save_expense(expense_list)


#   Printing Expenses
    elif choice == 2:
        print_list.print_expense_list(expense_list)

#   Calculating Total amount
    elif choice == 3:
       amount = total_amount.print_total_amount(expense_list)
       print(f"Total Expenses : {amount}")
