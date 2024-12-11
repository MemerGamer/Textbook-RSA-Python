# Textbook RSA Implementation in Python

This project implements a basic version of the RSA algorithm, a foundational public-key cryptosystem, in Python. The implementation uses only built-in Python modules and commands for simplicity and educational purposes.

## Features

- **Key Generation**: Generate public and private keys based on user-defined bit lengths.
- **Encryption**: Encrypt plaintext messages using the public key.
- **Decryption**: Decrypt ciphertext messages using the private key.
- **Prime Number Generation**: Use the Miller-Rabin primality test to ensure secure key generation.

## Files

- `rsa.py`: Contains the implementation of the RSA algorithm, including functions for key generation, encryption, and decryption.
- `main.py`: Demonstrates the usage of the RSA algorithm by generating keys, encrypting a message, and decrypting it.

## Prerequisites

- Python 3.x

## Example Usage

To see the RSA algorithm in action, run the `main.py` script:

```bash
python main.py
```

### Example Output

```text
Public Key: (e, n)
--------------------
Private Key: (d, n)
--------------------
Ciphertext: [...]
--------------------
Decrypted Message: Hello, RSA!
```

## How It Works

1. **Key Generation**: The `generate_keys` function generates a pair of keys. Large prime numbers are chosen, and their product determines the modulus (`n`). The public exponent (`e`) and private exponent (`d`) are computed such that they satisfy the modular arithmetic constraints of the RSA algorithm.

2. **Encryption**: The `encrypt` function converts the plaintext message into a list of integers (Unicode code points) and applies modular exponentiation using the public key.

3. **Decryption**: The `decrypt` function reverses the encryption process using the private key to recover the original message.

## Educational Note

This implementation follows the textbook RSA algorithm for simplicity. It is not secure for production use as it does not include padding mechanisms such as OAEP (Optimal Asymmetric Encryption Padding), which are critical for modern RSA security.

For any questions or contributions, feel free to submit a pull request or raise an issue in the repository.
