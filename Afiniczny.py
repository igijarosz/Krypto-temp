#szyfr afiniczny korzysta z funkcji C=(a*P+b)mod(m)

def encrypt(text, a, b, alphabet):
    result = ""
    m = len(alphabet)
    text = text.upper()

    for char in text:
        if char in alphabet:
            P = alphabet.index(char)
            C = (a * P + b) % m
            result += alphabet[C]

    return result


def decrypt(text, a, b, alphabet):
    m = len(alphabet)
    result = ""

    for char in text:
        if char in alphabet:
            C = alphabet.index(char)
            P = (pow(a, -1, m) * (C - b)) % m
            result += alphabet[P]

    return result

if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = "Kryptografia!"
    a = 5
    b = 8

    encrypted_text = encrypt(text, a, b, alphabet)
    decrypted_text = decrypt(encrypted_text, a, b, alphabet)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)
