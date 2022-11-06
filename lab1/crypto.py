#!/usr/bin/env python3 -tt
"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: Kovacs Tamas
SUNet: ktim2035
"""
# Caesar Cipher

def encrypt_caesar(plaintext):
    """Encrypt plaintext using a Caesar cipher.
    Add more implementation details here.
    """
    encoded_text = ''
    uppercase_leters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in plaintext:
        if i in uppercase_leters:
            encoded_text += uppercase_leters[(ord(i) - ord('A') + 3) % len(uppercase_leters)]
    return encoded_text

def decrypt_caesar(ciphertext):
    """Decrypt a ciphertext using a Caesar cipher.
    Add more implementation details here.
    """
    decoded_text = ''
    uppercase_leters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in ciphertext:
        if i in uppercase_leters:
            decoded_text += uppercase_leters[(ord(i) - ord('A') - 3) % len(uppercase_leters)]
    return decoded_text


# Vigenere Cipher

def encrypt_vigenere(plaintext, keyword):
    """Encrypt plaintext using a Vigenere cipher with a keyword.
    Add more implementation details here.
    """
    # repeating keyword until desired length is reached
    len_plaintext = len(plaintext)
    keyword = (keyword * (int(len_plaintext/len(keyword))+1))[:len_plaintext] # mindig ismeteljuk 1-el tobbszor a vegen ugy is csak a plain_text hosszig vesszuk oket

    encoded_text = ''
    uppercase_leters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(plaintext)):
        if plaintext[i] in uppercase_leters:
            encoded_text += uppercase_leters[(ord(plaintext[i]) - ord('A') + ord(keyword[i]) - ord('A')) % len(uppercase_leters)] # plaintext asci sorszama + key asci sorszama leszazalekolva h ne lepjunk ki
    return encoded_text
    


def decrypt_vigenere(ciphertext, keyword):
    len_plaintext = len(ciphertext)
    keyword = (keyword * (int(len_plaintext/len(keyword))+1))[:len_plaintext]

    decoded_text = ''
    uppercase_leters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(ciphertext)):
        if ciphertext[i] in uppercase_leters:
            decoded_text += uppercase_leters[(ord(ciphertext[i]) - ord('A') - ord(keyword[i]) - ord('A')) % len(uppercase_leters)]
    return decoded_text


# Scytale Cipher

def encrypt_scytale(plaintext, circumference):
    circumference = int(circumference)
    encoded_text = []
    for i in range(circumference):
        encoded_text.append(plaintext[i::circumference]) # az encode test hez minden iteracioban hozzafuzunk egy uj listat aminek alemei a plaintext karakterei i tol kezdve minden circumferenced -ik elem
    return ''.join(encoded_text)

def decrypt_scytale(ciphertext, circumference):
    circumference = int(circumference)
    decoded_text = []
    for i in range(circumference):
        decoded_text.append(ciphertext[i::len(ciphertext) // circumference])
    return (''.join(decoded_text))[:len(ciphertext)]


# Railfence Cipher

def encrypt_railfence(plaintext, num_rails):
    num_rails = int(num_rails)
    encripted =''
    lines = {}
    for i in range(1, num_rails + 1): #adatszerkezet felepites
        lines[i] = []

    # lines {
    #    1 : [],
    #    2 : [], 
    #    3 : []
    # }

    index = 1
    irany = 1
    for caracter in plaintext:
        lines[index].append(caracter)
        if index == 1:
            irany = 1
        elif index == num_rails:
            irany = -1
        index += irany
    
    for line in lines.values():
        encripted += ''.join(line)
    return encripted

def decrypt_railfence(ciphertext, num_rails):
    num_rails = int(num_rails)
    len_text = len(ciphertext)
    lengths = [0] * num_rails # csinalunk egy listat num rails nullassal
    lengths[0] = lengths[num_rails - 1] = len_text // (num_rails * 2 - 2) # az elso es utolso zigzagban hany elem van
    for i in range(1, num_rails - 1): # elso es utolso sor kozotti sorokban hany elem van
        lengths[i] = (len_text // (num_rails * 2 - 2)) * 2
    rest = len_text % (num_rails * 2 - 2) # megmondja, hogy a teljes zigzagok utan a fel zigzabgban hany elem van
    for i in range(num_rails-1): # felfele megyunk
        if rest == 0:
            break
        else:
            lengths[i] += 1
        rest -= 1
    for i in range(num_rails - 2, 2, -1): # lefele megyunk
        if rest == 0:
            break
        else:
            lengths[i] += 1
        rest -= 1
    
    lines = {}
    for i in range(0, num_rails):
        lines[i] = ciphertext[0:lengths[i]]
        ciphertext = ciphertext[lengths[i]:]
    
    # eredmenyek osszefuzese zigzag alapjan
    decripted = ''
    index = 1
    irany = 1
    for _ in range(len_text):
        decripted += lines[index - 1][0]
        lines[index - 1] = lines[index - 1][1:]
        if index == 1:
            irany = 1
        elif index == num_rails:
            irany = -1
        index += irany
    
    return decripted