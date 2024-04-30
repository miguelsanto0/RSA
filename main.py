import random

import sympy


def gcd(a, b):
    """Calculate the Greatest Common Divisor of two numbers."""
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Calculate the Extended Euclidean Algorithm of two numbers."""
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def generate_prime():
    """Generate a random prime number."""
    while True:
        num = random.randrange(2 ** (512 - 1), 2 ** 512)
        if sympy.isprime(num):
            return num


def generate_keys():
    """Generate RSA keys."""
    p = generate_prime()
    q = generate_prime()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    if gcd(e, phi) != 1:
        return generate_keys()

    _, d, _ = extended_gcd(e, phi)
    if d < 0:
        d += phi

    print("p is ", p)
    print("q is ", q)
    print("n is ", n)
    print("d is ", d)
    return (e, n), (d, n)

def encrypt(message, public_key):
    """Encrypt a message using RSA."""
    e, n = public_key
    message_to_int = int(message)
    ciphertext = pow(message_to_int, e, n)
    return ciphertext

def decrypt(ciphertext, private_key):
    """Decrypt a ciphertext using RSA."""
    d, n = private_key
    message_to_int = int(ciphertext)
    ciphertext = pow(message_to_int, d, n)
    return ciphertext


public_key, private_key = generate_keys()

message = input("Enter Message to encrypt here: ")
ciphertext = encrypt(message, public_key)
print(f"Ciphertext: {ciphertext}")
decryption = input("Enter message to decrypt here:")
decrypted_message = decrypt(decryption, private_key)
print(f"Decrypted message: {decrypted_message}")