def read_leaked_passwords(leaked_password_file):
    """
    Read the leaked passwords from the file and return a set for faster lookup.
    """
    leaked_passwords = set()  # Using a set for O(1) average-time complexity lookups
    with open(leaked_password_file, 'r') as file:
        for line in file:
            leaked_passwords.add(line.strip())  # Remove newline characters
    return leaked_passwords

def check_password_leaks(username_password_file, leaked_passwords):
    """
    Check if passwords from the username_password_file are leaked by comparing them with the leaked passwords.
    """
    with open(username_password_file, 'r') as file:
        for line in file:
            username, password = line.strip().split(',')
            if password in leaked_passwords:
                print(f"Password for username {username} has been leaked!")
            else:
                print(f"Password for username {username} is safe.")

# Example Usage
username_password_file = 'user_credentials.txt'  # Replace with the path to your username_password file
leaked_password_file = 'leak_password.txt'      # Replace with the path to your leaked_password file

# Read leaked passwords into a set for fast lookup
leaked_passwords = read_leaked_passwords(leaked_password_file)

# Check each password from the username_password file
check_password_leaks(username_password_file, leaked_passwords)
