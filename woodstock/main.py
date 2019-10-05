# # # Hello world: the print() built-in function and the + operator
# #
# # print('Woodstock was a music festival ' + '\nheld August 15–18, 1969, on Max Yasgur\'s dairy farm.')
# # print('Woodstock was a music festival', 'held August 15–18,', str(1969) + '.')
# # print()
# #
# # # print('Enter the year when Woodstock was held: ', end='')
# # # year = input()
# # year = input('Enter the year when Woodstock was held: ')
# # print('Woodstock was held in ' + year)
# # print()
# #
# #
# # # A simple function and function call
# #
# def show_year():
#     """The Woodstock year function.
#     """
#
#     print('The Woodstock year function')
#     year = input('Enter the year when Woodstock was held: ')
#     print('Woodstock was held in ' + year)
# #
# #
# # show_year()
# #
# #
# # # A simple loop and the range() built-in function
# #
# # for i in range(1, 4):
# #     print('Woodstock')
# #
# #
# # A simple list, accessing list elements, printing lists
#
# performers = ['Jimi Hendrix', 'Janis Joplin', 'The Who']
# print(performers)
# print(performers[1])
# print()
#
#
# # Looping through list elements - for and enumerate()
#
# for i in range(len(performers)):
#     print(performers[i])
# print()
#
# print(enumerate(performers))
# print(list(enumerate(performers)))
# for i, v in list(enumerate(performers)):
#     print(str(i) + ':', v)
# print()
#
#
# # Global variables: __name__, __file__, __doc__,...
# print(__name__)
# print(show_year.__doc__)
# print(__file__)
# print()

from woodstock.python import inception
inception.show_year()
