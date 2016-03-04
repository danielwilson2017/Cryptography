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
        p.append(associations.find())
    




id=input("Enter e to encrypt, d to decrypt, or q to quit: ")
if id not in('e', 'd', 'q'):
    print("Did not understand command, try again")
    id=input("Enter e to encrypt, d to decrypt, or q to quit: ")

'''
if id == "e":
    message=str(input("Message: "))
    key=input("Key: ")
    l=len(message)
    k=len(key)
    for x in range(0, l):
        let.apend(associations.find(message[x])
    for y in range(0, k):
        let.apend(associations.find(message[y])
elif id=="d" :
    dcrpt=input("Message: ")
    key=str(input("Key: "))
elif id == "q" :
    print("Goodbye!")
'''