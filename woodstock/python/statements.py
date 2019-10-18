"""Demonstrates peculiarities of if, for, while and other statements
"""


def demonstrate_branching():
    """Details and peculiarities of if statements.
    - is compares id()'s, == compares contents
    - id()'s are the same for equal strings (), but not for lists, user class instances,...
    - the condition of an if-statement need not necessarily be a boolean
    - there can be more than one elif after if (no switch statement, use multiple elif instead)
    """

    # w = 'Woodstock'
    # w1 = 'Woodstock'
    w = ['Woodstock']
    w1 = ['Woodstock']
    if w == w1:
        print(True)
    else:
        print(False)
    if w is w1:
        print(True)
    else:
        print(False)
    print(id(w), id(w1))
    print()

    if 2:
        print(True)
    else:
        print(False)
    print()

    if w == 1969:
        print(1969)
    elif w == 'Bethel':
        print('Bethel')
    elif w == 'Hendrix':
        print('Hendrix')
    else:
        print('Neither')
    print()


def demonstrate_loops():
    """Different kinds of loops. Also break and continue.
    - it is not necessary to iterate through all elements of an iterable
    - step in range()
    - unimportant counter (_)
    - break and continue
    - while loop
    """

    w = ['Woodstock', 1969, 'Bethel', True]
    for i in w[0:2]:
        print(i)
    print()

    for i in range(1, 10, 2):
        print(i, end=' ')
    print()
    print()

    for _ in range(3):
        print('Woodstock')
    print()

    i = 0
    while i < len('Woodstock'):
        print('Woodstock'[i], end=' ')
        i += 1
    print()


if __name__ == '__main__':

    # demonstrate_branching()
    demonstrate_loops()

