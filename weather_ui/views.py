import datetime  
from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .forms import UserRegistrationForm, CityForm
from django.contrib import messages
from dotenv import dotenv_values
from pathlib import Path
from datetime import datetime
import os
import requests

from django.conf import settings
from plotly.offline import plot
from plotly.graph_objects import Scatter3d, Scatter
import pandas as pd
import json

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
    # print(f'response : {res}')
    return render(request, 'main.html', {'res':res})

def get_current_data():
    try:
        url = f'https://api.openweathermap.org/data/2.5/weather?q=kathmandu&appid={ENV}'
        response = requests.get(url).json()
        return response
    except Exception as e:
        raise HttpResponse({'error': 'something went wrong'})

def get_forecast():
    url = f'https://api.openweathermap.org/data/2.5/forecast?q=kathmandu&appid={FORECAST_ENV}'
    response = requests.get(url).json()
    # print(f'forecast: {response.keys()}')
    # print(f'forecast: {response.values()}')
    # print(f'forecast length: {len(response)}')
    # print(response)
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




def weather_map(request):

    weather_data = None
    default_city = 'kathmandu'
    
    if request.method == 'POST':
        form = CityForm(request.POST)

        if form.is_valid():
            city = form.cleaned_data['city']
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={ENV}&units=metric'
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
                print(f'weather_data: {weather_map}')
    else:
        form = CityForm(initial={'city': default_city})
        url = f'http://api.openweathermap.org/data/2.5/weather?q=kathmandu&appid={ENV}&units=metric'
        res = requests.get(url)
        if res.status_code == 200:
            weather_data = res.json()

    res = get_current_data()
    plot_d =  plot_data()
    return render(request, 'main.html', {
        'form': form,
        'weather_data': weather_data,
        'mapbox_access_token': 'your_mapbox_token',
        'res': res,
        'plot': plot_d
    })

def plot_data():
    
    data = pd.DataFrame(flatten_weather_data())
    plot_div = plot([Scatter(x=data['temperature'], y=data['humidity'])], output_type='div')
    return plot_div



def flatten_weather_data():
    flattened_data = []
    file_path = os.path.join(os.path.dirname(__file__), 'static/data_kathmandu_weather.json')
    with open(file_path, 'r') as d:
      data = json.load(d)

    for item in data:
        # print(item)
        flat_dict = {
            'timestamp': datetime.fromtimestamp(item['timestamp']).strftime('%Y-%m-%d %H:%M:%S'),
            'longitude': item['data']['coord']['lon'],
            'latitude': item['data']['coord']['lat'],
            'weather_id': item['data']['weather'][0]['id'],
            'weather_main': item['data']['weather'][0]['main'],
            'weather_description': item['data']['weather'][0]['description'],
            'temperature': item['data']['main']['temp'],
            'feels_like': item['data']['main']['feels_like'],
            'temp_min': item['data']['main']['temp_min'],
            'temp_max': item['data']['main']['temp_max'],
            'pressure': item['data']['main']['pressure'],
            'humidity': item['data']['main']['humidity'],
            'sea_level': item['data']['main']['sea_level'],
            'ground_level': item['data']['main']['grnd_level'],
            'visibility': item['data']['visibility'],
            'wind_speed': item['data']['wind']['speed'],
            'wind_degree': item['data']['wind']['deg'],
            'clouds_percentage': item['data']['clouds']['all'],
            'country': item['data']['sys']['country'],
            'sunrise': datetime.fromtimestamp(item['data']['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S'),
            'sunset': datetime.fromtimestamp(item['data']['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S'),
            'timezone': item['data']['timezone'],
            'city_id': item['data']['id'],
            'city_name': item['data']['name']
        }
        flattened_data.append(flat_dict)

    return flattened_data