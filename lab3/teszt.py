from Knapsack import *

privat = generate_private_key(8)
publik = create_public_key(privat)
print(privat)
print(publik)

mesage = 'teszt knapsack'
print("eredeti uzenet: " + mesage)

ciphertext = enkriptal(mesage, publik)
print(ciphertext)
decripetd = dekriptal(ciphertext, privat)
print(decripetd)