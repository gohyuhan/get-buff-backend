from enum import Enum


class ChoiceEnum(Enum):
    def __new__(cls, code, message):
        obj = object.__new__(cls)
        obj._value_ = code
        obj.label = message
        return obj