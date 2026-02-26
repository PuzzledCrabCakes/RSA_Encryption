import sys

def main():
    prime_1 = int(sys.argv[1])
    prime_2 = int(sys.argv[2])
    public_key = int(sys.argv[3])
    n, e, d = RSA_cryptography(prime_1, prime_2, public_key)
    
    menu(n, e, d)


def menu(n: int, e: int, d: int) -> None:
    '''
    Simple menu function that displays options upon start up.

    Parameters:
    - n (int): product of primes
    - e (int): public key
    - d (int): private key
    '''
    user_input = ""
    while True:
        print("Welcome to the RSA cryptography cipher!")
        print("Would you like to encrypt or decrypt?")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit\n")
        user_input = input()
        if user_input == "1":
            encryption(n, e)
        elif user_input == "2":
            decryption(d, n)
        elif user_input == "3":
            break
        else:
            raise ValueError("Invalid option, please choose 1, 2, or 3.")

def RSA_cryptography(p: int, q: int, e: int) -> tuple[int, int, int]:
    '''
    Simple function to calculate the necessary information to perform the other functions.

    Parameters:
    - p (int): Prime number 1
    - q (int): Prime number 2
    - e (int): public key

    Returns:
    tuple[n, e, d]: Returns the product of primes, the public key, and the private key.
    '''
    n = p*q
    phi = (p-1)*(q-1)
    d = 0
    while True:
        d += 1
        if (e*d) % phi == 1:
            break
    
    return n, e, d

def encryption(n: int, e: int) -> list[int]:
    '''
    An encryption function that requests a string input and outputs a list of numbers corresponding to an encryption mapping.

    Parameters:
    - n (int): product of primes
    - e (int): public key

    Returns:
    - list[int]: returns a list of integers that corresponds to each ASCII character of the string - 96.
    '''
    string = (input("What is your phrase: "))
    ls = list(string.lower())
    for i, char in enumerate(ls):
        if char == " ":
            ls[i] = "32"
        else:
            if ord(char)-96 <= 9:
                ls[i] = str(ord(char)-96)
            else:
                ls[i] = str(ord(char)-96)
    num_list = list(map(int, ls))
    print("Letter to number -->:", end=" ")
    print(*num_list)
    numbers = []
    for i, v in enumerate(num_list):
        numbers.append(pow(v, e, n))
    
    print("Encrypted RSA Code:", end=" ")
    print(*numbers)
    print("")
    print("-------------------------------------------------------------------------------------------------")
    return numbers


def decryption(d: int, n: int) -> str:
    '''
    A decoding function that requests a list of of numbers and outputs a string corresponding to a decryption mapping.

    Parameters:
    - d (int): private key
    - n (int): product of primes

    Returns:
    - str: returns a decoded string that corresponds to a list of integers following the ASCII character + 96.
    '''
    num = input("What is your encyrpted phrase: ").strip()
    temp = num.split()

    tokens = list(map(int, temp))

    decrp = []
    for i, c in enumerate(tokens):
        decrp.append(pow(c, d, n))
    
    out = []
    for tok in decrp:
        code = int(tok)
        if code == 32:
            out.append(' ')
        elif 1 <= code <= 26:
            out.append(chr(code + 96))
        else:
            raise ValueError(f"Unexpected code: {code} (expected 1-26 or 32 for space)")
    
    string = "".join(out)
    print("Decoded message:", end=" ")
    print(string)
    print("")
    print("-------------------------------------------------------------------------------------------------")
    return string
    
if __name__ == "__main__":
    main()
    


