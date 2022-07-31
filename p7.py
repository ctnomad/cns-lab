import math
# from math import gcd

def gcd(a, h): 
    temp = -1
    while(True):
        temp = a%h
        if temp==0:
            return h
        a = h
        h = temp

def rsa(): 
    p = float(input("Enter one prime number "))
    q = float(input("Enter another prime number "))
    n=p*q;
    count = 0;
    totient = (p-1)*(q-1);
 
    #public key, e stands for encrypt
    e=2.0
    #Selecting a co-prime which satisfies e>1
    while(e<totient):
        count = gcd(e,totient)
        if(count==1):
            break
        else:
            e+=1
 
    #private key, d stands for decrypt
    d = 0
 
    #k can be any arbitrary value
    k = 2
 
    #choosing d such that it satisfies d*e = 1 + k * totient
    d = (1 + (k*totient))/e;


    msg = float(input("Enter message (m) value "))
    
    # Encryption c = (msg ^ e) % n
    cipher = msg**e
    cipher=math.fmod(cipher,n)
    #cipher = pow(msg, e, n)

    # Decryption m = (c ^ d) % n
    m = cipher**d
    m=math.fmod(m,n)
 
    print("Message data = ",msg);
    print("\np = ",p);
    print("q = ",q);
    print("n = pq = ",n);
    print("totient = ",totient);
    print("\ne = ",e);
    print("d = ",d);
    print("\nEncrypted data = ",cipher);
    print("\nDecrypted data = ",m);

rsa()
