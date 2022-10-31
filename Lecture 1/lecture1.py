from bakery import assert_equal
# do not delete the above line

def convert_hand(card: int) -> str:
    if card == 14:
        return "A"
    elif card == 13:
        return "K"
    elif card == 12:
        return "Q"
    elif card == 11:
        return "J"
    elif card == 10:
        return "X"
    else:
        return str(card)
    
def hand_to_string(hand: list[int]) -> str:
    x,y,z = hand[0],hand[1],hand[2]
    x_str = convert_hand(x)
    y_str = convert_hand(y)
    z_str = convert_hand(z)
    hand_str = x_str + y_str + z_str
    return hand_str

assert_equal(hand_to_string([1,2,3]), "123")
assert_equal(hand_to_string([14,13,12]), "AKQ")
assert_equal(hand_to_string([11,10,9]), "JX9")