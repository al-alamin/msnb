from django.shortcuts import render
from models import models

def faq(request):
    types = models.Type.objects.all().exclude(name='News')
    context = {'types':types}
    return render(request, 'faq/faq.html', context)
