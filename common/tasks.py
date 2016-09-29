from __future__ import absolute_import

from celery import shared_task

from event.models import Registration, Event, SkypeEmail
from common.utils import send_mail


@shared_task
def send_mail_async(subject, body_email, to_email):
    # This is just a helper function to send email async.
    # See the output in the worker process console
    print("\n\n Goint to send email asynconously\n\n")
    return send_mail(subject, body_email, to_email)


@shared_task
def send_skype_email_before_hour(event_id, time, hour=12):
    # Change and updat the body_email make it more customized
    print("\n\nGoing to send email %d hour before " % hour)
    event = Event.objects.get(id=int(event_id))
    # Going to check if this scheduled task has been edited.
    # If the Email is edited then the creation time will be different and this
    # task will simply be skipped then.
    if(event.creation_time != time):
        print("\nThis task has been edited later so this will be skipped")
        return

    registered_user_list = Registration.objects.filter(event=event)
    print(registered_user_list)
    for reg_user in registered_user_list:
        to_email = [reg_user.attendee.email, ]
        subject = "Your event registration Remainder for the event {0}".format(
            event.title)

        body_email = """
                     Hi {0},
                     Your Remainder for the event {1}.
                     The event will be held on {2} Bangladesh time.
                     The event duration is {3} hour/ hours.
                     Our Skype ID is 'MSNB'.
                     For any query please email at support@mystudynotebook.com.
                     Please don't forget to receive video call from our Skype account at the mentioned time.

                     Thanks,
                     Support Team
                     My Study Notebook
                     """.format(reg_user.attendee.first_name, event.title,
                                event.start_time, event.duration)
        send_mail(subject, body_email, to_email)


@shared_task
def send_skype_email_before_mintue(event_id, time, minute=30):
    # Change and updat the body_email make it more customized
    print("\n\nGoing to send email %d mintues before " % minute)
    event = Event.objects.get(id=int(event_id))

    # Going to check if this scheduled task has been edited.
    # If the Email is edited then the creation time will be different and this
    # task will simply be skipped then.
    if(event.creation_time != time):
        print("\nThis task has been edited later,so this will be skipped")
        return

    registered_user_list = Registration.objects.filter(event=event)
    print(registered_user_list)
    for reg_user in registered_user_list:
        to_email = [reg_user.attendee.email, ]
        subject = "Your event registration Remainder for the event {0}".format(
            event.title)
        body_email = """
                     Hi {0},
                     Your Remainder for the event {1}.
                     The event will be held on {2} Bangladesh time.
                     The event duration is {3} hour/ hours.
                     Our Skype ID is 'MSNB'.
                     For any query please email at support@mystudynotebook.com.
                     Please don't forget to receive video call from our Skype account at the mentioned time.

                     Thanks,
                     Support Team
                     My Study Notebook
                     """.format(reg_user.attendee.first_name, event.title,
                                event.start_time, event.duration)
        send_mail(subject, body_email, to_email)


@shared_task
def send_skype_email_after_mintue(event_id, time, minute=30):
    print("\n\nGoing to send email %d mintues after " % minute)
    event = Event.objects.get(id=int(event_id))
    # Going to check if this scheduled task has been edited.
    # If the Email is edited then the creation time will be different and this
    # task will simply be skipped then.
    if(event.creation_time != time):
        print("\nThis task has been edited later,so this will be skipped")
        return

    registered_user_list = Registration.objects.filter(event=event)
    print(registered_user_list)
    for reg_user in registered_user_list:
        to_email = [reg_user.attendee.email, ]
        subject = "Your event registration Remainder for the event {0}".format(
            event.title)
        body_email = """
                     Hi {0},
                     Your Congratulation for the event {1}.
                     The event will be held on {2} Bangladesh time.
                     The event duration is {3} hour/ hours.
                     Our Skype ID is 'MSNB'.
                     For any query please email at support@mystudynotebook.com.
                     Please don't forget to receive video call from our Skype account at the mentioned time.
                     Thanks for Joing our sessiong.
                     Give us your feed back.
                     Thanks,
                     Support Team
                     My Study Notebook
                     """.format(reg_user.attendee.first_name, event.title,
                                event.start_time, event.duration)
        send_mail_async.apply_async(
            (subject, body_email, to_email), countdown=5)


@shared_task
def skype_event_group_email(skype_email_id, time):
    print("\n\n In Skype group Email \n")
    skype_email = SkypeEmail.objects.get(id=skype_email_id)
    # Going to check if this scheduled task has been edited.
    # If the Email is edited then the creation time will be different and this
    # task will simply be skipped then.

    if(skype_email.creation_time != time):
        print(
            "\n This task has been edited later so this is going to be skipped")
        return
    registered_user_list = Registration.objects.filter(event=skype_email.event)
    print(registered_user_list)
    for reg_user in registered_user_list:
        print("\n\n group email for loop\n")
        to_email = [reg_user.attendee.email, ]
        subject = skype_email.email_subject
        body_email = skype_email.email_body
        send_mail_async.apply_async(
            (subject, body_email, to_email), countdown=1)


@shared_task
def add(x=4, y=5):
    print("\n\n****** task add method")
    return x + y


@shared_task
def mul(x, y):
    print("\n\n****** task mul")
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def my_periodic_task():
    print("Just creating a task from admin panel")
