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


def search_result(request):
    if request.method == 'POST':
        faq_search_form = FaqSearchForm(request.POST)
        if faq_search_form.is_valid():
            search_result = faq_search_form.get_search_result()
        types = models.Type.objects.all()
        context = {
            'faq_search_form':faq_search_form,
            'search_result': search_result,
            'types':types,
        }
        return render(request, 'faq/search_result.html', context)
    else:
        redirect('faq')
