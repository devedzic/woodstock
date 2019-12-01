"""The class representing the concept of lineup of a festival.
"""

from datetime import date, datetime, time
import json

from woodstock.music.performer import Performer, PerformerEncoder, performer_json_to_py
from woodstock.util.utility import format_date


class Lineup():
    """The class describing the concept of lineup of a festival.
    It includes a list of Performer objects and a show date for these performers.
    """

    # Class variables: like static fields in Java; typically defined and initialized before __init__()
    # Insert a class variable (static field), such as definition, date_pattern,...
    definition = 'The list of performers on a specific date.'
    date_pattern = '%b %d, %Y'

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
        return self == other if isinstance(other, Lineup) else False

    # Alternative constructor 1
    @classmethod
    def from_name_list(cls, names, date=date.today()):
        performers = [Performer(performer) for performer in names if isinstance(performer, str)]
        return cls(*performers, date=date)

    # Alternative constructor 2
    @classmethod
    def from_lineup_str(cls, lineup_str):
        if not lineup_str:
            return None
        split = lineup_str.split('Lineup for ')[1].split(': ')
        date_str = split[0]
        performer_names = split[1].split(', ')
        performers = [Performer(performer) for performer in performer_names if isinstance(performer, str)]
        return cls(*performers, date=datetime.strptime(date_str, Lineup.date_pattern))

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


def next_performer(lineup):
    """Generator that shows performers from a lineup, one at a time.
    """

    i = 0
    for performer in lineup.performers:
        if i == 0:
            print('The first one:')
        yield performer
        i += 1
        if i < len(lineup.performers):
            print('Another one:')


class LineupEncoder(json.JSONEncoder):
    """JSON encoder for Lineup objects.
    """

    # def default(self, o):                             # doesn't work well, '__Lineup__' is absorbed everywhere in dict
    #     # attr_dict = getattr(o, '__dict__', str(o))
    #     # print(type(attr_dict))
    #     # return {'__Lineup__': str(attr_dict)}
    #     return getattr(o, '__dict__', str(o))

    # def default(self, o):                             # works well, but converts date objects to isoformat
    #     return {'__Lineup__': json.dumps(o, default=lambda x: getattr(x, '__dict__', str(x)))}

    # def default(self, o):                             # works well for encoding,
    #     if isinstance(o, date):                       # but makes double-quote problems when decoding
    #         return o.isoformat()                      # returns datetime isoformat instead of date isoformat (?)
    #     if isinstance(o, Lineup):
    #         return {"__Lineup__": o.__dict__}
    #     return {f"__{o.__class__.__name__}__": o.__dict__}

    def default(self, o):
        if isinstance(o, Lineup):
            d = o.__dict__.copy()
            d['date'] = o.date.isoformat()
            d['performers'] = json.dumps([p for p in o.performers], cls=PerformerEncoder, indent=4)
            return {"__Lineup__": d}
        return {f"__{o.__class__.__name__}__": o.__dict__}


