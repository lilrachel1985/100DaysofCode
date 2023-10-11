alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(text,shift,alphabet,direction):
  result =""
  if direction =='encode':
    for letter in text:
      position = alphabet.index(letter)
      new_position = position + shift
      result += alphabet[new_position]
    print(f"The encoded text is {result}")
  elif direction=="decode":
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        result += alphabet[new_position]
    print(f"The decoded text is {result}")


#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(text=text,shift=shift,alphabet=alphabet,direction=direction)           







