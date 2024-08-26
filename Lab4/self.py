def encrypt(plaintext, key):
    plaintext = plaintext.lower()
    num_columns = len(key)
    num_rows = len(plaintext) // num_columns
    
    if len(plaintext) % num_columns != 0:
        num_rows += 1

    matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    index = 0
    for i in range(num_rows):
        for j in range(num_columns):
            if index < len(plaintext):
                matrix[i][j] = plaintext[index]
                index += 1

    sorted_key_indices = sorted((char, idx) for idx, char in enumerate(key))

    encrypted_text = ''
    for _, original_index in sorted_key_indices:
        column = ''.join(matrix[row][original_index] for row in range(num_rows))
        encrypted_text += column

    return encrypted_text

def decrypt(encrypted_text, key):
    num_columns = len(key)
    num_rows = len(encrypted_text) // num_columns

    if len(encrypted_text) % num_columns != 0:
        num_rows += 1

    sorted_key_indices = sorted((char, idx) for idx, char in enumerate(key))

    matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    index = 0
    for _, original_index in sorted_key_indices:
        for row in range(num_rows):
            if index < len(encrypted_text):
                matrix[row][original_index] = encrypted_text[index]
                index += 1

    decrypted_text = ''
    for row in matrix:
        decrypted_text += ''.join(row)

    return decrypted_text.strip()

def main():
    plaintext = input("Enter your text: ")
    key = input("Enter your key: ")

    encrypted_text = encrypt(plaintext, key)
    print("Encrypted text:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
