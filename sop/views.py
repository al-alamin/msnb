from django.shortcuts import render
from .forms import SOPSubmitForm

# Create your views here.
def sop(request):
    email_success = False
    if request.method=='POST':
        form = SOPSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            print(file.name)
            email_success = form.email_SOP(file)
    else:
        form = SOPSubmitForm()
    return render(request, 'sop/sop_review.html', {'form':form, 'email_success':email_success})