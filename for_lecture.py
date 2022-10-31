alpha = [4, 2, 1, 5, 8, 9, 2]
beta = 8

def find_first_odd(numbers: list[int]) -> int:
    """
    Returns the last integer in the list that is an odd number.
    """
    for number in numbers:
        # The number is odd if its remainder is 1 after dividing by 2
        if number % 2 == 1:
            return number
    return -1

def find_last_even(nums: list[int]) -> int:
    """
    Returns the last integer in the list that is an even number.
    """
    result = -1
    for num in nums:
        if num % 2 == 0:
            result = num
    return result

def double(values: list[int]) -> list[int]:
    """
    Returns all the integers in the list multiplied by two.
    """
    new_values = []
    for value in values:
        new_values.append(value*2)
    return new_values

def remove_after_high(items: list[int]) -> list[int]:
    """
    Go through a list and find the first element greater than
    some threshold `beta`. Then, return a new list without that
    element or any element that comes after it.
    """
    taken = []
    taking = True
    for item in items:
        if item > beta:
            taking= False
        elif taking:
            taken.append(item)
    return taken

def do_everything(integers: list[int]) -> bool:
    first_odd = find_first_odd(integers)
    integers = double(integers)
    integers = remove_after_high(integers)
    last_even = find_last_even(integers)
    return first_odd > last_even

print(do_everything(alpha))