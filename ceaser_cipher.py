alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text=input("type your message:\n").lower()
shift=int(input("Type the shift number:\n"))
def cipher(text,shift,direction):
    if direction=="decode":
        shift*=-1
    cipher_text=""
    for letter in text:
        if letter in alphabet:
           cipher_text+=alphabet[(alphabet.index(letter)+shift)%len(alphabet)]   
        else :
            cipher_text+=letter
    print(f"The {direction}d text is {cipher_text}")
cipher(text,shift,direction)







