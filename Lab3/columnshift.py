def encrypt(text, rails, key):
    rail_matrix = [['.' for _ in range(len(text))] for _ in range(rails)]
    row, direction = 0, 1

    for i in range(len(text)):
        rail_matrix[row][i] = text[i]
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    intermediate = ""
    for i in range(rails):
        for j in range(len(text)):
            if rail_matrix[i][j] != '.':
                intermediate += rail_matrix[i][j]

    key_pairs = sorted([(key[i], i) for i in range(len(key))])

    columns = ["" for _ in range(len(key))]
    for i in range(len(intermediate)):
        columns[i % len(key)] += intermediate[i]

    encrypted_text = ""
    for _, idx in key_pairs:
        encrypted_text += columns[idx]

    return encrypted_text


def decrypt(text, rails, key):
    key_pairs = sorted([(key[i], i) for i in range(len(key))])

    column_size = len(text) // len(key)
    extra_chars = len(text) % len(key)

    columns = ["" for _ in range(len(key))]
    index = 0
    for i in range(len(key)):
        size = column_size + (1 if i < extra_chars else 0)
        columns[key_pairs[i][1]] = text[index:index + size]
        index += size

    intermediate = ""
    for i in range(len(text)):
        intermediate += columns[i % len(key)][i // len(key)]

    rail_matrix = [['.' for _ in range(len(intermediate))] for _ in range(rails)]
    row, direction = 0, 1

    for i in range(len(intermediate)):
        rail_matrix[row][i] = '*'
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    index = 0
    for i in range(rails):
        for j in range(len(intermediate)):
            if rail_matrix[i][j] == '*':
                rail_matrix[i][j] = intermediate[index]
                index += 1

    decrypted_text = ""
    row, direction = 0, 1
    for i in range(len(intermediate)):
        decrypted_text += rail_matrix[row][i]
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    return decrypted_text


if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    rails = int(input("Enter the number of rails: "))
    key = input("Enter the key for column shuffling: ")

    encrypted_text = encrypt(text, rails, key)
    print("Encrypted:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, rails, key)
    print("Decrypted:", decrypted_text)
