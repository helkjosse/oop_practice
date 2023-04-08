from abc import ABC, abstractmethod


class Robot:
    code: str
    name: str
    __instance = None

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(Robot, cls).__new__(cls)
        return cls.__instance


class Building(ABC):

    @abstractmethod
    def __init__(self) -> None:
        self.floors = 1


class House(Building):

    def __init__(self, floors: int = 1) -> None:
        super().__init__()
        self.floors = floors


class Barn(Building):

    def __init__(self) -> None:
        super().__init__()
