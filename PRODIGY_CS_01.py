def caesar_cipher_encrypt(text,shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                shift_amount = 65
            else:
                shift_amount = 97
            encrypted_text += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text,shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (E)Encrypt or (D)Decrypt? Enter Q to quit:")
        if choice == 'Q':
            break
        if choice not in ['E','D']:
            print("invalid choice. please enter E,D or Q.")
            continue
        text = input("enter your message:")
        shift = int(input("enter the shift value:"))

        if choice == 'E':
            print("Encrypted message:",caesar_cipher_encrypt(text,shift))
        else:
            print("Decrypted message:",caesar_cipher_decrypt(text,shift))

if __name__ == "__main__":
    main()                 
