import logging

from django import forms
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from common.utils import send_mail
from event.models import Registration

logger = logging.getLogger(__name__)

ADMIN_EMAILS = settings.ADMIN_EMAILS


class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['skype_id', ]

    # must be called after cleaning data
    def save_and_mail(self, event, user):
        skype_id = self.cleaned_data['skype_id']
        email_success = False
        try:
            Registration.objects.create(attendee=user, event=event, skype_id=skype_id)
        except:
            reg_success = False
            logger.exception('Registration failed for the user {0} for the event {1}'.format(user,event))
        else:
            reg_success = True
            logger.info('{0} user successfully registered for the event {1}'.format(user, event))
        if reg_success:
            to_email = [user.email, ]
            subject = "Your event registration is confirmed for the event {0}".format(event.title)
            body_email = """
                         Hi {0},
                         Your registration is confirmed for the event {1}.
                         The event will be held on {2} Bangladesh time.
                         The event duration is {3} hour/ hours.
                         Our Skype ID is 'MSNB'.
                         For any query please email at support@mystudynotebook.com.
                         Please don't forget to receive video call from our Skype account at the mentioned time.

                         Thanks,
                         Support Team
                         My Study Notebook
                         """.format(user.first_name, event.title, event.start_time, event.duration)
            email_success = send_mail(subject, body_email, to_email)

        return reg_success, email_success


class EventRegistrationDeleteForm(forms.Form):
    delete = forms.BooleanField(required=False, label='Withdraw My Registration')
    reg_id = forms.IntegerField(widget=forms.HiddenInput())

    def del_registraion(self, user):
        delete = self.cleaned_data['delete']
        id = self.cleaned_data['reg_id']
        del_success = False
        if delete:
            try:
                reg = Registration.objects.get(id=id, attendee=user)
            except ObjectDoesNotExist:
                msg = 'Registration deletion failed for event id {0} and for user {1}'.format(id, user)
                logger.exception(msg)
            else:
                reg.delete()
                del_success = True
                msg = '{0}user registration deleted from the event id {1}'.format(user, id)
                logger.info(msg)

        return del_success
