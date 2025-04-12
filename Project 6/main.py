#!/usr/bin/env python3
"""
Words Per Minute (WPM) Typing Test

A terminal-based application that tests typing speed and accuracy.
The program displays words that the user needs to type over,
tracks typing speed in WPM, and highlights correct/incorrect input.
"""
import curses
from curses import wrapper
import time
import random
from typing import List, Tuple, Optional


def load_text() -> List[str]:
    """
    Load a list of words for the typing test.
    
    Returns:
        List[str]: A list of common English words for typing practice
    """
    words = [
        "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
        "it", "for", "not", "on", "with", "he", "as", "you", "do", "at",
        "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
        "or", "an", "will", "my", "one", "all", "would", "there", "their", "what",
        "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
        "when", "make", "can", "like", "time", "no", "just", "him", "know", "take",
        "people", "into", "year", "your", "good", "some", "could", "them", "see", "other",
        "than", "then", "now", "look", "only", "come", "its", "over", "think", "also",
        "back", "after", "use", "two", "how", "our", "work", "first", "well", "way",
        "even", "new", "want", "because", "any", "these", "give", "day", "most", "us",
        "is", "are", "was", "were", "had", "has", "it's", "been", "being", "am"
    ]
    return words


def display_text(stdscr: 'curses._CursesWindow', target_text: str, current_text: str, wpm: float = 0.0) -> None:
    """
    Display the target text, user's current input, and WPM on the screen.
    
    Args:
        stdscr: The curses window object
        target_text: The text the user needs to type
        current_text: The text the user has typed so far
        wpm: Current words per minute speed
    """
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    # Calculate center position for text
    start_x = max(0, w // 2 - len(target_text) // 2)
    start_y = h // 2
    
    # Display instructions
    instructions = "Type the text below. Press ESC to exit."
    stdscr.addstr(start_y - 3, max(0, w // 2 - len(instructions) // 2), instructions)
    
    # Display stats
    stats = f"WPM: {wpm:.2f}"
    stdscr.addstr(start_y - 1, max(0, w // 2 - len(stats) // 2), stats)
    
    # Display target text
    stdscr.addstr(start_y, start_x, target_text)
    
    # Display user's typing with color-coded feedback
    for i, char in enumerate(current_text):
        # Stay within bounds
        if i >= len(target_text) or start_x + i >= w - 1:
            break
            
        # Set color based on correctness
        if i < len(target_text):
            if char == target_text[i]:
                color = curses.color_pair(1)  # Green for correct
            else:
                color = curses.color_pair(2)  # Red for incorrect
            
            stdscr.addstr(start_y, start_x + i, char, color)
    
    stdscr.refresh()


def calculate_wpm(start_time: float, end_time: float, typed_chars: int) -> float:
    """
    Calculate words per minute based on typing duration and character count.
    
    Args:
        start_time: The time when typing started (in seconds)
        end_time: The time when typing ended (in seconds)
        typed_chars: Number of characters typed
        
    Returns:
        float: The calculated WPM
    """
    # Standard calculation: 5 characters = 1 word, convert to minutes
    elapsed_time = max(0.001, end_time - start_time)  # Avoid division by zero
    words = typed_chars / 5
    minutes = elapsed_time / 60
    return words / minutes if minutes > 0 else 0


def generate_target_text(word_list: List[str], word_count: int = 10) -> str:
    """
    Generate a random string of words for the typing test.
    
    Args:
        word_list: List of words to choose from
        word_count: Number of words to include
        
    Returns:
        str: Space-separated string of random words
    """
    selected_words = random.sample(word_list, min(word_count, len(word_list)))
    return " ".join(selected_words)


def run_typing_test(stdscr: 'curses._CursesWindow') -> Tuple[float, float]:
    """
    Run the main typing test.
    
    Args:
        stdscr: The curses window object
        
    Returns:
        Tuple[float, float]: A tuple containing (WPM, accuracy percentage)
    """
    # Initialize colors
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    
    # Prepare words and initial display
    words = load_text()
    target_text = generate_target_text(words)
    current_text = ""
    wpm = 0.0
    
    # Track typing statistics
    start_time = time.time()
    total_correct_chars = 0
    total_chars = 0
    
    # Display initial screen
    display_text(stdscr, target_text, current_text, wpm)
    
    while True:
        # Calculate and display current WPM
        if current_text:
            current_time = time.time()
            wpm = calculate_wpm(start_time, current_time, len(current_text))
        
        # Update display
        display_text(stdscr, target_text, current_text, wpm)
        
        # Get user input
        try:
            key = stdscr.getch()
        except:
            continue
        
        # Handle key input
        if key == 27:  # ESC
            break
        elif key == curses.KEY_BACKSPACE or key == 127 or key == 8:
            if current_text:
                current_text = current_text[:-1]
        elif 32 <= key <= 126:  # Printable ASCII characters
            char = chr(key)
            current_text += char
            total_chars += 1
            
            # Check if character is correct
            if len(current_text) <= len(target_text) and char == target_text[len(current_text) - 1]:
                total_correct_chars += 1
        
        # Check if test is complete
        if len(current_text) >= len(target_text):
            # Short pause to show completion
            display_text(stdscr, target_text, current_text, wpm)
            stdscr.timeout(1500)
            stdscr.getch()
            stdscr.timeout(-1)
            
            # Calculate final statistics
            end_time = time.time()
            final_wpm = calculate_wpm(start_time, end_time, total_chars)
            accuracy = (total_correct_chars / total_chars) * 100 if total_chars > 0 else 0
            
            # Generate new text for continued typing
            target_text = generate_target_text(words)
            current_text = ""
            start_time = time.time()
            total_correct_chars = 0
            total_chars = 0
    
    # Calculate final statistics
    end_time = time.time()
    final_wpm = calculate_wpm(start_time, end_time, total_chars)
    accuracy = (total_correct_chars / total_chars) * 100 if total_chars > 0 else 0
    
    return final_wpm, accuracy


def show_results(stdscr: 'curses._CursesWindow', wpm: float, accuracy: float) -> None:
    """
    Display the final typing test results.
    
    Args:
        stdscr: The curses window object
        wpm: Words per minute achieved
        accuracy: Typing accuracy percentage
    """
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    # Format and display results
    result_text = f"Your typing speed: {wpm:.2f} WPM"
    accuracy_text = f"Accuracy: {accuracy:.2f}%"
    exit_text = "Press any key to exit..."
    
    # Calculate center positions
    stdscr.addstr(h // 2 - 2, max(0, w // 2 - len(result_text) // 2), result_text)
    stdscr.addstr(h // 2, max(0, w // 2 - len(accuracy_text) // 2), accuracy_text)
    stdscr.addstr(h // 2 + 2, max(0, w // 2 - len(exit_text) // 2), exit_text)
    
    stdscr.refresh()
    stdscr.getch()


def main(stdscr: 'curses._CursesWindow') -> None:
    """
    Main function to initialize and run the typing test.
    
    Args:
        stdscr: The curses window object
    """
    # Set up curses
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    
    # Run typing test
    wpm, accuracy = run_typing_test(stdscr)
    
    # Show results
    show_results(stdscr, wpm, accuracy)


if __name__ == "__main__":
    try:
        wrapper(main)
    except KeyboardInterrupt:
        print("Typing test terminated.")
    except Exception as e:
        print(f"An error occurred: {e}")