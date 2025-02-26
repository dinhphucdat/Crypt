"""
Replace every o with 0, every e with 3, and every s with 5 ==> the language of hackers
"""

def SpeakOneThirtyThree(my_str):
    """
    Proceed the change inside
    """
    str_so_far = ""
    for index in range(len(my_str)):
        rep = my_str[index]
        if rep == "o" or rep == "O":
            str_so_far = str_so_far + "0"
        elif rep == "e" or rep == "E":
            str_so_far = str_so_far + "3"
        elif rep == "s" or rep == "S":
            str_so_far = str_so_far + "5"
        else:
            str_so_far = str_so_far + rep
    return str_so_far
