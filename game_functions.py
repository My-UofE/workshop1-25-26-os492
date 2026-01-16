import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    if next_val>current_val and user_input == "h":
        return True
    elif next_val<current_val and user_input == "l":
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    result = False
    x=0
    for x in range(len(word)):
        if word[x] == letter:
            result = True
            board[x] = letter
        else:
            x = x + 1
    if result == True:
        print("Well done!", letter, "is in the word")
        return result
    else:
        print("Sorry", letter, "is not in the word")
        return result
    
