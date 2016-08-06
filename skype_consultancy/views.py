from django.shortcuts import render
from models.models import Author

# Create your views here.
def skype(request):
    next_presenter = Author.objects.get(id=2)
    context = {'next_presenter':next_presenter}
    return render(request, 'skype_consultancy/skype_consultancy.html',context)