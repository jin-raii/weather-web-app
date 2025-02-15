from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def test(request):
    return render(request, 'index.html', context={'hello':'there'})

def login(request):
    return render(request, 'uni_form.html')

def index(request):
    context = {
        'city': 'Kathmandu',
        'temperature': 24,
        'feels_like': 22,
        'condition': 'Sunny',
        'humidity': 41,
        'wind_speed': 2,
        'pressure': 997,
        'uv_index': 8,
    }
    return render(request, 'main.html', context=context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'username {username}')
            # messages.add_message('username')
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'form.html', {'form': form})

