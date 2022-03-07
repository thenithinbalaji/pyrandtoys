import random as rop


def dice(count=1):
    res = ()

    for _ in range(int(count)):
        res += (rop.randint(1, 6),)

    return res


def coin(count=1):
    res = ()
    sample_space = ["HEADS", "TAILS"]

    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def dreidel(count=1):
    res = ()
    sample_space = ["NUN", "GIMEL", "HE", "SHIN"]

    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def cat(count=1):
    res = ()
    sample_space = ["ALIVE", "DEAD"]

    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def switch(count=1):
    res = ()
    sample_space = ["ON", "OFF"]

    for _ in range(int(count)):
        res += (rop.choice(sample_space),)

    return res


def spinner(lower, upper=0):
    if lower > upper:
        lower, upper = upper, lower

    return rop.randint(int(lower), int(upper))


def combi(list=[]):
    res = ()

    if str(type(list)) == "<class 'str'>":
        temp = []
        temp.append(list)
        list = temp

    elif str(type(list)) == "<class 'int'>":
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
