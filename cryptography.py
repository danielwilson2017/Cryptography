"""
cryptography.py
Author: Daniel Wilson
Credit: Avery

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
let = []
other = []

id=input("Enter e to encrypt, d to decrypt, or q to quit: ")
if id not in('e', 'd', 'q'):
    print("Did not understand command, try again")
    id=input("Enter e to encrypt, d to decrypt, or q to quit: ")


if id == "e":
    message=input("Message: ")
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