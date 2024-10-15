
def create_playfair_matrix(key):
    key = key.upper().replace("J", "I")  # Zamiana J z I
    matrix = []
    used_letters = []

    for char in key:
        if char not in used_letters and char in alphabet:
            matrix.append(char)
            used_letters.append(char)

    for char in alphabet:
        if char not in used_letters and char != 'J':
            matrix.append(char)

    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    """Find the row and column of a character in the 5x5 matrix."""
    for row_idx, row in enumerate(matrix):
        if char in row:
            return row_idx, row.index(char)
    return None

def process_digraphs(plaintext):
    """Splits plaintext into digraphs (pairs of letters) and handles duplicates."""
    plaintext = plaintext.upper().replace("J", "I")  # Treat J as I
    digraphs = []
    i = 0

    while i < len(plaintext):
        char1 = plaintext[i]
        char2 = plaintext[i + 1] if (i + 1) < len(plaintext) else "X"

        # Handle pairs of identical letters
        if char1 == char2:
            digraphs.append((char1, 'X'))  # Insert 'X' if letters are the same
            i += 1
        else:
            digraphs.append((char1, char2))
            i += 2

    if len(digraphs[-1]) == 1:  # Handle final single character
        digraphs[-1] = (digraphs[-1][0], 'X')

    return digraphs

def encrypt_digraph(matrix, digraph):
    """Encrypt a pair of letters (digraph) using the Playfair cipher rules."""
    char1, char2 = digraph
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)

    if row1 == row2:
        # Same row: shift right (wrap around)
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        # Same column: shift down (wrap around)
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        # Rectangle: swap columns
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_digraph(matrix, digraph):
    """Decrypt a pair of letters (digraph) using the Playfair cipher rules."""
    char1, char2 = digraph
    row1, col1 = find_position(matrix, char1)
    row2, col2 = find_position(matrix, char2)

    if row1 == row2:
        # Same row: shift left (wrap around)
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        # Same column: shift up (wrap around)
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        # Rectangle: swap columns
        return matrix[row1][col2] + matrix[row2][col1]

def playfair_encrypt(plaintext, key):
    """Encrypt a plaintext using the Playfair cipher."""
    matrix = create_playfair_matrix(key)
    digraphs = process_digraphs(plaintext)
    encrypted_message = ""

    for digraph in digraphs:
        encrypted_message += encrypt_digraph(matrix, digraph)

    return encrypted_message

def playfair_decrypt(ciphertext, key):
    """Decrypt a ciphertext using the Playfair cipher."""
    matrix = create_playfair_matrix(key)
    digraphs = process_digraphs(ciphertext)
    decrypted_message = ""

    for digraph in digraphs:
        decrypted_message += decrypt_digraph(matrix, digraph)

    return decrypted_message

# Example usage
if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "THIS SHOULD WORK"
    plaintext = "KRYPTOGRAFIAJESTFAJNA"

    print("Key Matrix:")
    matrix = create_playfair_matrix(key)
    for row in matrix:
        print(" ".join(row))

    encrypted = playfair_encrypt(plaintext, key)
    print("\nEncrypted:", encrypted)

    decrypted = playfair_decrypt(encrypted, key)
    print("Decrypted:", decrypted)
