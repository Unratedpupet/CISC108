from bakery import assert_equal

# do not delete the above line


def convert_hand(card: int) -> str:
    """
    This function converts a single integer into a card based string.

    Args:
        card (int): The integer value of the standard deck of cards.
    Returns:
        str: The string value associated with the integer value.
    """
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
    """
    This function converts the incoming list of integers into a string that is readible by the player.

    Args:
        hand (list): A three length list of integers that correspond with a standard playing card deck.
    Returns:
        str: The string value of the hand that is easily readible by the player.
    """
    # Gives each card it's own variable so that it can be passed into the convert_hand function.
    card_1, card_2, card_3 = hand[0], hand[1], hand[2]

    card_1_str = convert_hand(card_1)
    card_2_str = convert_hand(card_2)
    card_3_str = convert_hand(card_3)
    # Returns the string form of the hand.
    return card_1_str + " " + card_2_str + " " + card_3_str


assert_equal(hand_to_string([1, 2, 3]), "1 2 3")
assert_equal(hand_to_string([14, 13, 12]), "A K Q")
assert_equal(hand_to_string([11, 10, 9]), "J X 9")


def sort_hand(hand: list[int]) -> list[int]:
    """
    This function takes in a list of ints and sorts them in decending order.

    Args:
        hand (List[int]): Takes in a list of integers in any order

    Returns:
        list[int]: Returns a sorted list of integers.
    """
    # Initializes an empty list to sort into.
    sorted_hand = []

    # Checks to get the maximum value in the list, adds the maximum to the sorted_hand,
    # 	and removes that index from the original list.
    if hand[0] >= hand[1] and hand[0] >= hand[2]:
        sorted_hand.append(hand[0])
        hand.pop(0)
    elif hand[0] <= hand[1] and hand[1] >= hand[2]:
        sorted_hand.append(hand[1])
        hand.pop(1)
    else:
        sorted_hand.append(hand[2])
        hand.pop(2)

    # Second conditional check to get the next maximum integer,
    #    and adds the remaining two to the sorted_hand list.
    if hand[0] >= hand[1]:
        sorted_hand.append(hand[0])
        sorted_hand.append(hand[1])
    else:
        sorted_hand.append(hand[1])
        sorted_hand.append(hand[0])

    return sorted_hand


assert_equal(sort_hand([1, 2, 3]), [3, 2, 1])
assert_equal(sort_hand([14, 1, 10]), [14, 10, 1])
assert_equal(sort_hand([3, 2, 1]), [3, 2, 1])


def has_triple(hand: list[int]) -> bool:
    """
    This function checks to see if all three integers in the hand equal each other to make a triple.

    Args:
        hand (list[int]): Takes in a list of integers that are the hand.

    Return:
        bool: Returns True if all three 'cards' match. Returns False if they do not all match.

    """

    if hand[0] == hand[1] and hand[0] == hand[2]:
        return True
    else:
        return False


assert_equal(has_triple([1, 1, 1]), True)
assert_equal(has_triple([1, 1, 2]), False)
assert_equal(has_triple([1, 2, 1]), False)


def has_straight(hand: list[int]) -> bool:
    """
    This function checks to make sure the hand has direct consecutive descending order
        and returns a bool value.

    Args:
        hand (list[int]): The sorted hand in imported as a list of integers.

    Return:
        bool: Returns True if the hand is in direct, consecutive descending order.
            Returns False if not the case.

    """

    # Checks to see if card 2 is one less than card 1 AND card 3 is one less than card 2.
    if hand[1] == hand[0] - 1 and hand[2] == hand[1] - 1:
        return True
    else:
        return False


assert_equal(has_straight([10, 9, 8]), True)
assert_equal(has_straight([10, 8, 7]), False)
assert_equal(has_straight([10, 9, 6]), False)


def has_pair(hand: list[int]) -> bool:
    """
    This function checks to see if two integers in the hand equal each other to make a pair.

    Args:
        hand (list[int]): Takes in a list of integers that are the hand.

    Return:
        bool: Returns True if two 'cards' match. Returns False if they none of the cards match.

    """

    if hand[0] == hand[1] or hand[1] == hand[2]:
        return True
    else:
        return False


