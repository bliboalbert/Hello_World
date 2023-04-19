# import statements
import random
# from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] # card decks

# define function for every game procedure:

def deal_card(): # deal card to both player and computer
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def compute_score(card): # calculate card scores for players:
    if sum(card) == 21 and len(card) == 2:
        return 0
    if sum(card) > 21 and 11 in card:
        card.remove(11)
        card.append(1)
        return sum(card)
    return sum(card)

def compare(player_score, computer_score): # compare the scores of the players and decide winner
    if player_score == computer_score:
        print('Draw!')
    elif player_score == 0:
        print('You win with Blackjack!')
    elif computer_score == 0:
        print('Opponent win with Blackjack!')
    elif player_score > 21:
        print('You went over, you lose.')
    elif computer_score > 21:
        print('Opponent went over, you win!')
    elif player_score > computer_score:
        print('You win!')
    else:
        print('You lose!')
def blackjack():        
    game_over = False
    computer_hand = []
    player_hand = []
    for _ in range(2):
            player_card = deal_card()
            player_hand.append(player_card)
            computer_card = deal_card()
            computer_hand.append(computer_card)

    while not game_over:
        player_score = compute_score(player_hand)
        computer_score = compute_score(computer_hand)
            
        print(f'Your first hand: {player_hand}, score: {player_score}')
        print(f'Computer first hand: {computer_hand[0]}')
        
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True

        elif player_score < 21:
            play_again = input("Draw another card. Type 'y' to draw, otherwise 'n' to pass: ")
            if play_again == 'y':
                player_hand.append(deal_card())
                player_score = compute_score(player_hand)
            else:
                game_over = True
        while computer_score != 0 and computer_score < 17:
            computer_hand.append(deal_card())
            computer_score = compute_score(computer_hand)
        print(f'Your final hand: {player_hand}, score: {player_score}')
        print(f'Computer final hand: {computer_hand}, score: {computer_score}')
        compare(player_score, computer_score)
        
while input("play a game of Blackjack. Type 'yes' to play, otherwise 'no': ") == 'yes':
#         clear()
    blackjack()
    
# blackjack()        

