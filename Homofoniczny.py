import random

HOMOPHONIC_MAP = {
    'A': ['01', '02', '03'],
    'B': ['04', '05'],
    'C': ['06', '07', '08'],
    'D': ['09', '10'],
    'E': ['11', '12', '13', '14', '15'],
    'F': ['16', '17'],
    'G': ['18', '19'],
    'H': ['20', '21', '22'],
    'I': ['23', '24', '25'],
    'J': ['26'],
    'K': ['27', '28'],
    'L': ['29', '30'],
    'M': ['31', '32'],
    'N': ['33', '34'],
    'O': ['35', '36', '37'],
    'P': ['38', '39'],
    'Q': ['40'],
    'R': ['41', '42', '43'],
    'S': ['44', '45', '46'],
    'T': ['47', '48', '49'],
    'U': ['50', '51'],
    'V': ['52', '53'],
    'W': ['54', '55'],
    'X': ['56'],
    'Y': ['57', '58'],
    'Z': ['59']
}


def invert_homophonic_map(homophonic_map):
    inverted_map = {}
    for letter, symbols in homophonic_map.items():
        for symbol in symbols:
            inverted_map[symbol] = letter
    return inverted_map


def homophonic_encrypt(text):
    text = text.upper()
    result = ""

    for letter in text:
        if letter in HOMOPHONIC_MAP:
            result += random.choice(HOMOPHONIC_MAP[letter])

    return result


def homophonic_decrypt(text):
    result = ""

    i = 0
    while i < len(text):
        if text[i:i + 2] in HOMOPHONIC_DECRYPT_MAP:
            result += HOMOPHONIC_DECRYPT_MAP[text[i:i + 2]]
            i += 2

    return result


if __name__ == "__main__":
    plaintext = "Kryptografia"

    encrypted_message = homophonic_encrypt(plaintext)
    print("Encrypted Message:", encrypted_message)

    HOMOPHONIC_DECRYPT_MAP = invert_homophonic_map(HOMOPHONIC_MAP)

    decrypted_message = homophonic_decrypt(encrypted_message)
    print("Decrypted Message:", decrypted_message)
