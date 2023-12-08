from get_buff.enums import ChoiceEnum


class AccountEmailStatus(ChoiceEnum):
    DISABLED = ('DIS','disabled')
    ACTIVE= ('ACT','active')
    PENDING = ('PEN','pending')
    REVERIFY = ('REV', 'rverification pending')


class SecurityTokenEventType(ChoiceEnum):
    EMAIL_VERIFICATION = ('EVE','email verification')
    PASSWORD_RESET= ('PRE','password reset')
    NONE = ('NON', 'none')