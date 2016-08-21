from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from common.models import Author, Category
from event.models import Event, Registration
from django.utils.timezone import now
from django.core.exceptions import ObjectDoesNotExist
from .forms import EventRegistrationForm, EventRegistrationDeleteForm


# Create your views here.
def skype(request):
    context = {}
    reg_success = False
    email_success = False
    is_user_registered = False
    form = None
    del_form = None
    events = Event.objects.filter(start_time__gt=now(), category__name='skype_session')
    if events.exists():
        # take the first event ordered by start date. It's the first upcoming event
        event = events.first()
        context['event'] = event
        user = request.user
        # if event does not exist, there should be no registration
        if request.method == 'POST':
            form = EventRegistrationForm(request.POST)
            if form.is_valid():
                reg_success, email_success = form.save_and_mail(user=user, event=event)
        else:
            form = EventRegistrationForm()

        # check if the current user is registered for this event
        if not user.is_anonymous():
            try:
                reg = Registration.objects.get(event=event, attendee=user)
            except ObjectDoesNotExist:
                is_user_registered = False
            else:
                is_user_registered = True
                initialdict = {'reg_id': reg.id}
                del_form = EventRegistrationDeleteForm(initialdict)

    context['reg_success'] = reg_success
    context['email_success'] = email_success
    context['is_user_registered'] = is_user_registered
    context['form'] = form
    context['del_form'] = del_form

    return render(request, 'skype_consultancy/skype_consultancy.html', context)


@login_required
def delete_skype_registration(request):
    del_success = False
    if request.method == 'POST':
        form = EventRegistrationDeleteForm(request.POST)
        user = request.user
        if form.is_valid():
            del_success = form.del_registraion(user)

    print('del_success', del_success)
    return redirect('/skype/')
