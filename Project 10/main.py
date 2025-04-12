"""
Mastermind Game

This is a simple implementation of the Mastermind game where you need to guess
a randomly generated color code. Each color is represented by a letter.

How to play:
1. The computer will generate a 4-color code
2. You have 10 attempts to guess the code
3. After each guess, you'll receive feedback:
   - How many colors are in the correct position
   - How many colors are correct but in the wrong position
4. Try to guess the code within the allowed attempts!
"""

import random

# Game configuration constants
COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10  # Number of attempts allowed
CODE_LENGTH = 4  # Length of the code to guess

def generate_code():
    """
    Generate a random color code.
    
    Returns:
        A list of randomly selected colors
    """
    code = []
    for _ in range(CODE_LENGTH):  # Using _ as we don't need the loop variable
        color = random.choice(COLORS)
        code.append(color)
    return code

def get_guess():
    """
    Get a valid color code guess from the user.
    
    The function will continuously prompt until a valid guess is provided.
    
    Returns:
        A list of colors representing the user's guess
    """
    while True:
        guess_input = input(f"Enter {CODE_LENGTH} colors (space-separated) from {', '.join(COLORS)}: ").upper()
        guess = guess_input.split()
        
        # Check if the correct number of colors was entered
        if len(guess) != CODE_LENGTH:
            print(f"You must enter exactly {CODE_LENGTH} colors. You entered {len(guess)}.")
            continue
        
        # Check if all entered colors are valid
        invalid_colors = [color for color in guess if color not in COLORS] #explanation - for each color in the guess, check if it is in the COLORS list, if it is not, add it to the invalid_colors list
        if invalid_colors:
            print(f"Invalid color(s): {', '.join(invalid_colors)}. Valid colors are: {', '.join(COLORS)}")
            continue
            
        # If we reach here, the guess is valid
        return guess

def check_guess(guess, code):
    """
    Check how many colors are in the correct and incorrect positions.
    
    Args:
        guess: The user's guess
        code: The secret code
    
    Returns:
        A tuple containing (correct positions, incorrect positions)
    """
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    # Count occurrences of each color in the code
    for color in code:
        if color not in color_counts:
            color_counts[color] = 0 #explanation - if the color is not in the color_counts dictionary, add it and set the value to 0. 0 is used because we are counting the number of times each color appears in the code so that we can use it to check if the color is in the wrong position
        color_counts[color] += 1 #explanation - if the color is in the color_counts dictionary, increment the value by 1, this is to count the number of times each color appears in the code.

    # First pass: Check for correct positions
    for guess_color, real_color in zip(guess, code): #explanation - zip function means that the first item in the guess is paired with the first item in the code,ple -  the second item in the guess is paired with the second item in the code, and so on. example - if the guess is [R, G, B, Y] and the code is [R, G, B, Y], then the first item in the guess is paired with the first item in the code, so that we can check if the color is in the correct position.
        if guess_color == real_color:
            correct_pos += 1 #explanation - if the color is in the correct position, increment the correct_pos by 1
            color_counts[guess_color] -= 1 #explanation - if the color is in the correct position, decrement the value of the color in the color_counts dictionary by 1, this is to prevent the color from being counted more than once.
    
    # Second pass: Check for correct colors in wrong positions
    for guess_color in guess:
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos
    
def game():
    """
    Main game function that controls the game flow.
    """
    print("-" * 50)
    print("Welcome to Mastermind!")
    print(f"You have {TRIES} tries to guess the {CODE_LENGTH}-color code.")
    print(f"The valid colors are: {', '.join(COLORS)}")
    print("-" * 50)
    
    # Generate the secret code
    code = generate_code()
    
    # Main game loop
    for attempts in range(1, TRIES + 1):
        print(f"\nAttempt {attempts}/{TRIES}")
        guess = get_guess()
        
        # Check the guess against the code
        correct_pos, incorrect_pos = check_guess(guess, code)
        
        # Display feedback
        print(f"Result: {correct_pos} correct position(s), {incorrect_pos} correct color(s) in wrong position(s)")
        
        # Check if the player won
        if correct_pos == CODE_LENGTH:
            print(f"\nCongratulations! You guessed the code in {attempts} tries!")
            print(f"The code was: {' '.join(code)}")
            break
    else:
        # This runs if the for loop completes without breaking (player didn't guess the code)
        print(f"\nGame over! You ran out of tries.")
        print(f"The secret code was: {' '.join(code)}")
        
if __name__ == "__main__":
    game()

