import datetime  
from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .forms import UserRegistrationForm
from django.contrib import messages
from dotenv import dotenv_values
from pathlib import Path
from datetime import datetime
import os
import requests

# ENV = dotenv_values(Path('../.env'))
# print(f'env file {ENV["WEATHER_API_KEY"]}')
ENV = os.environ.get('WEATHER_API_KEY')
FORECAST_ENV = os.environ.get('WEATHER_FORECAST_API_KEY')
# Create your views here.
def test(request):
    return render(request, 'index.html', context={'hello':'there'})

def login(request):
    return render(request, 'login.html')

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

def weather_dashboard(request):
    context = {
        'current_weather': {
            'city': 'Kathmandu',
            'temperature': 24,
            'feels_like': 22,
            'condition': 'Sunny',
            'humidity': 41,
            'wind_speed': 2,
            'pressure': 997,
            'uv_index': 8,
            # 'timezone': pytz.timezone('Asia/kathmandu'),
            'timezone':'timezone',
            # 'current_time': datetime.now(pytz.timezone('Asia/kathmandu')),
            'current_time': datetime.now(),
            'sunrise': '06:37 AM',
            'sunset': '20:37 PM'
        },
        'daily_forecast': [
            {'day': 'Friday, 1 Sep', 'temp': 20, 'condition': 'Cloudy'},
            {'day': 'Saturday, 2 Sep', 'temp': 22, 'condition': 'Cloudy'},
            {'day': 'Sunday, 3 Sep', 'temp': 27, 'condition': 'Sunny'},
            {'day': 'Monday, 4 Sep', 'temp': 18, 'condition': 'Rain'},
            {'day': 'Tuesday, 5 Sep', 'temp': 16, 'condition': 'Rain'}
        ],
        'hourly_forecast': [
            {'time': '12:00', 'temp': 26, 'condition': 'Sunny', 'wind': 3},
            {'time': '15:00', 'temp': 27, 'condition': 'Sunny', 'wind': 2},
            {'time': '18:00', 'temp': 27, 'condition': 'Cloudy', 'wind': 3},
            {'time': '21:00', 'temp': 25, 'condition': 'Cloudy', 'wind': 3},
            {'time': '00:00', 'temp': 22, 'condition': 'Clear', 'wind': 3}
        ]
    }
    res = get_current_data()
    get_forecast()
    print(f'response : {res}')
    return render(request, 'main.html', {'res':res})

def get_current_data():
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q=kathmandu&appid={ENV}'
    response = requests.get(url).json()
    return response

def get_forecast():
    print('forecast api key', FORECAST_ENV)
    url = f'https://api.openweathermap.org/data/2.5/forecast/daily?q=kathmandu&cnt=1&appid={FORECAST_ENV}'
    response = requests.get(url).json()
    print(f'forecast: {response}')
    return response

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Created account now you can login {username}')
            # messages.add_message('username')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'form.html', {'form': form})

