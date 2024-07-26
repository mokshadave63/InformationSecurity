Alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
reversed_Alphabets = list(reversed(Alphabets))

plaintext = input("Enter your message: ")
key = int(input("Enter your key: "))
plaintext = plaintext.upper()

ciphertext = []
for char in plaintext:
    if char in Alphabets:
        index = Alphabets.index(char)
        new_char = reversed_Alphabets[index]
        new_index = (Alphabets.index(new_char) + key) % 26
        ciphertext.append(Alphabets[new_index])
    else:
        ciphertext.append(char)  

encrypted_message = ''.join(ciphertext)
print("Your encrypted message is:", encrypted_message)

decrypted_text = []
for char in ciphertext:
    if char in Alphabets:
        new_index = (Alphabets.index(char) - key) % 26
        new_char = Alphabets[new_index]
        index = reversed_Alphabets.index(new_char)
        decrypted_text.append(Alphabets[index])
    else:
        decrypted_text.append(char) 

original_message = ''.join(decrypted_text)
print("Your original message is:", original_message)
