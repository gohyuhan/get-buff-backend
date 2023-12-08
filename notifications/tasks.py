import importlib
from datetime import datetime

from django.core.mail import EmailMultiAlternatives
from django.utils import timezone

from celery import shared_task
from premailer import transform


@shared_task(bind=True)
def send_email(
    self,
    email_message_id,
    email_from = None,
    email_to = frozenset(),
    subject = None,
    plain_content = None,
    html_content = None,
    cc=frozenset(),
    bcc=frozenset()
):
    notifications_models= importlib.import_module("notifications.models")
    email_model = getattr(
        notifications_models, "EmailMessage"
    )
    try:
        email = email_model.objects.get(pk = email_message_id)
    except email_model.DoesNotExist as e:
        raise self.retry(exc = e, countdown = 10, max_retries =2)
    
    html_content = transform(html_content)
    msg = EmailMultiAlternatives(
        subject,plain_content,email_from,email_to,cc=cc,bcc=bcc
    )
    msg.mixed_subtype = 'related'
    msg.attach_alternative(html_content,'text/html')

    msg.send()
    try:
        email.callback_id = msg.anymail_status.message_id
    except AttributeError:
        pass
    email.sent = timezone.now()
    email.save()

    