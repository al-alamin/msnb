from django.contrib.auth.models import User
from random import shuffle

from django.shortcuts import render

from .forms import SOPSubmitForm


def sop(request):
    email_success = False
    if request.method == 'POST':
        form = SOPSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            email_success = form.email_SOP(file)
    else:
        form = SOPSubmitForm()
    reviewers = User.objects.filter(groups__name='Reviewer').distinct()
    # show reviewers in random
    reviewers = list(reviewers)  # for shuffling purpose
    shuffle(reviewers)

    context = {'form': form,
               'email_success': email_success,
               'reviewers': reviewers}
    return render(request, 'sop/sop_review.html', context)
