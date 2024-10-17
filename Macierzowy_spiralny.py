def matrix_fill(text, rows, cols):
    """Fills a matrix in a row by row way, for encryption purposes"""
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    index = 0

    for r in range(rows):
        for c in range(cols):
            if index < len(text):
                matrix[r][c] = text[index]
            else:
                matrix[r][c] = 'X'
            index += 1

    return matrix


def matrix_read(matrix, rows, cols):
    """Reads a matrix in a row by row way, for dectryption purposes"""
    text = ''

    for r in range(rows):
        for c in range(cols):
            text += matrix[r][c]

    return text


def spiral_read(matrix, rows, cols):
    """reads a matrix in a spiral starting from top left and going counterclockwise, for encryption purposes"""
    direction = 0  # 0 - down, 1 - right, 2 - up, 3 - left
    len_r = rows - 1
    len_c = cols - 1
    curr_r = 0
    curr_c = 0
    spiral_text = []
    first_move = True

    while len_r > 0 or len_c > 0:

        if direction == 0:
            if first_move:
                spiral_text.append(matrix[curr_r][curr_c])

                for i in range(len_r):
                    curr_r += 1
                    spiral_text.append(matrix[curr_r][curr_c])

                len_r += 1
                first_move = False

            else:
                for i in range(len_r):
                    curr_r += 1
                    spiral_text.append(matrix[curr_r][curr_c])

                len_c -= 1

        if direction == 1:
            for i in range(len_c):
                curr_c += 1
                spiral_text.append(matrix[curr_r][curr_c])

            len_r -= 1

        if direction == 2:
            for i in range(len_r):
                curr_r -= 1
                spiral_text.append(matrix[curr_r][curr_c])

            len_c -= 1

        if direction == 3:
            for i in range(len_c):
                curr_c -= 1
                spiral_text.append(matrix[curr_r][curr_c])

            len_r -= 1

        direction = (direction + 1) % 4

    return ''.join(spiral_text)


def spiral_fill(rows, cols, text):
    """fills a matrix in a spiral starting from top left and going counterclockwise, for dectryption purposes"""
    direction = 0  # 0 - down, 1 - right, 2 - up, 3 - left
    len_r = rows - 1
    len_c = cols - 1
    curr_r = 0
    curr_c = 0
    first_move = True
    index = 0

    matrix = [['' for _ in range(cols)] for _ in range(rows)]

    for _ in range(len(text)):

        if direction == 0:
            if first_move:
                matrix[curr_r][curr_c] = text[index]

                for i in range(len_r):
                    curr_r += 1
                    index += 1
                    matrix[curr_r][curr_c] = text[index]

                len_r += 1
                first_move = False

            else:
                for i in range(len_r):
                    curr_r += 1
                    index += 1
                    matrix[curr_r][curr_c] = text[index]

                len_c -= 1

        if direction == 1:
            for i in range(len_c):
                curr_c += 1
                index += 1
                matrix[curr_r][curr_c] = text[index]

            len_r -= 1

        if direction == 2:
            for i in range(len_r):
                curr_r -= 1
                index += 1
                matrix[curr_r][curr_c] = text[index]

            len_c -= 1

        if direction == 3:
            for i in range(len_c):
                curr_c -= 1
                index += 1
                matrix[curr_r][curr_c] = text[index]

            len_r -= 1

        direction = (direction + 1) % 4

    return matrix


# 16 95

def encrypt_matrix_cipher(plaintext, rows, cols):
    matrix = matrix_fill(plaintext, rows, cols)
    encrypted_text = spiral_read(matrix, rows, cols)
    return encrypted_text


def decrypt_matrix_cipher(ciphertext, rows, cols):
    matrix = spiral_fill(rows, cols, ciphertext)
    decrypted_text = matrix_read(matrix, rows, cols)
    return decrypted_text


# Example usage
if __name__ == "__main__":
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    col_count = 95
    row_count = 16

    message = "Laboratories in applied cryptography number 3 - spiral matrix cipher encoder and decoder. The facilitator indicates one type of substituent cipher and one type of cipher to the student to realize. At the same time, it changes the cipher in depending on the student's student record book number. For example, for ciphers The size of the matrix can be defined by the last four digits of the Index. The first two digits of the four will describe, for example, the number of columns, and the last two are the number of lines of the matrix in which the ciphertext should be written. In the case of substitution ciphers, the last digit of the index may define the type of substitution cipher, and the penultimate one, for example, the shift, if it is a monoalphabetic shift substitution cipher. The student is to implement both ciphers in one of the scripting languages. The scripts should be written independently from scratch without using ready-made libraries. Choose any logical-sounding text no shorter than 100 characters and containing the word cryptography. The text should be encrypted using different passwords no longer than 12 characters for both types of cipher (if the encryption method allows it). Encrypt the same text with the same passwords using ready-made encryptors available on the websites indicated in point 2: 'Required software or environment' or from websites found independently. Also write scripts to decrypt your texts."

    message = message.upper()

    print("Original text:\n", message)

    encrypted_message = encrypt_matrix_cipher(message, row_count, col_count)
    print("\nEncrypted message:\n", encrypted_message)

    decrypted_message = decrypt_matrix_cipher(encrypted_message, row_count, col_count)
    print("\nDecrypted message:\n", decrypted_message)
