"""
cryptography.py
Author: Daniel Wilson
Credit: Avery, Ethan

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!")
let = []
other = []

def encrypt(P):
    key=input("Key: ")
    P=list(P)
    z=0
    p=[]
    for x in P:
        p.append(associations.index(x))
    #print(p)
    c=[]
    for x in key:
        c.append(associations.index(x))
        z=z+1
    #print(c)
    C=[]
    q=0
    while z<len(c):
        C.append((p[x]+c[z%len(C)]%len(associations)))
        q=q+1
    #print(C)
    z=0
    K=[]
    while z<len(p):
        K.append(associations[c[z]])
        z=z+1
    #print(K)
    s=""
    for x in K:
        s=s+x
    print(s)
    return(s)
    '''
    for x in C:
        print(x,end="")
        print()

def decrypt(Z):
    key=input("Key: ")
    Z=list(Z)
    '''

def request_answer():
    id=input("Enter e to encrypt, d to decrypt, or q to quit")
    if id == "e":
        mes=str(input("Message: "))
        encrypt(mes)
    elif id == "d":
        mes=str(input("Message: "))
    elif id == "q":
        print("Goodbye!")
        return()
    else:
        print("Did not understand command, try again.")
        request_answer()
        
request_answer()