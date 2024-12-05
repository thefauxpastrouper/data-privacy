import itertools
import string

# Target password to crack
password = "abc"

# Function to brute-force the password
def brute_force(target):
    # Characters to use for guessing (lowercase letters)
    chars = string.ascii_lowercase
    
    # Try combinations of increasing lengths
    for length in range(1, 6):  # Limit the max length to avoid infinite loops
        # Generate all possible combinations of the given length
        for guess in itertools.product(chars, repeat=length):
            # Combine the guessed characters into a string
            guess = ''.join(guess)
            print(f"Trying: {guess}")  # Show each attempt
            
            if guess == target:
                print(f"Password found: {guess}")
                return guess
    print("Password not found!")
    return None

# Simulate the attack
brute_force(password)
