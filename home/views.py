from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home/home.html")


def google_custom_search(request):
    return render(request, 'google_custom_search/custom_search.html')
