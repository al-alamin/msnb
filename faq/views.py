from django.shortcuts import render, redirect
from models import models
from .forms import FaqSearchForm


def faq(request):
    types = models.Type.objects.all().exclude(name='News')
    recent_q = models.Question.objects.all().order_by('date')[:20]
    faq_search_form = FaqSearchForm()
    context = {'types': types,
               'recent_q': recent_q,
               'faq_search_form': faq_search_form,
               }
    return render(request, 'faq/faq.html', context)


def search_result(request, cat=None, tag=None):
    types = models.Type.objects.all().exclude(name='News')
    faq_search_form = FaqSearchForm()
    if request.method == 'POST':
        faq_search_form = FaqSearchForm(request.POST)
        if faq_search_form.is_valid():
            search_result = faq_search_form.get_search_result()

    elif cat is not None:
        search_result = models.Question.objects.filter(category__name__iexact=cat)
    elif tag is not None:
        search_result = models.Question.objects.filter(tag__name__iexact=tag)
    else:
        redirect('faq')

    context = {
        'faq_search_form': faq_search_form,
        'search_result': search_result,
        'types': types,
    }
    return render(request, 'faq/search_result.html', context)
