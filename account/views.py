from django.shortcuts import render, redirect
# from quizes.views import QuizListView
from .forms import ContactCreateForm

def index(request):

    if request.POST:
        form = ContactCreateForm(request.POST)

        if form.is_valid():
            form.save()
            print(11111111111111)

            return redirect('quiz_list_view')

    return render(request, 'index.html')