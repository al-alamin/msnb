from django.shortcuts import render
from .forms import SOPSubmitForm
from models.models import Author
from random import shuffle


def sop(request):
    email_success = False
    if request.method == 'POST':
        form = SOPSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            email_success = form.email_SOP(file)
    else:
        form = SOPSubmitForm()
    reviewers = Author.objects.filter(role__role='Reviewer').distinct()
    reviewers = list(reviewers)  # for shuffling purpose
    shuffle(reviewers)

    context = {'form': form,
               'email_success': email_success,
               'reviewers':reviewers}
    return render(request, 'sop/sop_review.html',context )
