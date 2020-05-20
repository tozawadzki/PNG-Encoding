import random, sys, os, rabinMiller
# Greatest common divisor
def GCD(a, b):
    while a!= 0:
        a, b = b%a, a
    return b

# Modular inverse - cryptomath module
def findModInverse(a, m):
    if GCD(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % m


def generateKey(keySize):
    # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
    p = rabinMiller.generateLargePrime(keySize)
    q = rabinMiller.generateLargePrime(keySize)
    n = p * q

    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if GCD(e, (p - 1) * (q - 1)) == 1:
            break

    # Step 3: Calculate d, the mod inverse of e.
    d = findModInverse(e, (p - 1) * (q - 1))
    publicKey = (n, e)
    privateKey = (n, d)
    print('Public key:', publicKey)
    print('Private key:', privateKey)
    return (publicKey, privateKey)

generateKey(1024)