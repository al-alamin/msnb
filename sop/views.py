from django.contrib.auth.models import User
from random import shuffle

from django.shortcuts import render
from django.utils import timezone

from .forms import SOPSubmitForm
# from background_task_list.task import background_print
# from common.models import Author, Category
from common.tasks import add


def sop(request):
    print("\n\n In sop method")

    # background_print(84)
    # background_print.now(5)
    # Category.objects.create(name="new tag from view mehtod")
    
    add.apply_async((4, 5), countdown=5)

    email_success = False
    if request.method == 'POST':
        form = SOPSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            print (type(file))
            # email_success = form.email_SOP(file)
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
