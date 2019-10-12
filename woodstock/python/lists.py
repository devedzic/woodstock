"""Demonstrates working with lists.
"""


def demonstrate_lists():
    """Using just the simplest operations with lists.
    - create a non-empty list with different kinds of elements
    - accessing/slicing a list
    - comparing 2 lists (== vs. is)
    - concatenating 2 lists (the + operator)
    - looping through a list
    """

    # create a non-empty list with different kinds of elements
    woodstock = ['Woodstock', 1969, True]
    # accessing/slicing a list
    print(woodstock[0])
    print(woodstock[0:2])
    # comparing 2 lists (== vs. is)
    print(woodstock == ['Woodstock', 1969, True])
    print(woodstock is ['Woodstock', 1969, True])
    # concatenating 2 lists (the + operator)
    print(woodstock + ['Bethel', 'NY'])
    # looping through a list
    for w in woodstock:
        print(w)


def demonstrate_list_methods():
    """Using append(), insert(), remove(), pop(), extend(),
    count(), index(), reverse(), len(),...
    Also, "in" and "not in" operators can be used to search lists
    for the occurrence of a given element.
    """

    woodstock = ['Woodstock', 1969, True]
    # append()
    print(woodstock.append('Bethel'))
    print(woodstock)
    # insert()
    print(woodstock.insert(2, 'Aug 15-18'))
    print(woodstock)
    # remove()
    woodstock.remove('Aug 15-18')
    print(woodstock)
    del woodstock[3]
    print(woodstock)
    # pop()
    woodstock.pop()                             # or, e.g., woodstock.pop(1) to remove the second element
    print(woodstock)
    # extend(): extend a list with elements from an iterable
    woodstock.extend((1969, 'Bethel'))
    print(woodstock)
    # count(): count the occurrences of an element in a list
    print(woodstock.count(1969))
    # index(): what is the index of an element in a list
    print(woodstock.index(1969))
    # reverse()
    print(woodstock.reverse())
    print(woodstock)
    # len()
    print(len(woodstock))
    # the in operator
    print(1969 in woodstock)
    # the not in operator
    print(1234 not in woodstock)


def demonstrate_arrays():
    """Using array.array() to build list-based numeric arrays.
    Demonstrating that lists and arrays are different types.
    """

    from array import array
    a = array('i', [1969, -13])
    print(a)
    print(a[1])
    print(type(a))
    list1 = [1969, -13]
    print(list1)
    print(type(list1))


def populate_empty_list():
    """Creating an empty list and populating it with random values.
    """

    from random import seed, randint

    seed(35)
    l1 = []
    for i in range(1000):
        l1.append(randint(1, 100))
    print(l1[:10])


def duplicate_list():
    """Duplicating lists (carefully :)).
    Don't use l2 = l1, but either of the following:
    - l2 = l1.copy()
    - l2 = l1 + []
    - l2 = l1[:]
    """


def demonstrate_list_comprehension():
    """Showing examples of list comprehension.
    - list comprehension over an array.array()
    - list comprehension over a list of strings
    Using str() and join() in printing results.
    """

    from array import array
    a = array('i', [1969, -13, 20])
    l1 = [str(e) for e in a]
    print(l1)
    print('join:', ''.join(l1))
    songs = ['We can work it out', 'Love the one you\'re with', 'You never give me your money']
    # print([title.split() for title in songs])
    first_words = [words[0] for words in [title.split() for title in songs]]
    print(' '.join(first_words))


if __name__ == '__main__':

    # demonstrate_lists()
    # demonstrate_list_methods()
    # demonstrate_arrays()
    # populate_empty_list()
    demonstrate_list_comprehension()

