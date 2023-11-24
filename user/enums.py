from get_buff.enums import ChoiceEnum


class TargetStatus(ChoiceEnum):
    LOSS = ("LOS", "loss")
    MAINTAIN = ("MAN", "maintain")
    GAIN = ("GAI", "gain")