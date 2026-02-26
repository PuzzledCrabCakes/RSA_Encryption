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

```
python main.py 3 11 7
```

Eample Output:

```
Welcome to the RSA cryptography cipher!
Would you like to encrypt or decrypt?
1. Encrypt
2. Decrypt
3. Quit

1
What is your phrase: I Like RSA
Letter to number -->: 9 32 12 9 11 5 32 18 19 1
Encrypted RSA Code: 15 32 12 15 11 14 32 6 13 1

-------------------------------------------------------------------------------------------------
Welcome to the RSA cryptography cipher!
Would you like to encrypt or decrypt?
1. Encrypt
2. Decrypt
3. Quit

2
What is your encyrpted phrase: 15 32 12 15 11 14 32 6 13 1
Decoded message: i like rsa

-------------------------------------------------------------------------------------------------
```
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Important Notes
Warning:
This is an educational implementation. In this version, the private key d is found using a simple incrementing loop, which is inefficient for large numbers. Additionally, the character mapping is custom (a=1, b=2, etc.) rather than standard ASCII/UTF-8.
