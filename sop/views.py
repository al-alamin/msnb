from django.shortcuts import render

# Create your views here.
def sop(request):
    return render(request, 'sop/sop_review.html')