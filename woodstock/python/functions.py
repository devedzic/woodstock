"""Demonstrates details of writing Python functions: annotations, default args, kwargs
"""


# def demonstrate_annotations(festival, year=1969):
def demonstrate_annotations(festival: str, year: int = 1969) -> str:
    """

    :param festival: Festival name
    :param year: Festival year
    :return: name, year

    """

    """Demonstrates how to use annotations of function parameters/arguments and of function return type.
    - print the function parameters/arguments
    - print the value of the __annotations__ attribute of this function
    - print the docstring of this function
    - return a formatted string (including function parameters/arguments)
    """
    print('festival:', festival + ',', 'year:', year)
    print('Annotations:', demonstrate_annotations.__annotations__)
    print()
    print(demonstrate_annotations.__name__,
          demonstrate_annotations.__doc__)
    return festival + ', ' + str(year)

    # # Alternatively:
    # return(f'Just called demonstrate_annotations.__doc__("{festival}", {year})')


def show_festival(name, year=1969, location='Bethel'):
    """Demonstrates default arguments/parameters.
    - print the function arguments/parameters in one line
    """

    print(locals())
    # print(show_festival.__dict__)

    print(locals())
    # print(show_festival.__dict__)

    # # See also https://stackoverflow.com/a/12627202/1899061 :
    # from inspect import signature, Parameter
    # s = signature(show_festival)
    # print(s.parameters)
    # print([(k, v) for k, v in s.parameters.items()])
    # print([(k, v.default)
    #        for k, v in s.parameters.items()
    #        if v.default is not Parameter.empty])

    print(f'Festival: {name} ({year}), {location}')

    # # Alternatively:
    # print(name + ':', year, f'({location})')


def use_flexible_arg_list(prompt: str, *headliners):
    """Demonstrates flexible number of arguments/parameters.
    - print the prompt and the list of festival headliners in one line
    """

    # headliners = list(headliners)                                 # not necessary, although improves readability

    print(headliners)

    # print(prompt + ':', ', '.join(headliners) + ',...')           # basic version
    print(prompt + ':' if len(headliners) else prompt,
          ', '.join(headliners) + ',...' if headliners else '')

    # # Alternatively:
    # print(prompt + ':' if headliners else prompt, ', '.join(headliners) + ',...' if headliners else '')


def use_all_categories_of_args(prompt, *headliners, year=1969, **location_details):
    """Demonstrates positional args, flexible args, keyword args, and kwargs (flexible keyword args).
    - print all arguments/parameters, including the keyword arguments/parameters, in one line
    """

    print(location_details)
    print(headliners)
    print()

    print(prompt, '(' + str(year) + '):',
          ', '.join(headliners) + ',...' if headliners else '[headliners not specified]',
          '(' + ', '.join([v for k, v in location_details.items()]) + ')' if location_details else '')

    # # Alternatively (breaking the whole string in pieces for better focus, and joining them together eventually):
    # prompt_part = f'{prompt}:' if headliners else f'{prompt}'
    # headliners_part = ', '.join(headliners) + ',...' if headliners else '[no headliners specified]'
    # year_part = f'({year};' if location_details else f'({year}' if location_details else f'({year})'
    # location_details_part = ', '.join([v for v in location_details.values()]) + ')' if location_details else ''
    # print(prompt_part, headliners_part, year_part, location_details_part)


if __name__ == "__main__":

    # print(demonstrate_annotations('Monterey Pop', 1967))
    # print()
    # print(demonstrate_annotations('Woodstock'))
    # print()

    # show_festival('Woodstock')
    # show_festival('Monterey Pop', year=1967, location='Monterey, CA')
    # print()

    # use_flexible_arg_list('Woodstock', 'Jimi Hendrix', 'Jefferson Airplane', 'Grateful Dead')
    # use_flexible_arg_list('Woodstock')
    # print()

    use_all_categories_of_args('Woodstock', 'Jimi Hendrix', 'Jefferson Airplane', place='Bethel', state='NY')
    use_all_categories_of_args('Woodstock')
    use_all_categories_of_args('Woodstock', 'Jimi Hendrix', 'Jefferson Airplane')
    use_all_categories_of_args('Woodstock', place='Bethel', state='NY')

