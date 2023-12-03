from get_buff.enums import ChoiceEnum

class SpecialTargetType(ChoiceEnum):
    """
    membership - to track about membership (user pay to upgrade to a non free tier) ( not appliable now )
    streak - to track about a continuous action 
    weight - to track about user weight gain/loss 
    """
    MEMBERSHIP = ("MEM", "membership")
    STREAK = ("STK", "streak")
    WEIGHT = ("WEIGHT", "weight")
    NONE = ("NON", "none")
    

class TargetCountType(ChoiceEnum):
    COUNT= ("CON", "count")
    DAYS = ("DYS", "days")
    WEEKS= ("WKS", "weeks")
    MONTHS = ("MNS", "months")
    YEARS = ("YRS", "years")
    NONE = ("NON", "none")
    

class SpecialTargetAction(ChoiceEnum):
    """
    paid - track the paid action (user pay to upgrade to a non free tier) ( not appliable now )
    loss - user loss target weight successfully
    gain - user gain target weight successfully
    """
    PAID = ("PAI", "paid")
    LOSS = ("LOS", "loss")
    GAIN = ("GAI", "gain")
    NONE = ("NON", "none")