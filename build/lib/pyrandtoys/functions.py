import random as rop
from typing import Tuple
from typing import Union


def dice(count: int = 1) -> Tuple[int, ...]:
    """
    Rolls N dice

    Parameters:
    count (int) : The number of dice to roll, default = 1

    Returns:
    tuple: The result of dice rolls.
    Each tuple element is a number between 1 and 6.
    """

    res = ()

    for _ in range(int(count)):
        res += (rop.randint(1, 6),)

    return res


def coin(count: int = 1) -> Tuple[str, ...]:
    """
    Toss N coins

    Parameters:
    count (int) : The number of coins to toss, default = 1

    Returns:
    tuple: The result of coin toss.
    A tuple element can be either HEADS or TAILS.
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
    tuple: The values of dreidel spins.
    Each tuple element is one of these values: NUN, GIMEL, HE, SHIN.
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
    tuple: The status of cats.
    A cat can be either ALIVE or DEAD.
    """
    res = ()
    sample_space = ["ALIVE", "DEAD"]

    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def switch(count: int = 1) -> Tuple[str, ...]:
    """
    Toggle a switch N times

    Parameters:
    count (int) : The number times to toggle a switch, default = 1

    Returns:
    tuple: The state of switches.
    A switch can be either ON or OFF.
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
    lower (int) : lowest number on the spinner.
    upper (int) : highest number on the spinner.

    Returns:
    int: The value at which the spinner has stopped spinning.

    Result is a number between lower and upper.
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
    tuple: The cards that have been picked.
    Each tuple element is a card from a deck of 52 cards.
    """

    SUITS = ("Spades", "Clubs", "Hearts", "Diamonds")
    RANKS = (
        "Ace",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Jack",
        "Queen",
        "King",
    )

    sample_space = [rank + " of " + suit for rank in RANKS for suit in SUITS]

    res = ()
    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def combi(*argv: Union[str, int, list, tuple]) -> Tuple[Union[int, str], ...]:
    """
    Randomise combinations between other functions

    Parameters:
    Functions to randomise

    Returns:
    tuple: The values of the randomised functions
    """

    res = []

    for item in argv:
        if isinstance(item, str):
            item = item.lower()
            try:
                res.append(eval(item + "()")[0])
            except:
                res.append(None)

        elif isinstance(item, list) or isinstance(item, tuple):
            temp = ()
            for i in item:

                if isinstance(i, str):
                    i = i.lower()
                    try:
                        temp += (eval(i + "()")[0],)
                    except:
                        temp += (None,)

                elif isinstance(i, int):
                    sample_space = ["coin", "dice", "switch", "card"]
                    temp2 = ()

                    for _ in range(i):
                        rand_op = rop.choice(sample_space)
                        try:
                            temp2 += (eval(rand_op + "()")[0],)
                        except:
                            temp2 += (None,)

                    temp += (temp2,)

                else:
                    temp += (None,)

            res.append(temp)

        elif isinstance(item, int):

            sample_space = ["coin", "dice", "switch", "card"]
            temp = ()

            for _ in range(item):
                rand_op = rop.choice(sample_space)
                try:
                    temp += (eval(rand_op + "()")[0],)
                except:
                    temp += (None,)

            res.append(temp)

    res = tuple(res)

    if len(res) == 1 and isinstance(res[0], tuple):
        return res[0]
    else:
        return res
