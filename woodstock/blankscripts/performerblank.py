"""Domain classes and functions related to the concept of performer
"""


from woodstock.util import utility
from woodstock.music.enums import Vocals, Instrumet
import json


class Performer:
    """The class describing the concept of performer.
    It is assumed that a performer is sufficiently described by their
    name and whether they are a solo performer or a band.

    Illustrates some of the important concepts of Python classes:
    - self
    - __init__()
    - __str__()
    - __eq__(self, other) is the equivalent of Java equals() and should be overridden in classes
    - data fields (instance variables)
    - methods - calling them by self.<method>(...) from the same class where they are defined
    """

    def __init__(self, name, is_band=True):
        pass
        # self.__n = 'lll'                                    # 'private' field

    # Properties: 'private' fields; run setters and getters in the debugger.
    # Make name a property (after setting up __init__(), __str__(), __eq__(), methods,...).

    # Add an immutable property (no setter for it)

    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    def play(self, song_title, *args, **kwargs):
        """Assumes that song_title, *args (expressions of gratitude) and kwargs.values() (messages) are strings.
        Prints song_title, expressions of gratitude and messages. A call example:
            <performer>.play(song_title, *['Thank you!', 'You're wonderful!], love='We love you!')
        """

        pass

    def play_song(self, song_title, *args, **kwargs):
        """Demonstrates calling another method feom the same class (self.<method>(...) as a mandatory syntax).
        """

    # Alternative constructor
    @classmethod
    def from_str(cls, performer_string):
        """Inverted __str__() method.
        Assumes that performer_string is in the format generated by __str__().
        """

        pass


class PerformerEncoder(json.JSONEncoder):
    """JSON encoder for Performer objects.
    """

    def default(self, o):
        # recommendation: always use double quotes with JSON

        pass


def performer_json_to_py(performer_json):
    """JSON decoder for Performer objects (object_hook parameter in json.loads()).
    """


class Singer(Performer):
    """The class describing the concept of singer.
    It is assumed that a singer is sufficiently described as a Performer,
    with the addition of whether they are a lead or a background singer.
    """

    # Version 1 - no multiple inheritance

    # Version 2 - with multiple inheritance

    def play(self, song_title, *args, **kwargs):
        """Overrides the play() method from superclass.
        Assumes that song_title, *args (expressions of gratitude) and kwargs.values() (messages) are strings.
        Prints song_title, expressions of gratitude and messages. A call example:
            <singer>.play(song_title, *['Thank you!', 'You're wonderful!], love='We love you!')
        """


class Songwriter(Performer):
    """The class describing the concept of songwriter.
    It is assumed that a songwriter is sufficiently described as a Performer
    who writes songs and plays an instrument.
    """

    # Version 1 - no multiple inheritance

    # Version 2 - with multiple inheritance

    def what_do_you_do(self):
        """Just a simple method to describe the concept of songwriter.
        """


class SingerSongwriter(Singer, Songwriter):
    """The class describing the concept of singer-songwriter.
    It is assumed that a singer-songwriter is sufficiently described as a Singer who is simultaneously a Songwriter.
    """


if __name__ == "__main__":

    pass

    # Data

    # # Some of the Woodstock performers, Aug 15-16, 1969
    # melanie = Performer('Melanie', is_band=False)
    # arloGuthrie = Performer('Arlo Guthrie', is_band=False)
    # # Some of the Woodstock performers, Aug 16-17, 1969
    # gratefulDead = Performer('Grateful Dead', is_band=True)
    # jeffersonAirplane = Performer('Jefferson Airplane', is_band=True)
    # theWho = Performer('The Who', is_band=True)
    # ccr = Performer('Creedence Clearwater Revival', is_band=True)
    # # Some of the Woodstock performers, Aug 17-18, 1969
    # csny = Performer('Crosby, Stills, Nash and Young', is_band=True)
    # jimiHendrix = Performer('Jimi Hendrix', is_band=False)
    # theBand = Performer('The Band', is_band=True)

    # Print objects
    print()

    # Compare objects
    print()

    # Access data fields (instance variables), including 'private' fields
    print()

    # Add new data fields (instance variables)
    #   1. <object>.<new_attr> = <value>
    #   2. <object>.__setattr__('<new_attr>', <value>)      # counterpart: <object>.__getattribute__('<attr>')
    #   3. setattr(<object>, '<new_attr>', <value>))        # counterpart: getattr(<object>, '<attr>')
    print()

    # Calling methods
    print()

    # Demonstrate object data fields and methods in Python Console for some built-in classes (boolean, int, object,...)
    # - True + 1
    # - True.__int__()
    # - (1).__class__.__name__
    # - (1).__class__
    # - o.__dir__()
    # - o.__dir__

    # Demonstrate object data fields and methods in Python Console for Performer objects
    print()

    # Demonstrate @classmethod (from_str())
    print()

    # Demonstrate inheritance
    # object class (like the Object class in Java; all classes inherit from object
    #   try, e.g., list.__mro__ in the console)
    #   object class defines object.__eq__(self, other) etc.
    #   object.__ne__(self, other), the inverse of object.__eq__(self, other),
    #   is provided by Python automatically once object.__eq__(self, other) is implemented
    print()

    # Demonstrate method overriding
    print()

    # Demonstrate multiple inheritance and MRO.
    # Make sure to read this first: https://stackoverflow.com/a/50465583/1899061 (especially Scenario 3).
    print()

    # Demonstrate JSON encoding/decoding of Performer objects
    # Single object
    print()

    # List of objects
    print()

