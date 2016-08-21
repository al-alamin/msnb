from django.core.mail import EmailMessage
from MSNB.settings import ADMIN_EMAILS

PRIMARY_ADMIN_EMAIL = ADMIN_EMAILS[0]
def send_mail(subject, body, to_email=ADMIN_EMAILS, from_email = PRIMARY_ADMIN_EMAIL, bcc=None, attachmets=None):
    email_success = False
    email = EmailMessage(subject, body, from_email, to_email, bcc)
    if attachmets is not None:
        email.attach(attachmets.name, attachmets.read(), attachmets.content_type)
    try:
        email.send()
    except Exception as e:
        print('mail failed' + e.__str__())
    else:
        email_success = True
    return email_success
