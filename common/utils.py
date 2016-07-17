from django.core.mail import EmailMessage


def send_mail_to_admin(subject, body, from_email, bcc=None, attachmets=None):
    email_success = False
    to = ('tareqbuet@gmail.com',)
    email = EmailMessage(subject, body, from_email, to)
    if attachmets is not None:
        email.attach(attachmets.name, attachmets.read(), attachmets.content_type)
    try:
        email.send()
    except:
        print('mail failed')
    else:
        email_success = True
    return email_success
