def encrypt(text, key, alphabet):
    result = ""
    text = text.upper()

    for char in text:
        if char in alphabet:

            pos = alphabet.index(char)
            result += key[pos]


    return result

def decrypt(encrypted_text, key, alphabet):
    result = ""

    for char in encrypted_text:
        if char in alphabet:

            pos = key.index(char)
            result += alphabet[pos]

    return result


if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "RZQALIKMTWCBGPHNFSUEDJVOYX"
    text = "Kryptografia!"
    shift = 3

    encrypted_text = encrypt(text, key, alphabet)
    decrypted_text = decrypt(encrypted_text, key, alphabet)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)
