class Band():
    def __init__(self, name, members=None):
        self.name = name
        self.members = members


# base class
class Musician():
    def __init__(self, name, instrument, solo, member, type):
        self.name = name
        self.instrument = instrument
        self.solo = solo
        self.member = member
        self.type = type

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f"{type} instance. Name = {name}"



class Guitarist(Musician):
    def __init__(self, name, instrument="guitar", solo="face melting guitar solo", type="Guitarist"):
        self.name = name
        self.instrument = instrument
        self.solo = solo
        self.type = type


class Bassist(Musician):
    def __init__(self, name, instrument="bass", solo="bom bom buh bom", type="Bassist"):
        self.name = name
        self.instrument = instrument
        self.solo = solo
        self.type = type


class Drummer(Musician):
    def __init__(self, name, instrument="drums", solo="rattle boom crash", type="Drummer"):
        self.name = name
        self.instrument = instrument
        self.solo = solo
        self.type = type
