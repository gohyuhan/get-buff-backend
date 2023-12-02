from get_buff.enums import ChoiceEnum


class MuscleGroup(ChoiceEnum):
    ABS = ("ABS", "abs")
    LEGS = ("LEG", "legs")
    CHEST = ("CST", "chest")
    ARMS = ("ARM", "arms")
    BACKnSHOULDER = ("BNS", "back and shoulder")
    NONE = ("NON", "none")