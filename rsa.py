import random
from math import gcd


def generate_prime_candidate(length):
    """Generate an odd integer randomly of the specified bit length."""
    return random.getrandbits(length) | (1 << length - 1) | 1


def is_prime(n, k=5):
    """Test if a number is prime using Miller-Rabin primality test."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as d*2^r + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Test for k rounds
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # Compute a^d % n
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def generate_large_prime(length):
    """Generate a prime number of the specified bit length."""
    p = generate_prime_candidate(length)
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p


def modular_inverse(e, phi):
    """Compute the modular multiplicative inverse of e modulo phi."""

    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x

    g, x, _ = egcd(e, phi)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi


def generate_keys(bit_length):
    """Generate RSA public and private keys."""
    p = generate_large_prime(bit_length // 2)
    q = generate_large_prime(bit_length // 2)
    while p == q:  # Ensure p and q are distinct
        q = generate_large_prime(bit_length // 2)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) == 1
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Compute the modular inverse of e
    d = modular_inverse(e, phi)

    return (e, n), (d, n)


def encrypt(public_key, plaintext):
    """Encrypt a plaintext message using the public key."""
    e, n = public_key
    plaintext_ints = [ord(char) for char in plaintext]
    ciphertext = [pow(m, e, n) for m in plaintext_ints]
    return ciphertext


def decrypt(private_key, ciphertext):
    """Decrypt a ciphertext message using the private key."""
    d, n = private_key
    plaintext_ints = [pow(c, d, n) for c in ciphertext]
    plaintext = "".join(chr(m) for m in plaintext_ints)
    return plaintext
