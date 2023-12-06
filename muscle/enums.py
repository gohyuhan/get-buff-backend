from get_buff.enums import ChoiceEnum


class MuscleGroup(ChoiceEnum):
    ABS = ("ABS", "abs")
    LEGS = ("LEG", "legs")
    CHEST = ("CST", "chest")
    ARMS = ("ARM", "arms")
    BACKNSHOULDER = ("BNS", "back and shoulder")
    CUSTOM = ("CUS", "custom")
    NONE = ("NON", "none")