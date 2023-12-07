from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import EmailMessage


def send_notification_email(template_path, context, event, recipient, cc=None, bcc=None):
    # Process the HTML template with dynamic context
    html_content = render_to_string(template_path, context)

    # Convert HTML to plain text 
    text_content = ' '.join(strip_tags(html_content).split())

    email_message = EmailMessage.objects.create(
        event=event,
        recipient_id=recipient.id, 
        cc=cc,
        bcc=bcc,
        subject=event.subject,
        body_html=html_content,
        body_plain=text_content,
    )
    email_message.send()