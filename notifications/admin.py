from django.contrib import admin


from .models import EmailMessage, Event
# Register your models here.

admin.site.register(EmailMessage)
admin.site.register(Event)