#railfence cipher
pt=input("enter the plaintext")
key=int(input("enter the key"))
res=[["0" for j in range(0,len(pt))] for j in range(0,key)]
r,c=0,0
temp=1
for i in pt:
    res[r][c]=i
    c+=1
    if temp==1:
        r+=1
        if(r>=key-1):
            temp=0
    else:
        r-=1
        if r<=0:
            temp=1
for i in range(0,key):
    for j in range(0,len(pt)):
        if(res[i][j]!='0'):
            print(res[i][j],end=" ")
