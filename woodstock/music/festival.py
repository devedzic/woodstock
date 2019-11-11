"""The class representing the concept of a festival.
"""


from datetime import date
import sys
from pickle import dump, load

from woodstock.music.performer import *
from woodstock.music.lineup import *
from woodstock.util.utility import *


class Festival:
    """The class describing the concept of a festival.
    It includes a name, a list of Lineup objects (lineups by date), location and the start and end dates.
    """

    def __init__(self, name, location, start, end, *lineups):
        if start > end:
            raise FestivalStartDateException(start, end)
        elif not all([check_lineup_date(lineup, start, end) for lineup in lineups]):
            wrong_date_lineups = [lineup for lineup in lineups if not check_lineup_date(lineup, start, end)]
            raise LineupDateException(wrong_date_lineups[0], start, end)
        else:
            self.name = name if name and isinstance(name, str) else 'unknown'
            self.location = location if location and isinstance(location, str) else 'unknown'
            self.start = start if start and isinstance(start, date) else 'unknown'
            self.end = end if end and isinstance(end, date) else 'unknown'
            self.lineups = lineups if lineups and all([isinstance(lineup, Lineup) for lineup in lineups]) else 'unknown'

    def __str__(self):
        lineups = '\n\t'.join(str(lineup) for lineup in self.lineups)
        return f'{self.name} ({format_date(self.start)} - {format_date(self.end)})' + '\n\t' + lineups


class FestivalError(Exception):
    """Base class for exceptions in this module.
    """

    pass


class FestivalStartDateException(FestivalError):
    """Exception raised when a the tart date of a festival lineup is not between start and end dates of the festival.
    """

    def __init__(self, start, end):
        self.message = f'festival start date ({start}) after festival end date ({end}).'


def check_lineup_date(lineup, start_date, end_date):
    """Checks if lineup.date is between start_date and end_date."""

    return start_date <= lineup.date <= end_date


class LineupDateException(FestivalError):
    """Exception raised when the date of a festival lineup is not between start and end dates of the festival.
    """

    def __init__(self, lineup, start, end):
        self.message = f'lineup date ({format_date(lineup.date)}) not between start and end dates of the festival ' \
                       f'({format_date(start)} - {format_date(end)}).'


if __name__ == "__main__":

    # pass

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

    day1_performers = [melanie, arloGuthrie]
    day1_lineup = Lineup(*day1_performers, date=date(1969, 8, 15))
    day2_performers = [gratefulDead, jeffersonAirplane, theWho, ccr]
    day2_lineup = Lineup(*day2_performers, date=date(1969, 8, 16))
    day3_performers = [csny, jimiHendrix, theBand]
    day3_lineup = Lineup(*day3_performers, date=date(1969, 8, 17))

    # print(day3_lineup)                                                  # just testing

    lineups = [day1_lineup, day2_lineup, day3_lineup]
    woodstock = Festival('Woodstock', 'Bethel (NY)', date(1969, 8, 15), date(1969, 8, 17), *lineups)
    print(woodstock)

    # Demonstrate exceptions
    # Here's the hierarchy of built-in exceptions: https://docs.python.org/3/library/exceptions.html#exception-hierarchy

    # Demonstrate exceptions - the general structure of try-except statements, possibly including else and finally
    p = ['Grateful Deat', 'Jefferson Airplane', 'Jimi Hendrix', 'The Band']
    # print(p[4])                 # raises IndexError
    try:
        print(p[3])
        # print(p / 0)
        print(p[4])
    # except:
    #     print('Caught an exception...')
    except IndexError:
        print('Caught an IndexError')
    except:
        print('Caught an exception...')
    else:
        print('This is the else clause (the try block has completed normally).')
    finally:
        print('After the code in the try block has completed normally, or after an except clause has been activated.')
    print()

    # Demonstrate exceptions - except: <exception> as <name> (and then type(name), <name>.args,...)
    try:
        print(p[4])
    except Exception as e:
        print('Caught an exception:', e)
        print('Caught an exception:', type(e))                  # get the exception type
        print('Caught an exception:', e.__class__.__name__)     # get the exception type name
        print('Caught an exception:', e.args)                   # get the exception type name and other attributes
    print()

    # Demonstrate exceptions - user-defined exceptions (wrong festival date(s), wrong lineup date)
    # try:
    #     woodstock = Festival('Woodstock', 'Bethel (NY)', date(1969, 8, 18), date(1969, 8, 17), *lineups)
    # except FestivalStartDateException as e:
    #     # print(f'Caught {e.__class__.__name__}: ' + e.message)
    #     sys.stderr.write(f'Caught {e.__class__.__name__}: ' + e.message + '\n')
    #     raise
    # # print(woodstock)
    # print()

    # try:
    #     # woodstock = Festival('Woodstock', 'Bethel (NY)', date(1969, 8, 18), date(1969, 8, 17), *lineups)
    #     day3_lineup = Lineup(*day3_performers, date=date(1969, 8, 11))
    #     lineups = [day1_lineup, day2_lineup, day3_lineup]
    #     woodstock = Festival('Woodstock', 'Bethel (NY)', date(1969, 8, 15), date(1969, 8, 17), *lineups)
    # except LineupDateException as e:
    #     # print(f'Caught {e.__class__.__name__}: ' + e.message)
    #     sys.stderr.write(f'Caught {e.__class__.__name__}: ' + e.message + '\n')
    #     raise
    # # print(woodstock)
    # print()

    # # Demonstrate writing to a text file
    # with open('performers.txt', 'w') as out:
    #     # for performer in day2_performers:
    #     #     out.write(str(performer) + '\n')
    #     out.writelines([str(performer) + '\n' for performer in day2_performers])
    # print()

    # # Demonstrate reading from a text file
    # p = []
    # with open('performers.txt', 'r') as f:
    #     # p = f.read()
    #     # print(p)
    #     while True:
    #         p_str = f.readline()
    #         if p_str:
    #             p.append(Performer.from_str(p_str))
    #         else:
    #             break
    #     for performer in p:
    #         print(performer)
    # print()

    # # Demonstrate writing to a binary file - pickle.dump() and <f>.write()/<f>.writelines() with str.encode(<obj>)
    # with open('performers', 'wb') as out:
    #     dump(day2_performers, out)
    # print()
    # with open('performers', 'wb') as out:
    #     # for performer in day2_performers:
    #     #     out.write(str.encode(str(performer) + '\n'))
    #     out.writelines([str.encode(str(performer) + '\n') for performer in day2_performers])
    # print()

    # # Demonstrate reading from a binary file - pickle.load() and <f>.read().decode()/<f>.readlines().decode()
    # with open('performers', 'rb') as f:
    #     d2_performers = load(f)
    #     for performer in d2_performers:
    #         print(performer)
    # print()
    # with open('performers', 'rb') as f:
    #     p = f.read().decode()
    #     print(p)
    # print()

    # Demonstrate get_project_dir(), get_data_dir() and writing/reading to/from files in data dir
    # day1_lineup_text = ''
    # for p in day1_lineup.performers:
    #     day1_lineup_text += str(p) + '\n'
    # f = get_data_dir() / 'day1_lineup.txt'
    # f.write_text(day1_lineup_text)
    # print()
    f = get_data_dir() / 'day1_lineup.txt'
    d2_lineup_text = f.read_text()
    print(d2_lineup_text)



