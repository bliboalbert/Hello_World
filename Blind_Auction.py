"""Blind Auction: Receive name and bid amount from bidders in a room without the consent of the other bidders on the bid amount of each bidder"""

def continue_bidding():
    '''Ask for name and bid amount from other bidders in the room and call main bidder function for computation'''
    name = input('Please your name: ')
    bid = int(input('How much do you bid? $'))
    grand_bid(name=name, bid=bid)
    
auction = {}
def grand_bid(name, bid):
    '''Compute the winner of the blind auction and print it in the console.'''
    auction[name] = bid
    
    next_bid = input("Type 'yes' if other bidders are there, otherwise 'no' \n").lower()
    if next_bid == 'no':
        max_bid = 0
        winner = ''
        for key in auction:
            bid_amount = auction[key]
            if bid_amount > max_bid:
                max_bid = bid_amount
                winner = key
        print(auction)      
        print(f"The winner is {winner} with ${max_bid} bid.")
        
    else:
        continue_bidding()
        

name = input('Please your name: ')
bid = int(input('How much do you bid? $ '))
grand_bid(name=name, bid=bid)