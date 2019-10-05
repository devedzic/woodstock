"""The very first module in a more structured version of the project.
"""


def show_year():
    """The Woodstock year function.
    """

    print('The Woodstock year function')
    year = input('Enter the year when Woodstock was held: ')
    print('Woodstock was held in ' + year)
    print(__name__)


if __name__ == '__main__':

    # Printing with ' ' and printing without '\n'

    print('Woodstock was a music festival ' + '\nheld August 15–18, 1969, on Max Yasgur\'s dairy farm.')
    print('Woodstock was a music festival', 'held August 15–18,', str(1969) + '.')
    print()

    # Printing with classical formatting (%)

    # Keyboard input

    # # print('Enter the year when Woodstock was held: ', end='')
    # # year = input()
    year = input('Enter the year when Woodstock was held: ')
    print('Woodstock was held in ' + year)
    print()

    # A simple loop and the range() built-in function

    for i in range(1, 4):
        print('Woodstock')

    # Printing docstrings

    print(show_year.__doc__)

    # A simple list, accessing list elements, printing lists

    performers = ['Jimi Hendrix', 'Janis Joplin', 'The Who']
    print(performers)
    print(performers[1])
    print()

    # Looping through list elements - for loop

    for i in range(len(performers)):
        print(performers[i])
    print()

    # Printing a list using enumerate()

    performers = ['Jimi Hendrix', 'Janis Joplin', 'The Who']
    print(enumerate(performers))
    print(list(enumerate(performers)))
    for i, v in list(enumerate(performers)):
        print(str(i) + ':', v)
    print()

    # A simple function call

    show_year()

    # Global variables: __name__, __file__, __doc__,...

    print(__name__)
    print(show_year.__doc__)
    print(__file__)
    print()

