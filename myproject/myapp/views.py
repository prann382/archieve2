from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MyForm
from .models import FormData

def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Save form data to the database
            FormData.objects.create(name=name, email=email, message=message)
            # Redirect to a success page or keep it as it is for the same page
            return HttpResponseRedirect(request.path_info)  # Redirect to the current URL
    else:
        form = MyForm()
    return render(request, 'myapp/my_template.html', {'form': form})
