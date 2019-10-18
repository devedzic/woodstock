"""Demonstrates tuples
"""


def demonstrate_tuples():
    """Creating and using tuples.
    - create and print 1-tuple, 2-tuple, mixed-type n-tuple
    - accessing elements of a tuple using []
    - demonstrate that tuples are immutable
    """

    woodstock = ('Woodstock', 1969, True)
    print(woodstock)
    print(type(woodstock))
    print()
    # w = tuple('Woodstock')
    # print(w)
    # print(type(w))
    w = ('Woodstock', )
    # w = tuple('Woodstock', )
    print('w:', w)
    print(type(w))
    print()
    print(woodstock[:])
    # woodstock[0] = 0                    # No way! Tuples are immutable!
    print()


def demonstrate_zip():
    """Using the built-in zip() function with tuples and double-counter for-loop.
    """

    woodstock = ('Woodstock', 1969, 'Bethel, NY')
    monterey_pop = ('Monterey Pop', 1967, 'Monterey, CA')
    festivals = zip(woodstock, monterey_pop)
    print(festivals)
    # print(list(festivals))
    for i in festivals:                   # zip() returns an iterator, which can be exhausted only once
        print(i)                          # (so, the print in the next for loop is "empty")
    for i, k in festivals:
        print(str(i) + ';', k)


def demonstrate_packing():
    """Packing and unpacking tuples.
    """

    woodstock = ('Woodstock', 1969, 'Bethel, NY')
    name, year, location = woodstock
    print(name, year, location)
    woodstock = name, year, location
    print(woodstock)


if __name__ == '__main__':

    # demonstrate_tuples()
    demonstrate_zip()
    # demonstrate_packing()
