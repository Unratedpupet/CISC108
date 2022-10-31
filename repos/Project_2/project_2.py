from bakery import assert_equal

PRINTABLE_OFFSET = 32
PRINTABLES_LENGTH = 94


def encrypt_text(message: str, rotation_amount: int) -> str:
    '''
    This function takes in a message and a rotation amount and converts it into an encrypted message using a Ceaser Cypher.
    
    Args:
        message (str): The message to be encrypted.
    
    Return:
        str: The encrypted message
    '''
    
    # Places each character in the string into a list converted using ord().
    char_list = []
    for char in message:
        char_list.append(ord(char))
    
    # Using the helper function(char_rotation), iterates through the list and rotates the character number.
    # If the character is less than 48, it is replaced by the "~"
    for index, char in enumerate(char_list):
        if char_rotation(char, rotation_amount) < 48:
            char_list[index] = 126
        else:
            char_list[index] = char_rotation(char, rotation_amount)
    
    # Converts the ord() back to string chars using chr()
    for index, char in enumerate(char_list):
        char_list[index] = chr(char)
    
    # Returns the encrypted string
    encrypted_message = ""
    return encrypted_message.join(char_list)

    

def char_rotation(char: int, rotation_amount: int) -> int:
    '''
    This helper function takes in the character int and rotates is given the rotation amount, and returns that new int value
    
    Args:
        char (int): The character integer to be rotated.
        rotation_amount (int): The amount the character needs to be rotated.
    
    Return:
        int: The character integer after being rotated.
    '''
    return (char + rotation_amount - PRINTABLE_OFFSET) % PRINTABLES_LENGTH + PRINTABLE_OFFSET






#assert_equal(char_rotation(46, 1), 47) 

print(encrypt_text("hello", -55))