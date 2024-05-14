alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]

direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceasar(direction, text, shift):
    if direction == 'encode':    
        cipher_text = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = (position + shift)
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encoded text is: {cipher_text}")
    else:
        plaintext = ""
        for letter in text:
            position = alphabet.index(letter)
            new_position = position - shift
            plaintext += alphabet[new_position]
        print(f"Your message was: {plaintext}")

ceasar(direction,text,shift)