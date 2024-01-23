import math

class RSAKeys:
    def __init__(self):
        self.publicKeyRsa = 0
        self.privateKeyRSA = 0
        self.modulus = 0

def find_gcd(a, b):
    if b == 0:
        return a
    return find_gcd(b, a % b)

def calculate_inverse(num1, num2):
    m0 = num2
    y = 0
    x = 1

    if num2 == 1:
        return 0

    while num1 > 1:
        q = num1 // num2
        t = num2

        num2 = num1 % num2
        num1 = t
        t = y

        y = x - q * y
        x = t

    if x < 0:
        x += m0

    return x

def check_if_prime(num):
    if num == 0 or num == 1:
        print("Number is not prime")
        return False

    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            print("Number is not prime")
            return False

    print("Number is prime")
    return True

def generate_keys(prime1, prime2):
    keys = RSAKeys()
    totient = (prime1 - 1) * (prime2 - 1)
    keys.modulus = prime1 * prime2
    keys.publicKeyRsa = 2

    while True:
        if find_gcd(keys.publicKeyRsa, totient) == 1:
            break
        keys.publicKeyRsa += 1

    keys.privateKeyRSA = calculate_inverse(keys.publicKeyRsa, totient)

    return keys

def encrypt(message, keys):
    e = keys.publicKeyRsa
    encrypted_text = 1

    while e > 0:
        encrypted_text = (encrypted_text * message) % keys.modulus
        e -= 1

    return encrypted_text

def decrypt(encrypted_text, keys):
    d = keys.privateKeyRSA
    decrypted = 1

    while d > 0:
        decrypted = (decrypted * encrypted_text) % keys.modulus
        d -= 1

    return decrypted

def encoder(message, keys):
    encoded = []

    for char in message:
        encoded.append(encrypt(ord(char), keys))

    return encoded

def decoder(encoded, keys):
    decoded = ''

    for num in encoded:
        decoded += chr(decrypt(num, keys))

    return decoded

if __name__ == '__main__':
    keys = RSAKeys()

    prime1 = int(input("Enter the first prime number: "))
    prime2 = int(input("Enter the second prime number: "))

    keys = generate_keys(prime1, prime2)

    print("The public key is:", keys.publicKeyRsa)
    print("The private key is:", keys.privateKeyRSA)
    print("The modulus is:", keys.modulus)

    message = input("Enter the message to encrypt: ")
    encoded = encoder(message, keys)

    print("Initial message:")
    print(message)
    print()

    print("The encoded message (encrypted by public key):")
    print(encoded)
    print()

    decoded = decoder(encoded, keys)

    print("The decoded message (decrypted by public key):")
    print(decoded)
