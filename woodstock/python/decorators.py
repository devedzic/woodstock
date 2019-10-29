"""Demonstrates pass, returning None, functions as parameters of other functions,
functions as return values of other functions and user-defined decorators
"""


import functools

from woodstock.python import functions


def return_none():
    """Demonstrates returning None and the pass statement.
    """

    # return None
    pass


def pass_function_as_parameter(f, *args, **kwargs):
    """Demonstrates using another function as a parameter. It works because functions are objects.
    The argument/parameter list specified as in this function is a fairly general one -
    it works regardless of the number of *args and **kwargs in the function call (both can be 0).
    If a call to f includes positional arguments, then they are part of the *args argument of this function.
    The same holds for optional *args in the call to f, as well as for the default arguments of f (if any).
    Likewise, if f is called with keyword arguments, they are included in the **kwargs argument of this function.
    In other words, from https://stackoverflow.com/a/3394898/1899061:
    You can use *args and **kwargs along with named arguments too. The explicit arguments get values first
    and then everything else is passed to *args and **kwargs. The named arguments come first in the list. For example:
        def table_things(titlestring, **kwargs)
    """

    # Try something like this in Python Console:
    #     p = *[1,2,3]        # generates an error
    #     p = *[1,2,3],       # generates a tuple
    #     p = 44, *[1,2,3]    # generates another tuple
    #     print(p)
    #     print(*p)

    # Try also this in Python Console:
    #     def f(*args):
    #         return sum(*args)     # it must be sum(*args), not sum(args), although in Python Console sum((1, 2)) is OK
    #     def g(f, *args):
    #         return f(*args)       # heuristics: if *args is in a f. signature, use *args in the f. body as well
    #     g(f, 1, 2, 3)             # result: 6

    f(*args, **kwargs)
    print(*args)
    print(type(*args))
    # print(args)
    # print(type(args))           # It's a tuple; note that print(type(*args)) generates an error if len(args) > 1
    # print(type(kwargs))         # It's a dict; note that print(type(**kwargs)) generates an error if len(kwargs) > 1


def return_function(full_name, first_name_flag):
    """Demonstrates using a function as the return value from another function.
    In this example, depending on the first_name_flag, return_function() returns one of the following functions:
    - a function that returns a person's first name
    - a function that returns a person's family name
    """

    name = full_name.split()

    def first_name():
        return name[0]

    def family_name():
        return name[1]

    if first_name_flag:
        return first_name
    else:
        return family_name


def return_function_with_args(*args):
    """Demonstrates using a function as the return value from another function.
    The returned function has parameters/arguments.
    In this example, depending on len(args), return_function_with_args() returns one of the following functions:
    - a function that returns an empty list
    - a function that returns a tuple of args (or a list or args, or...)
    """

    def return_empty():
        return []

    def return_tuple(*parameters):                      # '*' is important here; without it, args is a positional arg!
        return tuple(parameters)

    if args:
        return return_tuple
    else:
        return return_empty


# def a_very_simple_decorator(f):
def a_very_simple_decorator(f, *args):
    """Illustrates the essential idea of decorators:
        - take a function (f) as a parameter of a decorator function (decorator)
        - use the parameter function f inside an inner wrapper function (g)
        - return the inner wrapper function g from the decorator function
    Then define f and run f = decorator(f) before calling f.
    Even better, just put @decorator before the definition of f. Each call to f will then actually run decorator(f).
    """

    # Examples (run them in Python Console):

    # def decorator(f):
    #     def g():
    #         return f('Woodstock')
    #     return g
    #
    # def something(x):
    #     return x
    # ...
    # >>> something(4)
    # 4
    # ...
    # >>> something = decorator(something)
    # >>> something
    # <function __main__.decorator.<locals>.g()>
    # >>> something()
    # Woodstock

    # def decorator(f, *args):
    #     def g():
    #         print('Woodstock')
    #         return f(*args)
    #     return g
    #
    # def something(x):
    #     return x
    # ...
    # >>> something(4)
    # 4
    # ...
    # >>> something = decorator(something, 'Woodstock')
    # >>> something
    # <function __main__.decorator.<locals>.g()>
    # >>> something()
    # Woodstock
    # Woodstock

    def g():
        print('Woodstock')
        return f(*args)
    return g


def something(*x):
    return x


def highlight_performers(f_to_decorate):
    """Demonstrates how to develop a decorator. Uses the decorator-writing pattern:
    import functools
    def decorator(func):
        @functools.wraps(func)			                # preserves func's identity after it's decorated
        def wrapper_decorator(*args, **kwargs):
            # Do something before
            value = func(*args, **kwargs)
            # Do something after
            return value
        return wrapper_decorator
    """

    @functools.wraps(f_to_decorate)
    def highlight(*args):
        uppercase_args = [a.upper() for a in args[1:]]
        highlighted_f = f_to_decorate(args[0], *uppercase_args)
        print('-' * (sum([len(a) for a in args]) + (len(args) - 1) * 2))
        return highlighted_f

    return highlight


@highlight_performers
def print_festival(name, *performers):
    """Prints the name and the performers of a festival, assuming that both name and *performers are strings.
    The decorator before the function signature (@highlight_performers) illustrates how to apply a decorator;
    omit it if decorating manually.
    """

    print(name + ':' if performers else name, ', '.join(performers))


if __name__ == '__main__':

    # print(return_none())                                    # returning None

    # pass_function_as_parameter(
    #     functions.demonstrate_annotations,
    #     'Woodstock')
    # pass_function_as_parameter(
    #     functions.demonstrate_annotations,
    #     'Monterey Pop',
    #     1967)

    # pass_function_as_parameter(
    #     functions.show_festival,
    #     'Monterey Pop')
    # pass_function_as_parameter(
    #     functions.show_festival,
    #     'Monterey Pop',
    #     1967, 'Monterey, CA')

    # headliners = ['Jimi Hendrix', 'CSNY']
    # pass_function_as_parameter(
    #     functions.use_all_categories_of_args,
    #     'Woodstock')
    # pass_function_as_parameter(
    #     functions.use_all_categories_of_args,
    #     'Woodstock',
    #     *headliners)
    # pass_function_as_parameter(
    #     functions.use_all_categories_of_args,
    #     'Woodstock',
    #     *headliners,
    #     place='Bethel', state='NY')

    # print(return_function("Jimi Hendrix", True)())
    # print(return_function_with_args(1)('Jimi Hendrix', 'CSNY'))
    # print(return_function_with_args()())
    # # The next line would generate TypeError: return_empty() takes 0 positional arguments but 1 was given!!!
    # # print(return_function_with_args()('Jimi Hendrix'))

    # print(something(4))
    # something = a_very_simple_decorator(something, 'Monterey')
    # print(something)
    # print(something())

    festival = 'Woodstock'
    performers = ['Jefferson Airplane', 'The Who', 'Grateful Dead']
    # print_festival(festival, *performers)
    # print_festival = highlight_performers(print_festival)
    print_festival(festival, *performers)
    print(print_festival.__name__)
