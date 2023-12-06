from get_buff.enums import ChoiceEnum

class SpecialTargetType(ChoiceEnum):
    """
    streak - to track about a continuous action 
    """
    STREAK = ("STK", "streak")
    ALL = ("ALL","all other badge obtain")
    NONE = ("NON", "none")
    

class TargetCountType(ChoiceEnum):
    COUNT= ("CON", "count")
    DAYS = ("DYS", "days")
    WEEKS= ("WKS", "weeks")
    MONTHS = ("MNS", "months")
    YEARS = ("YRS", "years")
    NONE = ("NON", "none")
    