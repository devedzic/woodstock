"""The class representing the concept of lineup of a festival.
"""

from datetime import date, datetime, time

from woodstock.music.performer import Performer
from woodstock.util.utility import format_date


class Lineup():
    """The class describing the concept of lineup of a festival.
    It includes a list of Performer objects and a show date for these performers.
    """

    # Insert a class variable (static field), such as definition
    definition = 'The list of performers on a specific date.'

    def __init__(self, *performers, date=date.today()):
        self.performers = performers
        self.date = date
        self.__i = 0                                            # introduce and initialize iterator counter, self.__i

    def __str__(self):
        # return f'Lineup {self.date}: ' + \
        #        ', '.join([performer.name for performer in self.performers if isinstance(performer, Performer)]) \
        #        if self.performers else f'Lineup {self.date}: not specified'
        return f'Lineup for {format_date(self.date)}: ' + \
               ', '.join([performer.name for performer in self.performers if isinstance(performer, Performer)]) \
               if self.performers else f'Lineup for {format_date(self.date)}: not specified'

    def __eq__(self, other):
        return self == other

    # Alternative constructor
    @classmethod
    def from_name_list(cls, names, date=date.today()):
        performers = [Performer(performer) for performer in names if isinstance(performer, str)]
        return cls(*performers, date)

    @staticmethod
    def is_date_valid(d):
        """The first rock festival, the KFRC Fantasy Fair and Magic Mountain Music Festival,
        had been held on June 10-11, 1967, at Mount Tamalpais in Marin County.
        So, the valid date for creating a lineup for a r'n'r festival is between June 10-11, 1967, and today."""

        if not isinstance(d, date) and not isinstance(d, datetime):
            return False
        return date(1967, 6, 1) < d < date.today()

    def __iter__(self):
        return self

    def __next__(self):
        if self.__i < len(self.performers):
            self.__i += 1
            return self.performers[self.__i - 1]
        else:
            raise StopIteration


if __name__ == "__main__":

    # pass

    # class variables (like static fields in Java; typically defined and initialized before __init__())
    # object class (like the Object class in Java; all classes inherit from object
    #   try, e.g., list.__mro__ in the console)
    #   object class defines object.__eq__(self, other) etc.
    #   object.__ne__(self, other), the inverse of object.__eq__(self, other),
    #   is provided by Python automatically once object.__eq__(self, other) is implemented

    # Data

    # Some of the Woodstock performers, Aug 15-16, 1969
    melanie = Performer('Melanie', is_band=False)
    arloGuthrie = Performer('Arlo Guthrie', is_band=False)
    # Some of the Woodstock performers, Aug 16-17, 1969
    gratefulDead = Performer('Grateful Dead', is_band=True)
    jeffersonAirplane = Performer('Jefferson Airplane', is_band=True)
    theWho = Performer('The Who', is_band=True)
    ccr = Performer('Creedence Clearwater Revival', is_band=True)
    # Some of the Woodstock performers, Aug 17-18, 1969
    csny = Performer('Crosby, Stills, Nash and Young', is_band=True)
    jimiHendrix = Performer('Jimi Hendrix', is_band=False)
    theBand = Performer('The Band', is_band=True)

    # Check the basic methods (__init__(), __str__(),...)
    performers = [gratefulDead, jeffersonAirplane, theWho, ccr]
    day2_lineup = Lineup(*performers, date=date(1969, 8, 16))
    print(day2_lineup)
    print(day2_lineup.performers)
    print([performer.name for performer in day2_lineup.performers])
    print()

    # Check the alternative constructor (@classmethod from_name_list(name_list))
    name_list = [performer.name for performer in day2_lineup.performers]
    lineup = Lineup.from_name_list(name_list)
    print(lineup)
    print()

    # Check date validator (@staticmethod validate_date(date))
    print(Lineup.is_date_valid(date(1967, 6, 1)))
    print(Lineup.is_date_valid(date(1967, 6, 15)))
    print()

    # Check the iterator
    for _ in day2_lineup:
        print(next(day2_lineup).name)
    print()

    # Repeated attempt to run the iterator fails, because the iterator is exhausted
    for _ in day2_lineup:
        print(next(day2_lineup).name)


