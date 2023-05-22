from abc import ABC

class MalType(ABC):
    def __str__(self):
        pass


class Symbol(MalType):
    ...

class Number(MalType):
    ...

class MalList(MalType):
    def __init__(self) -> None:
        self._content = []

    def append(self, val):
        self._content.append(val)

    def __str__(self):
        str_accumulator = "("
        for val in self._content:
            str_accumulator += val
        str_accumulator += ")"
        return str_accumulator