assert_equal(has_pair([2, 2, 1]), True)
assert_equal(has_pair([2, 1, 1]), True)
assert_equal(has_pair([3, 2, 1]), False)


def score_hand(hand: list[int]) -> int:
    """
    This function scores the hand using the noted parameters

    Args:
        hand: (list[int]): The sorted hand.

    Return:
        int: Checks to see if the hand has any 'features', if so, it scores accordingly.
            If it has no 'features' it returns the base 16 values.
    """

    if has_triple(hand):
        return (16 * 16**3) + (hand[0] * 16**2) + (hand[1] * 16) + hand[2]
    elif has_straight(hand):
        return (15 * 16**3) + (hand[0] * 16**2) + (hand[1] * 16) + hand[2]
    elif has_pair(hand):
        if hand[0] == hand[1]:
            return (hand[0] * 16**3) + (hand[0] * 16**2) + (hand[1] * 16) + hand[2]
        else:
            return (hand[1] * 16**3) + (hand[0] * 16**2) + (hand[1] * 16) + hand[2]
    else:
        return (hand[0] * 16**2) + (hand[1] * 16) + hand[2]


assert_equal(score_hand([7, 7, 7]), 67447)
assert_equal(score_hand([7, 6, 5]), 63333)
assert_equal(score_hand([7, 7, 6]), 30582)
assert_equal(score_hand([7, 6, 6]), 26470)
assert_equal(score_hand([8, 6, 5]), 2149)


def dealer_plays(hand: list[int]) -> bool:
    """
    This functions scores the dealer's hand using the score_hand function. It then checks to
        see if the score is greater than the minimum score needed to have a Jack high with no features.

    Args:
        hand (list[int]): The dealer's hand

    Return:
        bool: If the dealer's hand is over the highest score without having a queen,
            it returns True, otherwise, it returns False.

    """

    # 2984 is the score value of a J, X, 8 hand, which is the highest possible
    #    without either queen high or a feature.
    return score_hand(hand) > 2984


assert_equal(dealer_plays([1, 1, 1]), True)
assert_equal(dealer_plays([14, 1, 1]), True)
assert_equal(dealer_plays([13, 1, 1]), True)
assert_equal(dealer_plays([12, 1, 1]), True)
assert_equal(dealer_plays([4, 3, 1]), False)


def play_round() -> int:
    """
    This function is the main play and scoring function.

    Args:
        There are no arguments to this function.

    Return:
        int: This function returns the player score after each round.
    """
    # Gets the player's hand
    player_hand = deal()
    player_hand = sort_hand(player_hand)
    print(f"Player hand is {hand_to_string(player_hand)}")

    # Player chooses to play or not. If "p" is entered, the play continues.
    if get_choice() == "p":
        # Gets the dealer's hand
        dealer_hand = deal()
        dealer_hand = sort_hand(dealer_hand)
        print(f"Dealer's hand is {hand_to_string(dealer_hand)}")

        # Checks to see if the dealer plays, if it does, compare's scores to see who wins.
        if dealer_plays(dealer_hand) == False:
            return 10
        else:
            if score_hand(player_hand) > score_hand(dealer_hand):
                return 20
            else:
                return -20
    else:
        return -10


# Everything below was pre-defined through BlockPy
def get_choice() -> str:
    """
    Get user input and return either 'p' or 'f' depending on the player's choice.
    """
    answer = " "
    while answer not in "pf":
        answer = input("Please enter either 'p' or 'f':")
    return answer


from random import randint


def deal() -> list[int]:
    """
    Simple random card dealing function that returns three randomly chosen cards,
    represented as integers between 2 and 14.
    """
    return [randint(2, 14), randint(2, 14), randint(2, 14)]


score = 0
while True:
    score += play_round()
    print("Your score is", score, "- Starting a new round!")
