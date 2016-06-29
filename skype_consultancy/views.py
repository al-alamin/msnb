from django.shortcuts import render

# Create your views here.
def skype(request):
    return render(request, 'skype_consultancy/skype_consultancy.html')