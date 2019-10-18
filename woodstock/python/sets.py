"""Demonstrates sets
"""


def demonstrate_sets():
    """Creating and using sets.
    - create a set with an attempt to duplicate items
    - demonstrate some of the typical set operators:
        & (intersection)
        | (union)
        - (difference)
        ^ (disjoint)
    """

    woodstock = {'Woodstock', 1969, 'Woodstock'}
    print(woodstock)
    print()
    print(woodstock & {'Woodstock'})
    print(woodstock | {'Bethel'})
    print(woodstock - {'Woodstock'})
    print(woodstock ^ {'Woodstock', 'Bethel'})


if __name__ == '__main__':

    demonstrate_sets()

