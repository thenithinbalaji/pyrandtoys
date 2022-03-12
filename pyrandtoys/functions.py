import random as rop
from typing import Tuple


def dice(count: int = 1) -> Tuple[int, ...]:
    """
    Rolls N dice

    Parameters:
    count (int) : The number of dice to roll, default = 1

    Returns:
    tuple: The values of dice rolls
    Each tuple element is a number between 1 and 6
   """

    res = ()

    for _ in range(int(count)):
        res += (rop.randint(1, 6),)

    return res


def coin(count: int = 1) -> Tuple[str, ...]:
    """
    Flips N coins

    Parameters:
    count (int) : The number of coins to roll, default = 1

    Returns:
    tuple: The values of coin rolls
    A tuple element can be either HEADS or TAILS
   """

    res = ()
    sample_space = ["HEADS", "TAILS"]

    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def dreidel(count: int = 1) -> Tuple[str, ...]:
    """
    Spin a dreidel N times

    Parameters:
    count (int) : The number times to spin, default = 1

    Returns:
    tuple: The values of dreidel spins
    A tuple element is one of these values: NUN, GIMEL, HE, SHIN
   """

    res = ()
    sample_space = ["NUN", "GIMEL", "HE", "SHIN"]

    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def cat(count: int = 1) -> Tuple[str, ...]:
    """
    Perform Schrödinger's cat experiment N times

    Parameters:
    count (int) : The number of times to perform the experiment, default = 1

    Returns:
    tuple: The status of cats
    A Cat can be ALIVE or DEAD
   """
    res = ()
    sample_space = ["ALIVE", "DEAD"]

    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def switch(count: int = 1) -> Tuple[str, ...]:
    """
    Toggles a switch N times

    Parameters:
    count (int) : The number times to flip a switch, default = 1

    Returns:
    tuple: The status of switches
    A Switch can be either ON or OFF
   """
    res = ()
    sample_space = ["ON", "OFF"]

    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def spinner(lower: int, upper: int = 0) -> int:
    """
    Spin a spinner with numbers from lower to upper value

    Parameters:
    lower (int) : lowest number on the spinner
    upper (int) : highest number on the spinner

    Returns:
    int: The value at which the spinner has stopped spinning
    int is a number between lower and upper
    """
    if lower > upper:
        lower, upper = upper, lower

    return rop.randint(int(lower), int(upper))


def card(count: int = 1) -> Tuple[str, ...]:
    """
    Picks N cards from a deck of 52 cards

    Parameters:
    count (int) : The number of cards to pick, default = 1

    Returns:
    tuple: The cards that have been picked
    Each tuple element is a card from a deck of 52 cards.
   """

    SUITS = ("Spades", "Clubs", "Hearts", "Diamonds")
    RANKS = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")

    sample_space = [rank + " of " + suit for rank in RANKS for suit in SUITS]

    res = ()
    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def combi(list: list = []) -> Tuple[str, ...]:
    """
    Randomise combinations between other functions

    Parameters:
    list (list) : The list of functions to randomise

    Returns:
    tuple: The values of the randomised functions
    """
    res = ()
    
    if isinstance(list, str):
        temp = []
        temp.append(list)
        list = temp

    elif isinstance(list, int):
        temp = []
        sample_space = ["coin", "dice", "switch"]

        for _ in range(list):
            rand_op = rop.choice(sample_space)
            temp.append(rand_op)

        list = temp

    for obj in list:
        obj = obj.lower()

        if obj == "coin":
            res += coin()

        elif obj == "dice":
            res += dice()

        elif obj == "dreidel":
            res += dreidel()

        elif obj == "cat":
            res += cat()

        elif obj == "switch":
            res += switch()
        
        elif obj == "card":
            res += card()

        else:
            res += (None,)

    return res
