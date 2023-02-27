from enum import Enum


class Stage(Enum):
    qualifying = "квалификация"
    top32 = "1/16"
    top16 = "1/8"
    top8 = "четвертьфинал"
    semifinal = "полуфинал"
    bf3rdp = "заезд за 3 место"
    final = "финал"


class Sponsor:
    def __int__(self, ID: int):
        self.id = id


class Race:
    def __int__(self, stage: Stage, numbers: set[int], start: int, ID: int):
        self.stage = stage
        self.numbers = numbers
        self.start = start


class Competition:
    def __int__(self, name: str, date: str, org_name: str, place: str, races: list[Race]):
        self.name = name
        self.date = date
        self.org_name = org_name
        self.place = place
        self.races = races
