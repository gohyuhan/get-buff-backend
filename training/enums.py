from get_buff.enums import ChoiceEnum

class TrainingLevel(ChoiceEnum):
    BEGINNER = ("BEG","beginner")
    INTERMEDIATE = ("INT","intermediate")
    ADVANCE = ("ADV","advance")
    CUSTOM = ("CUS", "custom")
    NONE = ("NON", "none")


class TrainingType(ChoiceEnum):
    PRESET = ("PRE", "preset")
    CUSTOM = ("CUS", "custom")
    NONE = ("NON", "none")


class CalculatedIn(ChoiceEnum):
    SECONDS=("SEC", "seconds")
    REPS = ("REP", "reps")
    NONE = ("NON", "none")


class TrainingStatus(ChoiceEnum):
    ONGOING = ("ONG", "ongoing")
    COMPLETED = ("COM", "completed")
    GIVEUP = ("GIV", "giveup")
    NONE = ("NON", "none")


class TrainingOrExerciseType(ChoiceEnum):
    TRAINING = ("TRA", "training")
    EXERCISE = ("EXE", "exercise")
    NONE = ("NON", "none")