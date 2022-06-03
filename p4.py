#vigener cipher
def generateKey(string,key):
    key=list(key)
    if(len(string)==len(key)):
        return (key)
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i%len(key)])
    return("".join(key))
def encrypt(string,key):
    encrypt_text=[]
    for i in range(len(string)):
        x=(ord(string[i])+ord(key[i]))%26
        x+=ord('A')
        encrypt_text.append(chr(x))
    return("".join(encrypt_text))
    
def decrypt(encrypt_text,key):
    orig_text=[]
    for i in range(len(encrypt_text)):
        x=(ord(encrypt_text[i])-ord(key[i])+26)%26
        x+=ord('A')
        orig_text.append(chr(x))
    return("".join(orig_text))
  

st=input("enter the plaintext")
k=input("enter the keyword")
string=st.upper()
keyword=k.upper()
key=generateKey(string,keyword)
encrypt_text=encrypt(string,key)
print("encrypted text is ",encrypt_text)
print("decrypted text is:",decrypt(encrypt_text,key))
