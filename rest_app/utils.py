from django.core.mail import EmailMessage
import os

# Util class to send email

class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['email_body'],
            from_email=os.environ.get('EMAIL_FROM'),
            to=[data['to_email']]
        )
        email.send()

    @staticmethod
    def send_email_with_attachment(data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['email_body'],
            from_email=os.environ.get('EMAIL_FROM'),
            to=[data['to_email']]
        )
        email.attach_file(data['attachment'])
        email.send()