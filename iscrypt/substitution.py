"""
substitution cipher
"""
def convertNum(input_chr):
    """
    convert strings into numbers (a -> 0, b -> 1,..., z -> 25)
    """
    asci_val = 0
    if ord(input_chr) >= 97 and ord(input_chr) <= 122:
        asci_val = ord(input_chr) - 97
    elif ord(input_chr) >= 65 and ord(input_chr) <= 90:
        asci_val = ord(input_chr) - 65
    return asci_val

def convertLet(input_num):
    """
    convert numbers into strings (0 -> a, 1 -> b,..., 25 -> z)
    """
    return chr(input_num + 97)

def substitutionEnc(message, key):
    """
    encrypts
    """
    encrypt_so_far = ""
    for i in range(len(message)):
        encrypt_num = convertNum(message[i])
        encrypt_chr = key[encrypt_num]
        encrypt_so_far = encrypt_so_far + encrypt_chr
    return encrypt_so_far

# print(substitutionEnc("abc", "tzwanfghqrsbcduiopvejklxym"))

def substitutionDec(encryption, key):
    """
    decrypts
    """
    message = ""
    for i in range(len(encryption)):
        decrypt_num = key.find(encryption[i])
        decrypt_chr = convertLet(decrypt_num)
        message = message + decrypt_chr
    return message

# print(substitutionDec("tzw", "tzwanfghqrsbcduiopvejklxym"))
