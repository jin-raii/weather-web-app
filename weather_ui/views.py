from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def test(request):
    return render(request, 'index.html', context={'hello':'there'})

def login(request):
    return render(request, 'uni_form.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.add_message('username')
            return redirect('')
    else:
        form = UserCreationForm()

    return render(request, 'form.html', {'form': form})

