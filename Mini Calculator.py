def add (num_1, num_2):
    return num_1 + num_2
def sub (num_1, num_2):
    return num_1 - num_2
def  mul (num_1, num_2):
    return num_1 * num_2 
def div (num_1, num_2):
    return num_1/num_2
def select_an_operators(select_operator):
    if select_operator == "+":
        return add(number_1, number_2)
    elif select_operator == "-":
        return sub(number_1, number_2)
    elif select_operator == "*":
        return mul(number_1,number_2)
    elif select_operator == "-":
        return div(number_1,number_2)
    else:
        print("Enter the correct operator")
        select_operator = input("Select a given oprators : \n + \n -\n * \n / \n")
        return select_an_operators

number_1 = int(input("Enter your first number : "))
select_operator = input("Select a given oprators : \n + \n -\n * \n / \n")
number_2 = int(input("Enter another number : "))
result = select_an_operators(select_operator)
print(f"{number_1} {select_operator} {number_2} = {result}")
count = 1 
while count > 0:
    y_n_selection = input("Type 'y' for next calculation and type 'n' to complete calculation: - ")
    if y_n_selection == "y":
        number_2 = int(input("Enter another number : "))
        number_1 = result 
        select_operator = input("Select a given oprators : \n + \n -\n * \n / \n")
        result = select_an_operators(select_operator)
        print(f"{number_1} {select_operator} {number_2} = {result}")
        count += 1
    elif y_n_selection == "n":
        result = select_an_operators(select_operator)
        print(f"{number_1} {select_operator} {number_2} = {result}")
        count -= count
