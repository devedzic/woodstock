"""Demonstrates working with strings in Python.
"""

import string


def demonstrate_formatting():
    """Using classical formatting.
    - \n is the new line char
    - r'...' - raw formatting
    - using \"\"\"...\"\"\" for multi-line formatting
    - string "multiplication"
    - substrings / slicing
    - str() vs. repr() (usually the same, but with whitespace there is a difference)
    """

    print('%5.2f %s %13d' % ((7 / 3), "sss", 5))    # classical, printf-like formatting
    print('C:\nowhere')                             # \n is the new line char
    print(r'C:\nowhere')                            # raw formatting
                                                    # using """...""" for multi-line formatting
    print("""Woodstock headliners:
        Jimi Hendrix
        The Who
        ...
    """)
    print("Jimi Hendrix   " * 3)                    # string "multiplication"
    print()

    hendrix = "Jimi Hendrix"                        # substrings / slicing
    print(hendrix[0:3])
    print(hendrix[-3:])
    print(hendrix[3:6])
    print(hendrix[:])
    print()

    print(1)
    print(str(1))
    print(repr(1))
    print('This is', 1)                             # str(1) is not necessary here
    print('This is ' + str(1))                      # str(<numeric>) and the like MUST be used in concatenation
    print(string.whitespace)
    print(str(string.whitespace))                   # str() and repr() usually give the same results, and usually str()
    print(repr(string.whitespace))                  # is used; but, with e.g. whitespace chars, there is a difference


def demonstrate_fancy_formatting():
    """Using "fancy" formatting.
    - format strings like '{0}{1} {2}', '{0}{1} {2}, {3}', etc.
    """

    print('The {} festival was held in {}, on {} farm.'.format('Woodstock', 1969, 'Max Yasgur\'s'))
    print('{}{} {}, {}, ...'.format('The headliners', ':', 'CSNY', 'Santana'))


def demonstrate_string_operations():
    """Using different string operations.
    - endswith(), split(), center(), in (aka contains()), == (aka equals(), len(),...), strip() (lstrip(), rstrip())
    """

    print('Woodstock'.endswith('ck'))
    print('Woodstock was held in 1969.'.split())
    print('Woodstock was held in 1969, and it was great :)'.split(sep=','))
    print('Woodstock'.center(20, '#'))
    print('oo' in 'Woodstock')
    festival = 'Woodstock'
    print('Woodstock' == festival)                  # comparison for content equality (==), no equals()
    print(len('Woodstock'))
    print('   Woodstock       '.strip() + str(1969))


if __name__ == '__main__':

    # demonstrate_formatting()
    # demonstrate_fancy_formatting()
    demonstrate_string_operations()
