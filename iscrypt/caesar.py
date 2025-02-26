def encryptC(input_string, shift):
    str_so_far = ""
    for i in range(len(input_string)):
        if ord(input_string[i]) >= 32 and ord(input_string[i]) <= 40:
            str_so_far += input_string[i]
        elif ord(input_string[i]) >= 91 and ord(input_string[i]) <= 96:
            str_so_far += input_string[i]
        elif ord(input_string[i]) >= 123 and ord(input_string[i]) <= 127:
            str_so_far += input_string[i]
        elif ord(input_string[i]) >= 65 and ord(input_string[i]) <= 90:
            current_num = convertNum(input_string[i])
            current_num = (current_num + shift)%26
            encrypt_chr = convertLet(current_num)
            encrypt_chr = encrypt_chr.upper()
            str_so_far = str_so_far + encrypt_chr
        else:
            current_num = convertNum(input_string[i])
            current_num = (current_num + shift)%26
            encrypt_chr = convertLet(current_num)
            str_so_far = str_so_far + encrypt_chr
    return str_so_far

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

def decryptC(input_string, shift):
    return encryptC(input_string, 26 - shift)

"""
def main():
    print(convertNum("a"))
    print(convertNum("z"))
    print(convertLet(4))
    print(encryptC('Friday!', 2))
    print(decryptC("Htkfca", 2))
"""
