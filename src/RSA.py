from math import sqrt

x, y = 0, 1
def gcd(a, b):
    if (a == 0):
        return b
 
    return gcd(b % a, a)
def isPrime(n):
    # Corner case
    if (n <= 1):
        return False

    if (n % 2 == 0 or n % 3 == 0):
        return "false"
    # Check from 2 to sqrt(n)
    for i in range(5, int(sqrt(n)),6):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
 
    return True
def power(x, y, M):
    if (y == 0):
        return 1
    p = power(x, y // 2, M) % M
    p = (p * p) % M
    if(y % 2 == 0):
        return p
    else:
        return ((x * p) % M)
def gcdExtended(a, b):
    global x, y
    if (a == 0):
        x = 0
        y = 1
        return b
    gcd = gcdExtended(b % a, a)
    x1 = x
    y1 = y

    x = y1 - (b // a) * x1
    y = x1
    return gcd
def modInverse(A, M):
    g = gcdExtended(A, M)
    if (g != 1):
        print("Inverse doesn't exist")
    else:
        res = (x % M + M) % M
        print("Modular multiplicative inverse is ", res)
        return res
def encrypt(x, e, n):
    return (pow(x, e, n))
def decrypt(y, d, n):
    return (pow(y, d, n))
p = 997497979979
q = 197111971171
e = 197111971171333
n = p*q
if (isPrime(p) == False or isPrime(q) == False):
    print("Invalid input")
else:
    d = modInverse(e, (p-1)*(q-1))
    mes = 20020454
    en = encrypt(mes, e, n)
    de = decrypt(en, d, n)
    print ("Encryption of messenger is: ", en)
    print ("Decryption of the encryption is: ", de)
    
