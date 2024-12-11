from rsa import generate_keys, encrypt, decrypt


def main():
    bit_length = 1024
    public_key, private_key = generate_keys(bit_length)
    message = "Hello, RSA!"

    print("Public Key:", public_key)
    print("-" * 20)
    print("Private Key:", private_key)
    print("-" * 20)
    
    ciphertext = encrypt(public_key, message)
    print("Ciphertext:", ciphertext)
    print("-" * 20)

    decrypted_message = decrypt(private_key, ciphertext)
    print("Decrypted Message:", decrypted_message)

if __name__ == "__main__":
    main()
