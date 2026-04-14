def print_total_amount(list):
    total_amount = 0
    for dict in list:             
         total_amount += dict["Amount"]
    return total_amount