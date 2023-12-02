from django.core.exceptions import ValidationError

class PasswordStrengthValidator(object):
    """
    Password Strength Validators
    - minimum 8 char
    should at least contain 1 upper, l lower and 1 number
    """

    def validate(password, user=None):
        error_msg = "Password Must Contain min. 8 chars with at least 1 lowercase, 1 uppercase and 1 number"
        if len(password) < 8:
            raise ValidationError(error_msg)
        if not any (c.isalpha() for c in password):
             raise ValidationError(error_msg)
        if not any (c.isdigit() for c in password):
             raise ValidationError(error_msg)
        if not any (c.islower() for c in password):
             raise ValidationError(error_msg)
        if not any (c.isupper() for c in password):
             raise ValidationError(error_msg)
        

class UserPasswordvalidator(object):
     
     def validate(password, user):
          check_user_password(password, user, "Invalid user/password")


class OldPasswordvalidator(object):
     
     def validate(password, user):
          check_user_password(password, user, "Invalid old password")


def check_user_password(password, user, error_msg):
     if not user.check_password(password):
          raise ValidationError(error_msg)