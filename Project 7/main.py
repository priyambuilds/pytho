"""
Tic Tac Toe Game

A simple command-line implementation of the classic Tic Tac Toe game.
Players can choose to play as X or O and play against either another human
or the computer.
"""
import random
from typing import List, Tuple, Optional, Literal

def sum(a: int, b: int, c: int) -> int:
    """
    Sum three values together.
    
    Args:
        a: First value
        b: Second value
        c: Third value
        
    Returns:
        Sum of the three values
    """
    return a + b + c

def print_board(xState: List[int], zState: List[int]) -> None:
    """
    Display the current state of the game board.
    
    Args:
        xState: List representing X player's positions (1 if occupied, 0 if not)
        zState: List representing O player's positions (1 if occupied, 0 if not)
    """
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")

def check_win(xState: List[int], zState: List[int]) -> int:
    """
    Check if either player has won or if the game is still ongoing.
    
    Args:
        xState: List representing X player's positions
        zState: List representing O player's positions
        
    Returns:
        1 if X wins, 0 if O wins, -1 if no winner yet
    """
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X wins")
            return 1  # returns 1 if X wins
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O wins")
            return 0  # returns 0 if O wins
    
    # Check for draw (board is full)
    if all((xState[i] == 1 or zState[i] == 1) for i in range(9)):
        print("It's a draw!")
        return 2
        
    return -1  # no one wins yet

def get_valid_move(xState: List[int], zState: List[int]) -> int:
    """
    Get a valid move from the human player.
    
    Args:
        xState: List representing X player's positions
        zState: List representing O player's positions
        
    Returns:
        Valid position (0-8) that is not already occupied
    """
    while True:
        try:
            value = int(input("Please enter a position (0-8): "))
            if value < 0 or value > 8:
                print("Invalid input! Please enter a number between 0 and 8.")
                continue
            
            if xState[value] == 1 or zState[value] == 1:
                print("Position already occupied! Try another position.")
                continue
                
            return value
        except ValueError:
            print("Invalid input! Please enter a number between 0 and 8.")

def computer_move(xState: List[int], zState: List[int]) -> int:
    """
    Generate a move for the computer player.
    
    This implements a simple AI that:
    1. Tries to win if possible
    2. Blocks the opponent from winning
    3. Takes the center if available
    4. Otherwise makes a random valid move
    
    Args:
        xState: List representing X player's positions
        zState: List representing O player's positions
        
    Returns:
        Position (0-8) chosen by the computer
    """
    # Create copies for testing moves
    computer_state = xState if computer_symbol == 'X' else zState
    human_state = zState if computer_symbol == 'X' else xState
    
    # Check winning moves
    for i in range(9):
        if xState[i] == 0 and zState[i] == 0:
            # Try this position
            computer_state[i] = 1
            if check_win(xState, zState) == (1 if computer_symbol == 'X' else 0):
                computer_state[i] = 0  # Reset the test
                return i
            computer_state[i] = 0  # Reset the test
    
    # Block opponent's winning moves
    for i in range(9):
        if xState[i] == 0 and zState[i] == 0:
            # Try this position for opponent
            human_state[i] = 1
            if check_win(xState, zState) == (1 if human_symbol == 'X' else 0):
                human_state[i] = 0  # Reset the test
                return i
            human_state[i] = 0  # Reset the test
    
    # Take center if available
    if xState[4] == 0 and zState[4] == 0:
        return 4
        
    # Take a random available position
    available_positions = [i for i in range(9) if xState[i] == 0 and zState[i] == 0]
    return random.choice(available_positions)

if __name__ == "__main__":
    print("Welcome to Tic Tac Toe")
    
    # Player setup
    while True:
        play_mode = input("Play against computer (c) or human (h)? ").lower()
        if play_mode in ['c', 'h']:
            break
        print("Invalid choice! Please enter 'c' for computer or 'h' for human.")
    
    if play_mode == 'c':
        while True:
            player_symbol = input("Choose your symbol - X or O: ").upper()
            if player_symbol in ['X', 'O']:
                break
            print("Invalid choice! Please enter 'X' or 'O'.")
        
        computer_symbol = 'O' if player_symbol == 'X' else 'X'
        human_symbol = player_symbol
        
        print(f"You are playing as {player_symbol}")
        print(f"Computer is playing as {computer_symbol}")
    
    # Initialize game state
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O
    
    # Main game loop
    while True:
        print_board(xState, zState)
        current_symbol = 'X' if turn == 1 else 'O'
        
        # Determine who's turn it is and get move
        if play_mode == 'h' or (play_mode == 'c' and current_symbol == human_symbol):
            print(f"{current_symbol}'s chance (You)")
            value = get_valid_move(xState, zState)
        else:
            print(f"{current_symbol}'s chance (Computer)")
            value = computer_move(xState, zState)
            print(f"Computer chose position {value}")
        
        # Update game state
        if turn == 1:
            xState[value] = 1
        else:
            zState[value] = 1
        
        # Check for win or draw
        cwin = check_win(xState, zState)
        if cwin != -1:
            print_board(xState, zState)
            if cwin == 2:
                print("It's a draw!")
            else:
                winner = "X" if cwin == 1 else "O"
                if play_mode == 'c':
                    if (winner == human_symbol):
                        print("You win!")
                    else:
                        print("Computer wins!")
                else:
                    print(f"Player {winner} wins!")
            
            print("Game over")
            
            # Ask to play again
            play_again = input("Play again? (y/n): ").lower()
            if play_again != 'y':
                break
                
            # Reset the game
            xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            turn = 1
            
            if play_mode == 'c':
                while True:
                    player_symbol = input("Choose your symbol - X or O: ").upper()
                    if player_symbol in ['X', 'O']:
                        break
                    print("Invalid choice! Please enter 'X' or 'O'.")
                
                computer_symbol = 'O' if player_symbol == 'X' else 'X'
                human_symbol = player_symbol
            
            continue
            
        turn = 1 - turn  # switches between 1 and 0
        