def lineup_json_to_py(lineup_json):
    """JSON decoder for Lineup objects (object_hook parameter in json.loads()).
    """

    # if '__Lineup__' in lineup_json:                   # works well, but has trouble with isoformat of date objects
    #     # lineup = Lineup(Performer(''), date=date.today())
    #     lineup = Lineup()
    #     # lineup.__dict__.update(lineup_json['__Lineup__'])
    #     lineup.__dict__.update(json.loads(lineup_json['__Lineup__']))
    #     print(lineup)
    #     return lineup
    # return lineup_json

    if "__Lineup__" in lineup_json:
        lineup = Lineup()
        lineup.__dict__.update(lineup_json["__Lineup__"])
        # The next line returns a date object in spite of the compiler complaint
        lineup.__dict__.update({'date': date.fromisoformat(lineup.date)})
        # print(lineup.performers)
        # print(type(lineup.performers))
        # print(str(lineup.performers))
        # lineup.__dict__.update({"performers": json.loads(str(lineup.performers), object_hook=performer_json_to_py)})
        lineup.__dict__.update({'performers': tuple(json.loads(lineup.performers, object_hook=performer_json_to_py))})
        # print(lineup.performers)
        lineup.__dict__.update({'_Lineup__i': 0})
        # # print(str(lineup.date))
        # print(type(lineup.date))
        # print(lineup.date)
        # # lineup.date = datetime.fromisoformat(lineup.date.split('T')[0])
        # # lineup.date = datetime.fromisoformat(lineup.date).date()
        # lineup.date = datetime.fromisoformat(lineup.date)
        return lineup
    return lineup_json


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

    # # Check the alternative constructor 1 (@classmethod from_name_list(name_list))
    # name_list = [performer.name for performer in day2_lineup.performers]
    # lineup = Lineup.from_name_list(name_list)
    # print(lineup)
    # print()
    #
    # # Check the alternative constructor 2 (@classmethod from_lineup_str(lineup_str))
    # lineup_str = day2_lineup.__str__()
    # day2_lineup = Lineup.from_lineup_str(lineup_str)
    # print('Day 2 lineup reconstructed from str:', day2_lineup)
    # print()
    #
    # # Check date validator (@staticmethod validate_date(date))
    # print(Lineup.is_date_valid(date(1967, 6, 1)))
    # print(Lineup.is_date_valid(date(1967, 6, 15)))
    # print()
    #
    # # Check the iterator
    # for performer in day2_lineup:
    #     print(performer.name)
    # print()
    #
    # # Repeated attempt to run the iterator fails, because the iterator is exhausted
    # for performer in day2_lineup:
    #     print(performer.name)
    # print()
    #
    # # Demonstrate generators
    # print(next_performer(day2_lineup))
    # next_p = next_performer(day2_lineup)
    # print(next(next_p))
    # print(next(next_p))
    # print(next(next_p))
    # print(next(next_p))
    # # # print(next(next_p))                                   # raises StopIteration
    # # print()
    # # # for performer in next_performer(day2_lineup):
    # # #     print(performer)
    # # # print('No more.')
    #
    # # # Demonstrate generator expressions
    # # next_p = (performer for performer in day2_lineup.performers)
    # # print(next(next_p))
    # # print(next(next_p))
    # # print(next(next_p))
    # # print(next(next_p))
    # next_p = next_performer(day2_lineup)
    # print(list(next_p))                                     # list of Performer objects created by the generator
    # print(p.name for p in list(next_p))                     # this is just a generator expression inside ()!
    # # print(list(p.name for p in list(next_p)))               # list of Performer names created by the generator expr.

    # Demonstrate JSON encoding/decoding of Lineup objects
    # Single object
    day2_lineup_json = json.dumps(day2_lineup, cls=LineupEncoder, indent=4)
    print(day2_lineup_json)
    d2l = json.loads(day2_lineup_json, object_hook=lineup_json_to_py)
    print(d2l)
    print(day2_lineup)
    # The following line causes # RecursionError: maximum recursion depth exceeded (???);
    # see https://stackoverflow.com/questions/14749225/maximum-recursion-depth-exceeded-when-property-is-applied-to-instance-variab
    # print(d2l == day2_lineup)
    print()

    # List of objects
    performers = [melanie, arloGuthrie]
    day1_lineup = Lineup(*performers, date=date(1969, 8, 15))
    performers = [gratefulDead, jeffersonAirplane, theWho, ccr]
    day2_lineup = Lineup(*performers, date=date(1969, 8, 16))
    performers = [csny, jimiHendrix, theBand]
    day3_lineup = Lineup(*performers, date=date(1969, 8, 17))

    lineups = [day1_lineup, day2_lineup, day3_lineup]
    lineups_json = json.dumps(lineups, cls=LineupEncoder, indent=4)
    print(lineups_json)
    lineups_py = json.loads(lineups_json, object_hook=lineup_json_to_py)
    # print(lineups_py)
    for l in lineups_py:
        print(l)
    print()


