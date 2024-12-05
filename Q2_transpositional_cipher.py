def rail_fence_encrypt(text, num_rails):
    if num_rails <= 1 or num_rails >= len(text):
        return text

    rails = [''] * num_rails
    row, step = 0, 1

    for char in text:
        rails[row] += char
        # Zigzag direction control
        if row == 0:
            step = 1
        elif row == num_rails - 1:
            step = -1
        row += step

    return ''.join(rails)

def rail_fence_decrypt(ciphertext, num_rails):
    if num_rails <= 1 or num_rails >= len(ciphertext):
        return ciphertext

    # Create a zigzag pattern to track positions
    pattern = [0] * len(ciphertext)
    row, step = 0, 1
    for i in range(len(ciphertext)):
        pattern[i] = row
        if row == 0:
            step = 1
        elif row == num_rails - 1:
            step = -1
        row += step

    # Determine the length of each rail
    rail_lengths = [pattern.count(r) for r in range(num_rails)]

    # Divide ciphertext into rails based on calculated lengths
    rails = []
    index = 0
    for length in rail_lengths:
        rails.append(ciphertext[index:index + length])
        index += length

    # Reconstruct plaintext by following the zigzag pattern
    rail_indices = [0] * num_rails
    result = []
    for r in pattern:
        result.append(rails[r][rail_indices[r]])
        rail_indices[r] += 1

    return ''.join(result)

# Example usage
if __name__ == "__main__":
    plaintext = input("Enter the text to encrypt: ")
    num_rails = int(input("Enter the number of rails: "))

    encrypted = rail_fence_encrypt(plaintext, num_rails)
    print(f"Encrypted text: {encrypted}")

    decrypted = rail_fence_decrypt(encrypted, num_rails)
    print(f"Decrypted text: {decrypted}")
