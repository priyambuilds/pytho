#we want to randomly generate a bunch of different math questions and ask the users to solve them and not let them continue once they get it right and measure the time it takes for them to get it right.

import random
import time
import os

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_difficulty_settings():
    """Get difficulty settings from the user."""
    print("Choose difficulty level:")
    print("1. Easy (numbers 1-10, basic operations)")
    print("2. Medium (numbers 3-12, includes multiplication)")
    print("3. Hard (numbers 5-20, includes division)")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-3): "))
            if choice == 1:
                return {'min': 1, 'max': 10, 'operators': ['+', '-']}
            elif choice == 2:
                return {'min': 3, 'max': 12, 'operators': ['+', '-', '*']}
            elif choice == 3:
                return {'min': 5, 'max': 20, 'operators': ['+', '-', '*', '/']}
            else:
                print("Please enter a number between 1 and 3.")
        except ValueError:
            print("Please enter a valid number.")

def get_problem_count():
    """Get the number of problems from the user."""
    while True:
        try:
            count = int(input("How many problems would you like to solve? (5-20): "))
            if 5 <= count <= 20:
                return count
            else:
                print("Please enter a number between 5 and 20.")
        except ValueError:
            print("Please enter a valid number.")

def generate_problem(settings):
    """Generate a math problem based on difficulty settings."""
    left = random.randint(settings['min'], settings['max'])
    right = random.randint(settings['min'], settings['max'])
    operator = random.choice(settings['operators'])
    
    # Ensure division problems have clean answers
    if operator == '/':
        # Make sure we get a clean division result
        right = random.randint(1, 10)
        left = right * random.randint(1, settings['max'] // right)
    
    expr = f"{left} {operator} {right}"
    
    # Calculate the answer safely
    if operator == '+':
        answer = left + right
    elif operator == '-':
        answer = left - right
    elif operator == '*':
        answer = left * right
    else:  # operator == '/'
        answer = left // right
        
    return expr, answer

def format_time(seconds):
    """Format time in minutes and seconds."""
    minutes = seconds // 60
    seconds %= 60
    return f"{int(minutes)}m {seconds:.1f}s"

def main():
    """Main function to run the math quiz."""
    clear_screen()
    print("Welcome to the Math Practice Quiz!")
    print("=================================")
    
    settings = get_difficulty_settings()
    problems = get_problem_count()
    
    wrong = 0
    wrong_problems = []
    problem_times = []
    
    input("\nPress Enter to start the quiz...")
    clear_screen()
    print("Quiz started! Good luck!")
    print("=================================")
    
    overall_start_time = time.time()
    
    for i in range(problems):
        expr, answer = generate_problem(settings)
        problem_start_time = time.time()
        attempts = 0
        
        while True:
            try:
                guess = input(f"Problem #{i+1}: {expr} = ")
                attempts += 1
                
                if guess == str(answer):
                    problem_end_time = time.time()
                    problem_time = problem_end_time - problem_start_time
                    problem_times.append(problem_time)
                    print(f"Correct! (Time: {problem_time:.1f}s)")
                    break
                else:
                    print("Incorrect. Try again.")
                    wrong += 1
                    if attempts >= 3:
                        print(f"The correct answer is: {answer}")
                        wrong_problems.append(f"{expr} = {answer}")
                        break
            except ValueError:
                print("Please enter a valid number.")
        
        print("---------------------------------")
    
    overall_end_time = time.time()
    total_time = overall_end_time - overall_start_time
    
    clear_screen()
    print("\nQuiz Results")
    print("=================================")
    print(f"Total problems: {problems}")
    print(f"Correct answers: {problems - len(wrong_problems)}")
    print(f"Incorrect attempts: {wrong}")
    print(f"Accuracy rate: {(problems - len(wrong_problems)) / problems * 100:.1f}%")
    print(f"Total time: {format_time(total_time)}")
    
    if problem_times:
        avg_time = sum(problem_times) / len(problem_times)
        fastest_time = min(problem_times)
        slowest_time = max(problem_times)
        print(f"Average time per problem: {avg_time:.1f}s")
        print(f"Fastest problem: {fastest_time:.1f}s")
        print(f"Slowest problem: {slowest_time:.1f}s")
    
    if wrong_problems:
        print("\nProblems to review:")
        for idx, problem in enumerate(wrong_problems):
            print(f"{idx+1}. {problem}")
    
    play_again = input("\nWould you like to play again? (y/n): ").lower()
    if play_again == 'y':
        main()
    else:
        print("Thanks for playing! Goodbye!")

if __name__ == "__main__":
    main()


