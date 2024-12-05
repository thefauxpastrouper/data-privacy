import random

def load_words_from_file(file_path):
    """Loads words from a dictionary file into a list."""
    try:
        with open(file_path, 'r') as file:
            words = [line.strip() for line in file if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def generate_password(word_list, word_count=4):
    """Generates a password by combining random words from the word list."""
    if not word_list:
        print("Error: No words available to generate a password.")
        return ""
    password_words = random.sample(word_list, min(word_count, len(word_list)))
    return ''.join(password_words)

# Specify the path to your dictionary file
dictionary_file = "dictionary.txt"  # Replace with the actual path to your file
words = load_words_from_file(dictionary_file)

# Generate and print a password
if words:
    password = generate_password(words)
    print(f"Generated Password: {password}")
