# DES implementation
import pyDes

# Define fixed key and plaintext
fixed_key = b'abcdefgh'  # 8-byte key
fixed_plaintext = b'12345678'  # 8-byte plaintext

# Function to perform DES encryption with fixed key
def des_encrypt(plaintext, key):
    k = pyDes.des(key, pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)
    ciphertext = k.encrypt(plaintext)
    return ciphertext

# Function to calculate the avalanche effect
def avalanche_effect(plaintext, altered_bit_position):
    original_ciphertext = des_encrypt(plaintext, fixed_key)
    
    # Alter the bit at the specified position
    altered_plaintext = bytearray(plaintext)
    altered_plaintext[altered_bit_position // 8] ^= (1 << (altered_bit_position % 8))
    
    # Encrypt the altered plaintext
    altered_ciphertext = des_encrypt(bytes(altered_plaintext), fixed_key)
    
    # Calculate the number of differing bits
    difference = 0
    for i in range(len(original_ciphertext)):
        difference += bin(original_ciphertext[i] ^ altered_ciphertext[i]).count('1')
    
    return difference

# Function to print output of each round
def print_output(round_number, plaintext, ciphertext):
    print(f"Round {round_number}:")
    print(f"Plaintext: {plaintext.hex()}")
    print(f"Ciphertext: {ciphertext.hex()}\n")

# Function to perform DES encryption for multiple rounds
def des_encrypt_rounds(plaintext, key, rounds=16):
    k = pyDes.des(key, pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)
    ciphertext = plaintext
    for i in range(rounds):
        ciphertext = k.encrypt(ciphertext)
        print_output(i+1, plaintext, ciphertext)
    return ciphertext

# Main function to demonstrate DES, 2-DES, and 3-DES
if __name__ == "__main__":
    print("=== DES Encryption ===")
    des_encrypt_rounds(fixed_plaintext, fixed_key)

    print("=== 2-DES Encryption ===")
    double_encrypted_plaintext = des_encrypt(fixed_plaintext, fixed_key)
    des_encrypt_rounds(double_encrypted_plaintext, fixed_key)

    print("=== 3-DES Encryption ===")
    triple_encrypted_plaintext = des_encrypt(double_encrypted_plaintext, fixed_key)
    des_encrypt_rounds(triple_encrypted_plaintext, fixed_key)

    # Calculate and compare avalanche effects
    print("\n=== Avalanche Effect Analysis ===")
    altered_bit_positions = [1, 8, 16, 24, 31, 38, 45, 53]
    for pos in altered_bit_positions:
        print(f"Altered Bit Position: {pos}")
        print("DES Avalanche Effect:", avalanche_effect(fixed_plaintext, pos))
        print("2-DES Avalanche Effect:", avalanche_effect(double_encrypted_plaintext, pos))
        print("3-DES Avalanche Effect:", avalanche_effect(triple_encrypted_plaintext, pos))
        print()
