def encrypt(text, rails, skip):
    # Create a 2D matrix to represent the rails
    rail_matrix = [['.' for _ in range(len(text))] for _ in range(rails)]

    row = 0
    direction = 1  # 1 for moving down, -1 for moving up

    # Traverse through the text
    for i in range(len(text)):
        rail_matrix[row][i] = text[i]

        # Adjust the direction if we're at the top or bottom rail
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        # Skip rows according to the skip factor
        row += direction * skip

        # Ensure the row stays within valid bounds
        if row < 0:
            row = 0
        if row >= rails:
            row = rails - 1

    # Collect the encrypted text from the rail matrix
    encrypted_text = ""
    for i in range(rails):
        for j in range(len(text)):
            if rail_matrix[i][j] != '.':
                encrypted_text += rail_matrix[i][j]

    return encrypted_text


def decrypt(text, rails, skip):
    # Create a 2D matrix to represent the rails
    rail_matrix = [['.' for _ in range(len(text))] for _ in range(rails)]

    row = 0
    direction = 1

    # Mark the positions that will hold characters
    for i in range(len(text)):
        rail_matrix[row][i] = '*'

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        # Skip rows according to the skip factor
        row += direction * skip

        # Ensure the row stays within valid bounds
        if row < 0:
            row = 0
        if row >= rails:
            row = rails - 1

    # Fill the rail matrix with the actual text
    index = 0
    for i in range(rails):
        for j in range(len(text)):
            if rail_matrix[i][j] == '*' and index < len(text):
                rail_matrix[i][j] = text[index]
                index += 1

    # Read the decrypted text following the zigzag pattern
    decrypted_text = ""
    row = 0
    direction = 1

    for i in range(len(text)):
        decrypted_text += rail_matrix[row][i]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        # Skip rows according to the skip factor
        row += direction * skip

        # Ensure the row stays within valid bounds
        if row < 0:
            row = 0
        if row >= rails:
            row = rails - 1

    return decrypted_text


if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    rails = int(input("Enter the number of rails: "))
    skip = int(input("Enter the skip factor: "))

    encrypted_text = encrypt(text, rails, skip)
    print("Encrypted:", encrypted_text)

    decrypted_text = decrypt(encrypted_text, rails, skip)
    print("Decrypted:", decrypted_text)
