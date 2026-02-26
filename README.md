# RSA Cryptography Cipher
This Python script implements a basic RSA (Rivest–Shamir–Adleman) encryption and decryption tool. It allows users to generate keys using two prime numbers and a public exponent, then perform simple text-to-number substitutions and RSA transformations.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Features
- Key Generation: Calculates the modulus (n) and the private key (d) using the provided primes (p,q) and public exponent (e).

- Text Encryption: Converts text to a numeric format (1-26 for a-z, 32 for spaces) and encrypts each value using the RSA algorithm: c=m^e (mod n).

- Message Decryption: Reverses the process using the private key: m=c^d (mod n), and converts numbers back into a readable string.

- Interactive Menu: A simple command-line interface to toggle between encryption and decryption modes.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The script requires three command-line arguments to initialize the keys:

Prime 1 (p)
Prime 2 (q)
Public Key (e)

Example Execution:

'''
python main.py 3 11 7
'''
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Important Notes
[!WARNING]
This is an educational implementation. In this version, the private key d is found using a simple incrementing loop, which is inefficient for large numbers. Additionally, the character mapping is custom (a=1, b=2, etc.) rather than standard ASCII/UTF-8.
