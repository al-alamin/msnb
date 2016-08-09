from random import shuffle

from django.shortcuts import render

from common.models import Author


# Create your views here.
def home(request):
    advisors_roles = ['Advisor','Reviewer','Presenter']
    advisors = Author.objects.filter(role__role__in=advisors_roles).distinct()
    advisors = (list(advisors))  # to make it shuffleable
    shuffle(advisors)  # in-place shuffling
    return render(request, "home/home.html", {'advisors':advisors})


def google_custom_search(request):
    return render(request, 'google_custom_search/custom_search.html')
