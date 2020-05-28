# Function that calculates x^m modulo n using O(log(m)) operations
def power(x, m, n):
    a = 1
    while m > 0:
        if m % 2 == 1:
            a = (a * x) % n
        x = (x * x) % n
        m //= 2
    return a

def encrypting(primeNumber, publicKey):
    result = power(primeNumber, publicKey[1], publicKey[0])
    return result


def decrypting(primeNumber, privateKey):
    result = power(primeNumber, privateKey[1], privateKey[0])
    return result
