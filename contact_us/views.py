from django.shortcuts import render

from .forms import ContactUsForm


def contactus(request):
    success = False

    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            success = contact_form.send_contactus_mail()
    else:
        contact_form = ContactUsForm()

    return render(request, 'contact_us/contact_us.html', {'form': contact_form, 'success': success})
