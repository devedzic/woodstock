"""Demonstrates how operators and expressions work in Python.
"""


# Demonstrate arithmetic operators (function demonstrate_arithmetic_operators())
def demonstrate_arithmetic_operators():
    """Working with arithmetic operators.
    """

    print(((13 // 4) % 2) + 5)


# Demonstrate relational operators (function demonstrate_relational_operators())
def demonstrate_relational_operators():
    """Working with relational operators.
    """

    # - simple comparisons
    print(1 >= 2)
    if 0:
        print(True)
    else:
        print(False)
    if '':
        print("'' is True")
    else:
        print("'' is False")
    if 0.0:
        print(True)
    else:
        print(False)
    print()

    # - comparing dates (== vs. is)
    from datetime import date
    d1 = date(2019, 10, 12)
    print(d1)
    d2 = date.today()
    if d1 == d2:
        print('d1 == d2')
    else:
        print('d1 != d2')
    if d1 is d2:
        print('d1 is d2')
    else:
        print('d1 is not d2')
    print()

    # - None in comparisons, type(None)
    if not None:
        print('not None is True')
    else:
        print('not None is not True')
    print(type(None))
    print(None)


# Demonstrate logical operators (function demonstrate_logical_operators())
def demonstrate_logical_operators():
    """Working with logical operators.
    """

    # - logical operations with True and False
    print('True and False:', True and False)
    print('True or False:', True or False)
    print('not False:', not False)
    print('True and None:', True and None)
    print('1 and None:', 1 and None)
    print()

    # - logical operations with dates
    from datetime import date
    d1 = date.today()
    d2 = date(1999, 12, 21)
    if d1 > d2:
        print('d1 > d2')
    else:
        print('d1 <= d2')

    # - logical operations with None (incl. None and int, None and date, etc.)
    print(None and 1)
    print(None and d1)

# - None and date vs. None > date
    print(None > d1)


if __name__ == '__main__':

    # demonstrate_arithmetic_operators()
    # demonstrate_relational_operators()
    demonstrate_logical_operators()

