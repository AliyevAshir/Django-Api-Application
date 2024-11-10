# core/tasks.py

from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@shared_task
def send_email_task(subject, message, recipient_list):
    # Render the HTML template
    html_message = render_to_string('emails/email.html', {'subject': subject, 'message': message})
    plain_message = strip_tags(html_message)  # Optional: create a plain text version

    send_mail(
        subject,
        plain_message,  # The plain text version
        'cyberaz191@gmail.com',  # Use your email here
        recipient_list,
        html_message=html_message,  # The HTML version
        fail_silently=False,
    )
