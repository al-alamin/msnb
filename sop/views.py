from random import shuffle

from django.shortcuts import render
from django.utils import timezone

from .forms import SOPSubmitForm
from background_task_list.task import background_print
from common.models import Author, Category
from .tasks import add


def sop(request):
    print("\n\n In sop method")

    # background_print(84)
    # background_print.now(5)
    # Category.objects.create(name="new tag from view mehtod")
    
    # add.apply_async((4, 5), countdown=10)

    email_success = False
    if request.method == 'POST':
        form = SOPSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            print (type(file))
            # email_success = form.email_SOP(file)
    else:
        form = SOPSubmitForm()
    reviewers = Author.objects.filter(role__role='Reviewer').distinct()
    # show reviewers in random
    reviewers = list(reviewers)  # for shuffling purpose
    shuffle(reviewers)

    context = {'form': form,
               'email_success': email_success,
               'reviewers': reviewers}
    return render(request, 'sop/sop_review.html', context)
