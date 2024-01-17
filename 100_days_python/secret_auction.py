import random
print("Welcome to DaveTech SECRET AUCTION program")
good = ["Telivision", "Motorcycle", "Generator", "Laptop", "Air Conditioner", "Iphone", "grand piano", "car", "gas cooker"]

items_to_be_sold = random.choice(good)
print(f"At DaveTech, we are selling our {items_to_be_sold} today to any lucky customer, highest bidder wins...Goodluck")
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner of the {items_to_be_sold} is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    
