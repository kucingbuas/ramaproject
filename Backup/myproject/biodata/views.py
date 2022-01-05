from django.shortcuts import render
from .form import CustomerForm

# Create your views here.
def biodata(request):

    form = CustomerForm()
    
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

    template_name = "biodata.html"
    context = {
        'title':'biodata',
        'form' : form,
    }
    return render(request, template_name, context)