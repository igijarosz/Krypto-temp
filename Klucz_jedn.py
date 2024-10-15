import random


def generate_random_key(length):
    return ''.join(random.choice(alphabet) for _ in range(length))


def encrypt(text, key):
    result_bin = []

    for i in range(len(text)):
        if text[i] in alphabet:
            text_char = text[i]
            key_char = key[i]

            encrypted_char_bin = bin(ord(text_char) ^ ord(key_char))

            result_bin.append(encrypted_char_bin)

    return result_bin


def decrypt(text_bin, key):
    result = ""

    for i in range(len(text_bin)):
        text_char = chr(int(text_bin[i], 2))
        key_char = key[i]

        decrypted_char = chr(ord(text_char) ^ ord(key_char))

        result += decrypted_char
    return result


if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = "Kryptografia!"


    text = text.upper()
    for i in text:
        if i in alphabet:
            pass
        else:
            text = text.replace(i, "")
    print("Text To Encrypt:      ", text)

    key = generate_random_key(len(text))
    print("Generated Key:      ", key)

    encrypted_text = encrypt(text, key)
    decrypted_text = decrypt(encrypted_text, key)

    print("Encrypted Text Binary:     ", end="")
    for i in encrypted_text:
        print(i[2:].zfill(8), end=" ")
    print("\nDecrypted Text:     ", decrypted_text)
