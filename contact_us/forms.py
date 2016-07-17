from django import forms


class ContactUsForm(forms.Form):
    attrs = {"class": "form-control",'required':'required'}
    name = forms.CharField(max_length=50, label='Name',widget=forms.TextInput(attrs=attrs))
    email = forms.EmailField(max_length=30, label='Email',widget=forms.TextInput(attrs=attrs))
    msg = forms.CharField(max_length=500, label='Message',widget=forms.Textarea(attrs=attrs))
