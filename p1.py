#ceasercipher
def encrypt(text,s):
    cipher=""
    for i in range(len(text)):
        char=text[i]
        if char==" ":
            cipher+=char
        elif(char.isupper()):
            cipher+=chr((ord(char)+s-65)%26+65)
        else:
            cipher+=chr((ord(char)+s-97)%26+97)
    return cipher
def decrypt(cipher,s):
    plaintext=""
    for i in range(len(cipher)):
        char=cipher[i]
        if char==" ":
            plaintext+=char
        elif(char.isupper()):
            plaintext+=chr((ord(char)-s-65)%26+65)
        else:
            plaintext+=chr((ord(char)-s-97)%26+97)
    return plaintext
text=input("enter the plaintext:")
s=int(input("enter the shift value key:"))
print("encrypted text is:",encrypt(text,s))
print("decrypted text",decrypt(encrypt(text,s),s))
