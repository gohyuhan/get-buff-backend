import uuid

from django.db import models
from django.contrib.auth import get_user_model

from constance import config

from notifications.tasks import send_email


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    desp = models.TextField()
    subject = models.TextField()


class EmailMessage(models.Model):
    track_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, null=True, blank=True)
    recipient_id = models.IntegerField()
    cc = models.EmailField(null=True, blank=True)
    bcc = models.EmailField(null=True, blank=True)
    subject = models.CharField(max_length=255)
    body_html = models.TextField()
    body_plain = models.TextField()
    callback_id = models.CharField(null=True, blank=True)
    sent = models.DateTimeField(null=True, blank=True)
    delivered = models.DateTimeField(null=True, blank=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def send(self):
        User= get_user_model()
        recipient = User.objects.get(id=self.recipient_id)
        cc = [self.cc] if self.cc else []
        bcc = [self.bcc] if self.bcc else [] 
        send_email.delay(
            email_message_id = self.pk,
            email_from = f"{config.DEFAULT_EMAIL_FROM_NAME}  <{config.DEFAULT_EMAIL_FROM}>",
            email_to = [recipient.email],
            subject = self.subject,
            plain_content = self.body_plain,
            html_content = self.body_html,
            cc=cc,
            bcc=bcc
        )