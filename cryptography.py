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
    s=0
    p=[]
    for x in P:
        p.append(associations.index(x))
    print(p)
    c=[]
    for x in key:
        c.append((p[z]+c[z%len(c)]))
        z=z+1
    print(c)
    z=0
    C=[]
    while z>len(c):
        C.append(associations[c[z]])
        z=z+1
    print(C)
    
    
    for x in C:
        print(x,end="")
        print()


def decrypt(Z):
    key=input("Key: ")
    Z=list(Z)
    

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