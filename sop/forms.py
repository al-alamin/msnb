from django import forms
from common.utils import send_mail_to_admin


class SOPSubmitForm(forms.Form):
    attrs = {"class": "form-control", 'required': 'required'}
    name = forms.CharField(max_length=50, label='Name', widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(max_length=30, label='Email', widget=forms.TextInput(attrs=attrs))
    msg = forms.CharField(max_length=500, label='Message', widget=forms.Textarea(attrs=attrs))
    file_attrs = {'required': 'required',
                  'onchange':"this.parentNode.nextSibling.value = this.value",
                  }
    file = forms.FileField(widget=forms.FileInput(attrs=file_attrs))

    def email_SOP(self, file):
        name = self.cleaned_data['name']
        from_email = self.cleaned_data['email']
        msg = self.cleaned_data['msg']
        subject = "{0} submitted a SOP for review".format(name)
        email_success = send_mail_to_admin(subject, msg, from_email, attachmets=file)
        return email_success
