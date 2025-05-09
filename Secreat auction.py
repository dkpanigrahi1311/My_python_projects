
def find_highest_bidder(biding_dictionary):
    highest_amount = 0  
    winner = ""
    for key in biding_dictionary:
        amount = biding_dictionary[key]
        if amount > highest_amount:
            highest_amount = amount
            winner = key
    print(f"The winner is {winner} with a bid of RS.{highest_amount}")


bids = {}
continue_biding = True
while continue_biding:
    name = input("Enter your name: ")
    price = int(input("Enter your bid amount: "))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        continue_biding = False
    elif should_continue == "yes":
        print("\n"*20)
        continue_biding = True
    else:
        print("enter correct spell")
find_highest_bidder(bids)

