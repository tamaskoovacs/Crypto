import random
import math

# privat kulcsot generalo fuggveny
def generate_private_key(n=8):
    # egy olyan sorozatot hozunk létre, amelynek minden elem nagyobb mint az elotte levo elemek összege
    w = []
    sum = 0
    for _ in range(n):
        value = random.randint(sum + 1, sum + n + 1)
        w.append(value)
        sum += value

    # generaljunk egy olyan erteket, amely nagyobb mint a sorozat osszes elemenek osszege
    q = sum + random.randint(1, n)

    # keressunk egy olyan szamot 2 es q kozott ami relativ prim q-val
    # addig generalunk random szamokat, amig nem talalunk egyet ami megfelelo
    r = 0
    while True:
        r = random.randint(2, q)
        if math.gcd(q, r) == 1:
            break

    print("privat kulcs generalva")
    # visszateritjuk a sorozatot es 2 szamot amik egyutt a kulcsot alkotjak
    return w, q, r


# a pulkikus kulcsot a pricat kulcs segitsegevel hozzuk letre keplet szerint
def create_public_key(private_key):
    w, q, r = private_key
    print("public kulcs generalva")
    return [(r * wi) % q for wi in w]

# enkriptalljuk az uzenetet byteonkent a public kulcs segitsegevel keplet szerint
def enkriptal(message, public_key):
    encrypted_chunks = []
    for chunk in message:
        a = [int(x) for x in bin(ord(chunk))[2:].zfill(8)] # byteokat binaris szamokká alakitjuk
        c = sum(ai * bi for ai, bi in zip(a, public_key)) # enkriptaljuk a byteokat a public kulcs segitsegevel
        encrypted_chunks.append(c)
    print("uzenet enkriptalva")
    return encrypted_chunks

# dekriptaljuk az uzenetet a public kulcs segitsegevel keplet szerint
def dekriptal(message, private_key):
    w, q, r = private_key
    s = modinv(r, q)
    decrypted_message = ""
    for c in message:
        c_prime = (c * s) % q
        decrypted_byte = solve_subset_sum(w, c_prime)
        decrypted_message += chr(int(''.join([str(bit) for bit in decrypted_byte]), 2))
    print("uzenet dekriptalva")
    return decrypted_message


# segedfuggveny amiben a moduláris inverz keresését használjuk
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError("Nem letezik moduláris inverz")
    else:
        return x % m

# segedfuggveny amiben euklidesz kiterjesztett algoritmusat hasznalunk
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# segedfüggvény mely az adott súlyokat és célösszeget használja a "superincreasing subset sum" probléma megoldásához.
def solve_subset_sum(w, c_prime):
    n = len(w)
    b = [0] * n
    for i in range(n - 1, -1, -1):
        if c_prime >= w[i]:
            b[i] = 1
            c_prime -= w[i]
    return b
