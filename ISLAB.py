def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        # Here we check that if the letter is an alphabet we shift it and if it's a number  or space we ignore it
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            # Apply shifting formula
            #Encrypt: shift the letter forward in the alphabet by 'shift' places,
            # wrap around using %26 if it goes past 'Z' or 'z'
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char

        else:
            result += char
    return result
# Function to decrypt the message
def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():

            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            # Decrypt: shift the letter backward in the alphabet by 'shift' places,
            # wrap around using %26 if it goes before 'A' or 'a'
            new_char = chr((ord(char) - start - shift) % 26 + start)
            result += new_char

        else:
            result += char

    return result

# Input Values For Encryption
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted_text = caesar_encrypt(message, shift)
print("Encrypted Text", encrypted_text)

decrypted_text = caesar_decrypt(encrypted_text, shift)
print("Decrypted Text", decrypted_text)
