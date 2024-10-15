def encrypt(text, shifts, alphabet):
    result = ""
    shift_count = len(shifts)
    alphabet_size = len(alphabet)
    text = text.upper()

    for i in range(len(text)):
        if text[i] in alphabet:
            text_pos = alphabet.index(text[i])
            shift_value = shifts[i % shift_count]
            encrypted_char = alphabet[(text_pos + shift_value) % alphabet_size]
            result += encrypted_char

    return result


def decrypt(encrypted_text, shifts, alphabet):
    result = ""
    shift_count = len(shifts)
    alphabet_size = len(alphabet)

    for i in range(len(encrypted_text)):
        if encrypted_text[i] in alphabet:
            encrypted_pos = alphabet.index(encrypted_text[i])
            shift_value = shifts[i % shift_count]
            decrypted_char = alphabet[(encrypted_pos - shift_value + alphabet_size) % alphabet_size]
            result += decrypted_char

    return result

if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text= "Kryptografia!"
    shifts = [3, 1, 4, 1, 8, 4]

    # Encrypting
    encrypted_text = encrypt(text, shifts, alphabet)
    decrypted_text = decrypt(encrypted_text, shifts, alphabet)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)
