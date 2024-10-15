'''Szyfr podstawieniowy polialfabetyczny, czyli szyfr Viegenera'''


def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return key


def encrypt(text, key, alphabet):
    result = ""
    key = generate_key(text, key)
    alphabet_size = len(alphabet)
    text = text.upper()

    for i in range(len(text)):
        if text[i] in alphabet:
            text_pos = alphabet.index(text[i])
            key_pos = alphabet.index(key[i])
            encrypted_char = alphabet[(text_pos + key_pos) % alphabet_size]

            result += encrypted_char

    return str(result)


def decrypt(encrypted_text, key, alphabet):
    result = ""
    key = generate_key(encrypted_text, key)
    alphabet_size = len(alphabet)

    for i in range(len(encrypted_text)):
        if encrypted_text[i] in alphabet:
            encrypted_pos = alphabet.index(encrypted_text[i])
            key_pos = alphabet.index(key[i])
            decrypted_char = alphabet[(encrypted_pos - key_pos + alphabet_size) % alphabet_size]

            result += decrypted_char

    return result


if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = "Kryptografia!"
    key = "AMOGUS"

    encrypted_text = encrypt(text, key, alphabet)
    decrypted_text = decrypt(encrypted_text, key, alphabet)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)
