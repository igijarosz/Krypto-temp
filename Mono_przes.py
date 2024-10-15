'''Szyfr monoalfabetyczny przesunięciowy, czyli tzw. cezar'''


def encrypt(text, shift, alphabet):
    result = ""
    alphabet_size = len(alphabet)
    text = text.upper()

    for char in text:
        if char in alphabet:

            pos = alphabet.index(char)
            new_pos = (pos + shift) % alphabet_size
            result += alphabet[new_pos]


    return result

def decrypt(text, shift, alphabet):
    result = ""
    alphabet_size = len(alphabet)
    text = text.upper()

    for char in text:
        if char in alphabet:

            pos = alphabet.index(char)
            new_pos = (pos - shift) % alphabet_size
            result += alphabet[new_pos]

    return result


if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = "Kryptografia!"
    shift = 3

    encrypted_text = encrypt(text, shift, alphabet)
    decrypted_text = decrypt(encrypted_text, 3, alphabet)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)
