#password generator
import random
import string  # string module has all the letters, digits, and special characters.


def generate_password(min_length, numbers=True, special_characters=True):
    """
    Generate a secure random password.
    
    Args:
        min_length (int): The minimum length for the password.
        numbers (bool): Include numbers in the password if True.
        special_characters (bool): Include special characters in the password if True.
        
    Returns:
        str: A randomly generated password meeting the specified criteria.
    
    Raises:
        ValueError: If min_length is less than 1.
    """
    if min_length < 1:
        raise ValueError("Password length must be at least 1 character")
        
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters  # Start with letters as the base character set
    if numbers:  # Add digits if requested
        characters += digits
    if special_characters:  # Add special characters if requested
        characters += special
    
    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length: #this means that the password will keep generating until the criteria is met. that is, the password will keep generating until the length of the password is at least the minimum length and the password will have at least one number and one special character.
        new_char = random.choice(characters) #this is used to generate a random character from the characters string and add it to the password.
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers: #if we have a number in the password, then we set the meets_criteria to True. If we don't have a number in the password, then we set the meets_criteria to False.
            meets_criteria = has_numbers 
        if special_characters: #This will proceed even if the password doesn't have a number.
            meets_criteria = meets_criteria and has_special
        
    return pwd


def get_password_strength(password):
    """
    Evaluate the strength of a password.
    
    Args:
        password (str): The password to evaluate.
        
    Returns:
        str: A description of password strength (Weak, Medium, Strong, Very Strong).
    """
    # Check password composition
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    # Calculate score based on length and composition
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if has_upper and has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    
    # Return strength description
    if score < 2:
        return "Weak"
    elif score < 3:
        return "Medium"
    elif score < 5:
        return "Strong"
    else:
        return "Very Strong"


def main():
    """Run the password generator interactive CLI."""
    print("=== Secure Password Generator ===")
    
    try:
        min_length = int(input("Enter the minimum length: "))
        if min_length < 1:
            print("Password length must be at least 1 character. Using default of 8.")
            min_length = 8
    except ValueError:
        print("Invalid input. Using default length of 8.")
        min_length = 8
        
    numbers = input("Do you want to have numbers in your password? (y/n): ").lower() == "y"
    special = input("Do you want to have special characters in your password? (y/n): ").lower() == "y"
    
    try:
        pwd = generate_password(min_length, numbers, special)
        print("\nGenerated password:", pwd)
        print(f"Password strength: {get_password_strength(pwd)}")
        print(f"Password length: {len(pwd)} characters")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
