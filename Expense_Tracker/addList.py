
def add_item():
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter Expense category(food , travel .. ): ")
        desc = input("Enter description: ")
        amount = float(input("Enter Amount: "))
        temp_dict = {"Date" : date , "Category" : category , 
                     "Description" : desc , "Amount" : amount} 
        return temp_dict