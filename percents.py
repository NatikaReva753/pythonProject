def percents(x, y):
    """What percentage of x is y"""
    one_percent = x / 100
    result = y / one_percent
    print(str(y) + " is " + str(result) + " % of " + str(x))
    return result


def print_percents(x, y):
    """Print what percentage of x is y"""
    print(str(y) + " is " + str(percents(x, y)) + " % of " + str(x))

