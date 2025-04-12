"""
Maze Path Finder

This program visualizes the BFS algorithm to find the shortest path 
through mazes. It uses the curses library for visualization.
"""
import curses
from curses import wrapper
import queue
import time
import sys
import os
import argparse

# Maze representations
MAZE_1 = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

MAZE_2 = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", "O", " ", " ", " ", " ", "#", " ", " ", " ", "#"],
    ["#", "#", "#", "#", " ", " ", "#", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", "#", "#", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", "#", " ", " ", "#", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#", "#", " ", "#"],
    ["#", "#", "#", "#", "#", "#", " ", "#", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", "#", " ", "#", "#"],
    ["#", " ", "#", "#", "#", "#", "#", "#", " ", " ", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", " ", "X", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

# Default maze
maze = MAZE_1

def find_start(maze, start):
    """
    Find the starting position in the maze.
    
    Args:
        maze: The maze represented as a 2D list
        start: The character representing the start position
        
    Returns:
        The (row, col) coordinates of the starting position, or None if not found
    """
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None

def find_path_bfs(maze, stdscr, animation_speed=0.2):
    """
    Find the shortest path using Breadth-First Search algorithm.
    
    Args:
        maze: The maze represented as a 2D list
        stdscr: The curses window object for display
        animation_speed: Delay between animation frames in seconds
        
    Returns:
        A list of coordinates representing the path, or None if no path found
    """
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)
    if not start_pos:
        return None

    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    visited = set([start_pos])
    
    steps = 0
    nodes_explored = 0

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos
        nodes_explored += 1

        stdscr.clear()
        print_maze(maze, stdscr, path)
        stdscr.addstr(len(maze) + 1, 0, f"Algorithm: BFS | Steps: {steps} | Nodes Explored: {nodes_explored}")
        stdscr.addstr(len(maze) + 2, 0, f"Speed: {animation_speed:.2f}s | Press 'q' to quit, '+' to speed up, '-' to slow down")
        time.sleep(animation_speed)
        stdscr.refresh()
        
        # Check for user input during algorithm execution
        try:
            key = stdscr.getkey()
            if key == 'q':
                return None
            elif key == '+' and animation_speed > 0.05:
                animation_speed -= 0.05 #decrease speed
            elif key == '-':
                animation_speed += 0.05 #increase speed
        except:
            pass

        if maze[row][col] == end:
            return path, steps, nodes_explored
        
        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            r, c = neighbor
            if maze[r][c] == "#":
                continue
            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)
            steps += 1

    return None

def find_neighbors(maze, row, col):
    """
    Find all valid neighboring cells for a given position.
    
    Args:
        maze: The maze represented as a 2D list
        row: The current row position
        col: The current column position
        
    Returns:
        A list of (row, col) tuples representing valid neighboring positions
    """
    neighbors = []
    
    if row > 0:  # Up
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # Down
        neighbors.append((row + 1, col))
    if col > 0:  # Left
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # Right
        neighbors.append((row, col + 1))
    return neighbors

def print_maze(maze, stdscr, path=None):
    """
    Print the maze with the path highlighted.
    
    Args:
        maze: The maze represented as a 2D list
        stdscr: The curses window object for display
        path: List of coordinates representing the current path
    """
    if path is None:
        path = []
        
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    GREEN = curses.color_pair(3)
    YELLOW = curses.color_pair(4)

    for i, row in enumerate(maze): #enumerate is used to get the index and value of the maze
        for j, value in enumerate(row): #if and else statements are used to check if the current position is in the path.
            if (i, j) in path: #if the current position is in the path
                if maze[i][j] == "O": #start position
                    stdscr.addstr(i, j*2, "O", GREEN)
                elif maze[i][j] == "X": #end position
                    stdscr.addstr(i, j*2, "X", YELLOW)
                else:
                    stdscr.addstr(i, j*2, "•", RED) # this is used to highlight the path
            else: #if the current position is not in the path
                if value == "O":
                    stdscr.addstr(i, j*2, value, GREEN)
                elif value == "X":
                    stdscr.addstr(i, j*2, value, YELLOW)
                else:
                    stdscr.addstr(i, j*2, value, BLUE)

def load_maze_from_file(file_path):
    """
    Load a maze from a text file.
    
    Args:
        file_path: Path to the maze file
        
    Returns:
        The maze represented as a 2D list
    """
    try:
        with open(file_path, 'r') as f:
            return [list(line.strip()) for line in f.readlines()]
    except Exception as e:
        print(f"Error loading maze: {e}")
        sys.exit(1)

def display_menu(stdscr):
    """
    Display a menu to select maze and algorithm.
    
    Args:
        stdscr: The curses window object for display
        
    Returns:
        A tuple of (selected_maze, animation_speed)
    """
    curses.curs_set(0)
    
    current_row = 0
    menu = ["Maze 1", "Maze 2", "Load from file", "Animation Speed: 0.2", "Start", "Exit"]
    selected_maze = MAZE_1
    animation_speed = 0.2
    
    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        
        # Print the title
        title = "Maze Path Finder"
        stdscr.addstr(1, (w - len(title)) // 2, title, curses.A_BOLD)
        
        # Print menu items
        for i, item in enumerate(menu):
            x = w // 2 - len(item) // 2
            y = h // 2 - len(menu) // 2 + i
            
            if i == current_row:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, x, item)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, item)
        
        # Instructions
        stdscr.addstr(h-2, 2, "Use arrow keys to navigate, Enter to select")
        
        # Refresh the screen
        stdscr.refresh()
        
        # Get user input
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:  # Enter key
            if current_row == 0:  # Maze 1
                selected_maze = MAZE_1
                menu[0] = "Maze 1 ✓"
                menu[1] = "Maze 2"
                menu[2] = "Load from file"
            elif current_row == 1:  # Maze 2
                selected_maze = MAZE_2
                menu[0] = "Maze 1"
                menu[1] = "Maze 2 ✓"
                menu[2] = "Load from file"
            elif current_row == 2:  # Load from file
                stdscr.clear()
                stdscr.addstr(h//2, 2, "Enter file path: ")
                curses.echo()
                file_path = stdscr.getstr(h//2, 17, 100).decode('utf-8')
                curses.noecho()
                if os.path.exists(file_path):
                    selected_maze = load_maze_from_file(file_path)
                    menu[0] = "Maze 1"
                    menu[1] = "Maze 2"
                    menu[2] = f"File: {os.path.basename(file_path)} ✓"
                else:
                    stdscr.addstr(h//2 + 1, 2, "File not found! Press any key...")
                    stdscr.getch()
            elif current_row == 3:  # Animation Speed
                stdscr.addstr(h//2, 2, "Enter speed (0.05-1.0): ")
                curses.echo()
                try:
                    speed = float(stdscr.getstr(h//2, 26, 5).decode('utf-8'))
                    if 0.05 <= speed <= 1.0:
                        animation_speed = speed
                        menu[3] = f"Animation Speed: {animation_speed}"
                except:
                    pass
                curses.noecho()
            elif current_row == 4:  # Start
                return selected_maze, animation_speed
            elif current_row == 5:  # Exit
                sys.exit(0)

def main(stdscr):
    """
    Main function to run the maze path finder.
    
    Args:
        stdscr: The curses window object for display
    """
    # Setup
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Maze Path Finder")
    parser.add_argument("-f", "--file", help="Path to maze file")
    parser.add_argument("-s", "--speed", type=float, default=0.2, help="Animation speed (seconds)")
    parser.add_argument("-m", "--maze", type=int, choices=[1, 2], help="Built-in maze number")
    parser.add_argument("--no-menu", action="store_true", help="Skip menu and run with arguments")
    
    try:
        args, _ = parser.parse_known_args()
    except:
        args = None
    
    global maze
    animation_speed = 0.2
    
    # Either use command line arguments or show menu
    if args and args.no_menu:
        if args.file:
            maze = load_maze_from_file(args.file)
        elif args.maze == 2:
            maze = MAZE_2
        animation_speed = args.speed
    else:
        maze, animation_speed = display_menu(stdscr)
    
    # Run the BFS algorithm
    result = find_path_bfs(maze, stdscr, animation_speed)
    
    # Display results and wait for user to press 'q' to exit
    if result:
        path, steps, nodes = result
        while True:
            stdscr.clear()
            print_maze(maze, stdscr, path)
            stdscr.addstr(len(maze) + 1, 0, f"Path found! Length: {len(path)}, Steps taken: {steps}, Nodes explored: {nodes}")
            stdscr.addstr(len(maze) + 2, 0, "Press 'q' to exit...")
            stdscr.refresh()
            
            # Wait for the 'q' key
            try:
                key = stdscr.getkey()
                if key.lower() == 'q':
                    break
            except:
                time.sleep(0.1)  # Small delay to reduce CPU usage
    else:
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "No path found or search canceled!")
            stdscr.addstr(1, 0, "Press 'q' to exit...")
            stdscr.refresh()
            
            # Wait for the 'q' key
            try:
                key = stdscr.getkey()
                if key.lower() == 'q':
                    break
            except:
                time.sleep(0.1)  # Small delay to reduce CPU usage

if __name__ == "__main__":
    wrapper(main)