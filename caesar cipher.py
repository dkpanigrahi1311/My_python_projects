alphabets = list("abcdefghijklmnopqrstuvwxyz")
type_of_code = input("Type 'encode' for encoding the string, Type 'decode' for decoding the string")
original_text = input("Enter the text: ")
original_text = original_text.lower()
shift_number = int(input("Enter shift number: "))

def encoding(original_text, shift_number):
    cipher_text = ""
    for letter in original_text:    
        index_position = alphabets.index(letter) + shift_number
        index_position %= len(alphabets)
        cipher_text += alphabets[index_position]

    print(cipher_text)
def decoding(original_text, shift_number):
    cipher_text = ""
    for letter in original_text:    
        index_position = alphabets.index(letter) - shift_number
        index_position %= len(alphabets)
        cipher_text += alphabets[index_position]
    print(cipher_text)

if type_of_code == "encode":
    encoding(original_text, shift_number)
elif type_of_code == "decode":
    decoding(original_text, shift_number)
else:
    print("enter 'encode' or 'decode' text only")
