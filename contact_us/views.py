from django.core import mail
from django.shortcuts import render

from .forms import ContactUsForm


# Create your views here.
def contactus(request):
    success = False

    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            subject = "{0} from My Study Notebook wants to contact you".format(name)
            msg = contact_form.cleaned_data['msg']
            from_email = contact_form.cleaned_data['email']
            to_email = ('support@whitecanvassoft.com',)  # must be a list or tuple
            try:
                mail.send_mail(subject, msg, from_email, to_email, fail_silently=False)
            except Exception as ex:
                # print(type(ex).__name__, ex.args)
                pass
            else:
                success = True

    else:
        contact_form = ContactUsForm()

    return render(request, 'contact_us/contact_us.html', {'form': contact_form, 'success': success})
