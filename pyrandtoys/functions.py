import random as rop
from typing import Tuple


def dice(count: int = 1) -> Tuple[int, ...]:
    """
    Rolls N dices and returns the values as a tuple

    Parameters:
    count (int) : The number of dices to roll

    Returns:
    tuple: The values of dice rolls
    The tuple values is a number between 1 and 6
   """

    res = ()

    for _ in range(int(count)):
        res += (rop.randint(1, 6),)

    return res


def coin(count: int = 1) -> Tuple[str, ...]:
    """
    Rolls N coins and returns the values as a tuple

    Parameters:
    count (int) : The number of coins to roll

    Returns:
    tuple: The values of coin rolls
    tuple can be HEADS or TAILS
   """

    res = ()
    sample_space = ["HEADS", "TAILS"]

    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def dreidel(count: int = 1) -> Tuple[str, ...]:
    """
    Spin a dreidel N times and return the values as a tuple

    Parameters:
    count (int) : The number times to spin

    Returns:
    tuple: The values of dreidel spins
    Tuple contains one of the values between ["NUN", "GIMEL", "HE", "SHIN"]
   """

    res = ()
    sample_space = ["NUN", "GIMEL", "HE", "SHIN"]

    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def cat(count: int = 1) -> Tuple[str, ...]:
    """
    Ask if the cat is alive or dead

    Parameters:
    count (int) : The number of times to ask

    Returns:
    tuple: The dead or alive values of the cats
    Cat can be ALIVE or DEAD
   """
    res = ()
    sample_space = ["ALIVE", "DEAD"]

    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def switch(count: int = 1) -> Tuple[str, ...]:
    """
    Flip a switch N times and return the values as a tuple

    Parameters:
    count (int) : The number times to spin

    Returns:
    tuple: The values of dreidel spins
    Switch can be ON or OFF
   """
    res = ()
    sample_space = ["ON", "OFF"]

    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def spinner(lower: int, upper: int = 0) -> int:
    """
    Spin a spinner between a lower and upper value

    Parameters:
    lower (int) : The lower value of the spinner
    upper (int) : The upper value of the spinner

    Returns:
    int: The value of the spinner
    int is a number between lower and upper
    """
    if lower > upper:
        lower, upper = upper, lower

    return rop.randint(int(lower), int(upper))


def combi(list: list = []) -> Tuple[str, ...]:
    """
    Randomise combinations between other functions

    Parameters:
    list (list) : The list of functions to randomise

    Returns:
    tuple: The values of the randomised functions
    """
    res = ()
    
    if isinstance(list, list):
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

        else:
            res += (None,)

    return res
