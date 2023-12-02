from get_buff.enums import ChoiceEnum

class SpecialTargetType(ChoiceEnum):
    RECIPE= ("REC", "recipe")
    MEMBERSHIP = ("MEM", "membership")
    STREAK = ("STK", "streak")
    NONE = ("NON", "none")
    

class SpecialTargetCountType(ChoiceEnum):
    COUNT= ("CON", "count")
    DAYS = ("DYS", "days")
    WEEKS= ("WKS", "weeks")
    MONTHS = ("MNS", "months")
    YEARS = ("YRS", "years")
    NONE = ("NON", "none")
    