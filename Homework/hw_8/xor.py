"""
CS 211 - Sabrina Zhang
HW 8 - XOR Encryption  
References : https://www.delftstack.com/howto/python/perform-xor-of-strings-in-python/
"""

def xor_encrypt(plaintext, key):
    idx = 0
    encrypted = ""
    for ch in plaintext:
        if idx > (len(key) - 1):
            idx = 0 # if the index is the end of the key reset index
        encrypted = encrypted + chr(ord(ch) ^ ord(key[idx]))
        idx += 1
    return encrypted
    
if __name__ == "__main__":
    plaintext = "This is a secret message!"
    print("Plaintext:")
    print(plaintext)
    key = "beautifulIsBetterThanUgly" # Python's Zen
    ciphertext = xor_encrypt(plaintext, key)
    print("Ciphertext:")
    print(ciphertext)
    decrypted_text = xor_encrypt(ciphertext, key)
    print("Decrypted text:")
    print(decrypted_text)

    if plaintext == decrypted_text:
        print("Encryption and decryption successful!")
    else:
        print("Error: Decryption failed!")