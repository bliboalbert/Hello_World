# Complete number guessing game
# Player attempts to guess the random number generated by the computer

# import statements
import random

# define functions to control game behaviour
def generate_number():
    computer_guess = random.randint(1, 100) # generate integers between 1 and 100 inclusive
    return computer_guess

def compare_guesses(computer_guess, player_guess):
    if player_guess == computer_guess:
        return 'You win!'
    elif player_guess < computer_guess:
        return 'Too low!'
    elif player_guess > computer_guess:
        return 'Too high!'
def play_game():
    computer_guess = generate_number()
    print('Welcome to Number Guessing Game!')
    print('I am guessing a number between 1 and 100 \n')
        
    level = input("Choose difficulty: type 'easy' or 'hard': ").lower()
    if level == 'easy':
        live = 10
        print(f"You've {live} attempts to guess. Good luck.")
    else:
        live = 5
        print(f"You've {live} attempts to guess. Good luck.")
    game_over = False
    while not game_over:
            
        player_guess = int(input('Make your guess: '))
        print(compare_guesses(computer_guess, player_guess))
        compare = compare_guesses(computer_guess, player_guess)
        if compare == 'You win!':
            play_more = input("Type 'yes' to play more, otherwise 'no' ").lower()
            if play_more == 'yes':
                play_game()
            else:
                game_over = True
                
        else:
            live -= 1
            if live == 0:
                print('You lose!')
                game_over = True
            else:
                print(f"You've {live} attempts remaining. Good luck.")
#                 play_game()
while input("Play number guessing game: type 'yes' to play, otherwise 'no' ") == 'yes':
     play_game()
# play_game()
