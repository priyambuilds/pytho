# Words Per Minute (WPM) Typing Test

A terminal-based application that tests typing speed and accuracy, built with Python's curses library.

## Features

- Real-time WPM calculation
- Color-coded feedback (green for correct typing, red for errors)
- Random word generation for varied typing practice
- Accuracy tracking
- Simple, terminal-based UI

## Requirements

- Python 3.6 or higher
- Terminal with color support

## Usage

Run the program with:

```bash
python main.py
```

## Controls

- Type the text displayed on the screen
- Press ESC to exit the program

## Testing

Run the tests with pytest:

```bash
pytest
```

## Project Structure

- `main.py` - Main application code
- `tests/` - Test directory containing unit tests

## How It Works

1. The program displays a string of random words
2. As you type, your input is compared character-by-character with the target text
3. Correctly typed characters are highlighted in green, errors in red
4. Your WPM is calculated in real-time
5. After completing a text, a new one is generated automatically
6. When you exit, your final WPM and accuracy are displayed 