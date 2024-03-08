def decrypt_caesar(ciphertext, shift):
    decrypted_text = ""

    for char in ciphertext:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Shift the character position by the specified amount
            char_code = ord(char)
            decrypted_char_code = (char_code - shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a')
            
            # Convert back to character and append to the decrypted text
            decrypted_text += chr(decrypted_char_code)
        else:
            # Keep non-alphabetic characters unchanged
            decrypted_text += char

    return decrypted_text

# Example usage:
cipher_text = "Kvtyez Jtyffcj Gzvinjqv Kvtyezbld Gifxirdzjkptqev n Gfcjtv qrgvnezrartv girbkptqev erltqrezv"
shift_amount = 1

decrypted_text = decrypt_caesar(cipher_text, shift_amount)
print("Original text:", cipher_text)
print("Decrypted text:", decrypted_text)