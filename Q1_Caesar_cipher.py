def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Example usage
if __name__ == "__main__":
    plaintext = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    
    encrypted_text = caesar_cipher_encrypt(plaintext, shift)
    print(f"Encrypted text: {encrypted_text}")
    
    decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
    print(f"Decrypted text: {decrypted_text}")