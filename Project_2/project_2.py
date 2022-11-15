from bakery import assert_equal

PRINTABLE_OFFSET = 32
PRINTABLES_LENGTH = 94
ROTATION_AMOUNT = 23
BASE = 31
HASH_SIZE = 1000000000


def encrypt_text(message: str, rotation_amount: int) -> str:
    '''
    This function takes in a message and a rotation amount and converts it
        into an encrypted message using a Ceaser Cypher.
    
    Args:
        message (str): The message to be encrypted.
    
    Return:
        str: The encrypted message
    '''
    
    # Places each character in the string into a list converted using ord().
    char_list = []
    for char in message:
        char_list.append(ord(char))
        if ord(char) < 48:
            char_list.append(126)
    
    # Using the helper function(char_rotation), iterates through the list and
    # 	rotates the character number leaving 126 alone.
    for index, char in enumerate(char_list):
        if char != 126:
            char_list[index] = char_rotation(char, rotation_amount)
    
    # Converts the ord() back to string chars using chr()
    for index, char in enumerate(char_list):
        char_list[index] = chr(char)
    
    # Returns the encrypted string
    encrypted_message = ""
    return encrypted_message.join(char_list)

    

def char_rotation(char: int, rotation_amount: int) -> int:
    '''
    This helper function takes in the character int and rotates is given the
        rotation amount, and returns that new int value
    
    Args:
        char (int): The character integer to be rotated.
        rotation_amount (int): The amount the character needs to be rotated.
    
    Return:
        int: The character integer after being rotated.
    '''
    return (char + rotation_amount - PRINTABLE_OFFSET) % PRINTABLES_LENGTH + PRINTABLE_OFFSET


def decrypt_text(message: str, rotation_amount: int) -> str:
    '''
    This function takes in a message and a rotation amount and converts it
        into an decrypted message using a Ceaser Cypher.
    
    Args:
        message (str): The message to be decrypted.
    
    Return:
        str: The decrypted message
    '''

    # Places each character in the string into a list converted using ord().
    char_list = []
    for char in message:
        char_list.append(ord(char))

    # Filters through the list and removes any char with value of 126
    filtered_list = []
    for char in char_list:
        if char != 126:
            filtered_list.append(char)
    char_list = filtered_list

    # Using the helper function(char_rotation), iterates through the list
    # 	and rotates the character number.
    for index, char in enumerate(char_list):
        char_list[index] = char_rotation(char, -rotation_amount)
    
    # Iterates through the finalized list and converts back to strings.
    for index, char in enumerate(char_list):
        char_list[index] = chr(char)

    # Returns the decrypted string
    decrypted_message = ""
    return decrypted_message.join(char_list)


# char_rotation unit tests
assert_equal(char_rotation(46, 1), 47)
assert_equal(char_rotation(46, 10), 56)
assert_equal(char_rotation(46, -10), 36)
assert_equal(char_rotation(46, 0), 46)

# encrypt_text unit tests
assert_equal(encrypt_text("hello", -55), "1.558")
assert_equal(encrypt_text("hello", 10), "rovvy")
assert_equal(encrypt_text("hello", 20), '|y""%')
assert_equal(encrypt_text("hello ", 20), '|y""%4~')

# decrypt_text unit tests
assert_equal(decrypt_text("1~558", 55), "X\\\\_")
assert_equal(decrypt_text("rovvy", -10), '|y""%')
assert_equal(decrypt_text("|y~~~", -20), "2/")
assert_equal(decrypt_text(';<=>?', 10), "12345")


def hash_text(message: str, base: int, hash_size: int) -> int:
    '''
    This function takes in a message, base, and hash_size value and creates a
        unique hash for it's message.
    
    Args:
        message (str): The inputed message
        base (int): An arbitrary integer
        hash_size (int): The integer used to lower the size of the hashed value
        
    Return:
        int: The unique hash value of the given text
    '''
    
    # Creates a new list with the ord values of each character in the string
    char_list = []
    for char in message:
        char_list.append(ord(char))
    
    # The hashing value using the given hash formula
    for index, char in enumerate(char_list):
        char_list[index] = (index + base) ** (char)
    
    # Summing the values of the hash
    list_sum = 0
    for char in char_list:
        list_sum += char
    
    # Using hash_size to lower the overall size of the hash
    hashed = list_sum % hash_size
    return hashed
    
    
assert_equal(hash_text('', BASE, HASH_SIZE), 0)
assert_equal(hash_text('This is a string', BASE, HASH_SIZE), 442938034)
assert_equal(hash_text('Hello World!', BASE, HASH_SIZE), 811478700)
assert_equal(hash_text('hello', BASE, HASH_SIZE), 586943565)


def main():
    '''
    This is the main function that checks for user input on whether to encrypt
        or decrypt a message.
    After checking what the user wants to do:
    encrypt: prints out the encrypted message and hash value
    decrypt: Asks for the encrypted message and decrypts it as long as the hash
        value is correct
    
    Args:
        None
    
    Return:
        None, prints needed values
    '''
    response = input("Would you like to encrypt or decrypt a message? ").lower()
    
    if response == "encrypt":
        message = input("Please input your message: ")
        encrypted_message = encrypt_text(message, ROTATION_AMOUNT)
        encrypted_hash = hash_text(message, BASE, HASH_SIZE)
        print(encrypted_message, encrypted_hash)
        pass
    
    elif response == "decrypt":
        message = input("Please input your encrypted message: ")
        message_hash = hash_text(decrypt_text(message, ROTATION_AMOUNT), BASE, HASH_SIZE)
        user_hash = int(input("Please input the hash value: "))
        if user_hash == message_hash:
            print("The message was: " + decrypt_text(message, ROTATION_AMOUNT))
            pass
        else:
            print("error, the input hash did not correct!")
            pass
    else:
        print("error, you did not choose a valid option")
        pass


main()
