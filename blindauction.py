# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)

def find_highest_bidder(dictionary):
    max_bid_name = max(dictionary)
    print(f"The winner is {max_bid_name} with a bid of $ {dictionary[max_bid_name]}")

# OR
# for bidder in bidding_dictionary:
#    bid_amount = bidding_dictionary[bidder]
#    if bid_amount > highest_bid :
#        highest_bid = bid_amount
#        winner = bidder
# print(f"the winner is {winner} with a bid of $ {highest_bid}.")

bidding_dictionary = {}

game = True
while game :
    name = input("What is your name?")
    bid = input("What is your bid? : $")
    bidding_dictionary[name] = bid
    any_other_bid = input("Are there any other bidders? "
                              "Type 'yes' or 'no'. \n").lower()
    if any_other_bid == 'no' :
        game = False
        find_highest_bidder(bidding_dictionary)
    elif any_other_bid == 'yes' :
        print("\n"*100)





