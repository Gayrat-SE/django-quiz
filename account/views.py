from django.shortcuts import render, redirect

from .forms import ContactCreateForm

def index(request):

    if request.POST:
        form = ContactCreateForm(request.POST)

        if form.is_valid():
            form = form.save()

            return render(request, 'quizes/main.html')

    return render(request, 'index.html')