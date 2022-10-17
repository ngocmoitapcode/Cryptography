from math import sqrt
import random

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modInverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def isPrime( n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True
def power( x, y, p):
    res = 1 
    x = x % p 
    while (y > 0):
        if (y & 1):
            res = (res * x) % p
        y = y >> 1 # y = y/2
        x = (x * x) % p
    return res
def findPrimefactors(s, n) :
    while (n % 2 == 0) :
        s.add(2)
        n = n // 2
    for i in range(3, int(sqrt(n)), 2):
        while (n % i == 0) :
 
            s.add(i)
            n = n // i
    if (n > 2) :
        s.add(n)
def find_g(n) : # Primitive_Root
    s = set()
    if (isPrime(n) == False):
        return -1
    phi = n - 1
    findPrimefactors(s, phi)
    for r in range(2, phi + 1):
        flag = False
        for it in s:
            if (power(r, phi // it, n) == 1):
 
                flag = True
                break
        if (flag == False):
            return r
    return -1

def find_h(g, a, p) :
    return pow(g, a, p) # publicKey_sender
def encrypt(mes, g, h, r, p) :
    y1 = pow(g, r, p)
    y2 = mes * pow(h, r, p)
    return y1, y2
def decrypt(y1, y2, a, p) :
    y_temp = modInverse(pow(y1, a), p)
    return pow(y2 * y_temp, 1, p)



p = 472868766193183 # a random prime number limit 16digits long
g = find_g(p) # primitiveRoot
print()
a = random.randint(0, 1000) # random privateKey_sender
h = find_h(g, a, p) #publicKey_sender
print("Public key(p, g, h) =" , "(", p, ",", g, ",", h, ")")
#encryption
print("This is the encryption")
mes = 20020454
print("Message is:", mes)
r = random.randint(0, 1000) # random sprivateKey_receiver
my_encryption = encrypt(mes, g, h, r, p)
print("This is the ciphertext:", my_encryption)
y1 = my_encryption[0]
y2 = my_encryption[1]

#Decryption
x = decrypt(y1, y2, a, p)
print("This is the plaintext:", x)
