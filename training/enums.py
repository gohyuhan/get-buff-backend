from get_buff.enums import ChoiceEnum

class TrainingLevel(ChoiceEnum):
    BEGINNER = ("BEG","beginner")
    INTERMEDIATE = ("INT","intermediate")
    ADVANCED = ("ADV","advanced")


class TrainingType(ChoiceEnum):
    PRESET = ("PRE", "preset")
    CUSTOM = ("CUS", "custom")


class CalculatedIn(ChoiceEnum):
    SECONDS=("SEC", "seconds")
    REPS = ("REP", "reps")


class TrainingStatus(ChoiceEnum):
    ONGOING = ("ONG", "ongoing")
    COMPLETED = ("COM", "completed")
    GIVEUP = ("GIV", "giveup")