from django import forms
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from common.utils import send_mail
from event.models import Registration

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
        else:
            reg_success = True
        if reg_success:
            to_email = ADMIN_EMAILS + [user.email, ]
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
        print('id', id)
        del_success = False
        if delete:
            try:
                reg = Registration.objects.get(id=id, attendee=user)
            except ObjectDoesNotExist:
                print('does not exist')
            else:
                reg.delete()
                del_success = True

        return del_success
