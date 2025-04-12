"""Turtle racing game that takes user input for the number of racing turtles and displays a race with random movements."""
import turtle
import random
import time
from typing import List, Tuple

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "gray", "black"]


def no_of_racers() -> int:
    """
    Prompt the user to input the number of racers.
    
    Returns:
        int: Number of racers between 2 and 10
    """ 
    while True:
        try:
            racers = int(input("How many turtles do you want to race? (2-10): "))
            if racers < 2 or racers > 10:
                print("Error: Number of racers must be between 2 and 10.")
                continue
            return racers
            
        except ValueError:
            print("Error: Please enter a valid number.")
        

def create_turtles(colors: List[str]) -> List[turtle.Turtle]:
    """
    Create turtle objects for the race.
    
    Args:
        colors: List of colors for the turtles
        
    Returns:
        List of turtle objects
    """
    turtles = []
    spacingx = WIDTH / (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH/2 + (i + 1) * spacingx, -HEIGHT/2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles


def race(colors: List[str]) -> str:
    """
    Conduct the race until a turtle reaches the finish line.
    
    Args:
        colors: List of colors for the racing turtles
        
    Returns:
        The color of the winning turtle
    """
    turtles = create_turtles(colors)
    # Draw finish line
    finish_line = turtle.Turtle()
    finish_line.penup()
    finish_line.goto(-WIDTH/2, HEIGHT/2 - 10)
    finish_line.pendown()
    finish_line.hideturtle()
    finish_line.pensize(3)
    finish_line.forward(WIDTH)
    
    is_race_on = True
    while is_race_on:
        for racer in turtles:
            # Move the racer forward by a random amount
            distance = random.randrange(1, 20)
            racer.forward(distance)
            
            # Check if the racer has reached the finish line
            x, y = racer.pos()
            if y >= HEIGHT/2 - 10:
                is_race_on = False
                winning_color = colors[turtles.index(racer)]
                return winning_color
        # Small delay to make the race visible
        time.sleep(0.05)

def init_turtle() -> turtle.Screen:
    """
    Initialize the turtle screen with proper settings.
    
    Returns:
        The configured turtle screen object
    """
    screen = turtle.Screen()
    screen.title("Turtle Racing Game")
    screen.bgcolor("white")
    screen.setup(WIDTH, HEIGHT)
    return screen


def main() -> None:
    """Run the main turtle racing game program."""
    racers = no_of_racers()
    screen = init_turtle()
    
    # Select the colors based on number of racers
    race_colors = COLORS.copy()
    random.shuffle(race_colors)
    colors = race_colors[:racers]
    
    # Start the race
    winner = race(colors)
    print(f"The winner is the {winner} turtle!")
    
    # Keep the window open until clicked
    print("Click on the window to exit.")
    screen.exitonclick()


if __name__ == "__main__":
    main()