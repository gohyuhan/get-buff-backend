from django.contrib import admin

from account.models import (
    User,
    SecurityToken,
)


# Register your models here.
admin.site.register(User)
admin.site.register(SecurityToken)