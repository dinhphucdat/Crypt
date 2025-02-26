from . import caesar
from . import substitution
from . import speak133t

def caesarClient(is_encode, key : int, message : str):
    """
    encode/decode using caesar cipher
    """
    if (is_encode):
        output = caesar.encryptC(message, key)
        print(f"Your encoded message with Caesar Cipher: {output:s}")
    else:
        output = caesar.decryptC(message, key)
        print(f"Your decoded message with Caesar Cipher: {output:s}")

def substitutionClient(is_encode, key : str, message : str):
    """
    encode/decode using substitution cipher
    """
    if (is_encode):
        output = substitution.substitutionEnc(message, key)
        print(f"Your encoded message with substitution cipher: {output:s}")
    else:
        output = substitution.substitutionDec(message, key)
        print(f"Your decoded message with substitution cipher: {output:s}")

def speakToThreeClient(message):
    """
    encode with speak to 3
    """
    print(f"Your Sp3akToThr33 message: {speak133t.SpeakOneThirtyThree(message):s}")
