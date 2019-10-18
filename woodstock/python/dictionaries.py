"""Demonstrates dictionaries
"""


def demonstrate_dictionaries():
    """Creating and using dictionaries.
    - create a blank (empty) dictionary
    - create a non-empty dictionary
    - print a non-empty dictionary
        - print all items using the items() function
        - print one item per line
    - pprint dictionary in one column
    - add/remove items to/from a dictionary
    - update a dictionary with the items from another dictionary or from an iterable of (k, v) pairs using dict.update()
    - using the keys() and values() functions
    """

    # create a blank (empty) dictionary
    woodstock = {}
    print(type(woodstock))
    print(woodstock)

    # create a non-empty dictionary
    woodstock = {'name': 'Woodstock', 'year': 1969, 'location': 'Bethel, NY'}
    print(type(woodstock))
    print(woodstock)
    print()

    # print all items using the items() function
    print(woodstock.items())
    print(list(woodstock.items()))

    # print one item per line
    for i in woodstock.items():
        print(i)
    print()
    for k, v in woodstock.items():
        print(k + ':', v)
    print()

    # pprint dictionary in one column
    from pprint import pprint
    pprint(woodstock, width=1)
    print()

    # add/remove items to/from a dictionary
    woodstock['date'] = 'Aug 15-18'
    print(woodstock)
    del woodstock['date']
    print(woodstock)

    # update a dictionary
    woodstock['name'] = 'Woodstock festival'
    print(woodstock)
    name = {'name': 'Woodstock'}
    woodstock.update(name)
    # name = ('name', 'Woodstock')
    # woodstock.update([name])
    print(woodstock)
    print()

    # using the keys() and values() functions
    print(type(woodstock.keys()))
    print(type(woodstock.values()))
    for k, v in (zip(woodstock.keys(), woodstock.values())):
        print(k + ':', v)


def sort_dictionary(d, by):
    """Sorting a dictionary by keys or by values.
    - using zip()
    - using operator.itemgetter()
    - using lambda
    """

    # # using zip()
    # if by == 'k':
    #     return dict(sorted(zip(d.keys(), d.values())))
    # elif by == 'v':
    #     return dict(sorted(zip(d.values(), d.keys())))
    # else:
    #     return None

    # using lambda
    if by == 'k':
        return dict(sorted(d.items(), key=lambda item: item[0]))
    elif by == 'v':
        return dict(sorted(d.items(), key=lambda item: item[1]))
    else:
        return None


def demonstrate_dict_sorting():
    """Demonstrate sorting a dictionary.
    """

    woodstock = {'name': 'Woodstock',
                 'year': '1969',
                 'location': 'Bethel, NY'}
    print(sort_dictionary(woodstock, 'k'))
    print(sort_dictionary(woodstock, 'v'))
    print(sort_dictionary(woodstock, 5))


if __name__ == '__main__':

    # demonstrate_dictionaries()
    demonstrate_dict_sorting()

