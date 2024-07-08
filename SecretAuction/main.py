values = {}


def bid_checker(name, bid): 
    values[name]=bid


cont = True
while cont is True:
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = int(input("What's your bid: $"))
    bid_checker(name,bid)
    other = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other == 'no':
        cont = False 
bid_amount=0
for bid in values:
    if values[bid] > bid_amount:
        bid_amount = values[bid]
        name = bid 
        
print(f"The winner is {name} with a bid of ${bid_amount}!")
   