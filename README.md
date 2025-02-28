### Deadline FEB 29

# Kathmandu Weather Map

## Description

This web application provides weather information for Kathmandu, Bagmati Province, Nepal by default. It's built using the Django framework and allows users to view current and predicted **weather_description**.


## App Highlights:

*   **Kathmandu Focused (Default):** Weather map starts centered on Kathmandu, Nepal.
*   **Global Weather Search:** Find weather for any location by searching.
*   **Interactive Dropdown Plot:**  Click dropdown to see **temperature/humidity/pressure** over **second** scatter plot.
*   **Real-time Data:** Powered by OpenWeatherAPI for up-to-date weather.
*   **Predicted Weather Description:** LogisticRegression from **scikit-learn** package

## Technologies:

*   Python & Django Backend
*   Django Authentication, Crispy Forms
*   Machine Learning Model (`model.pkl`)
*   HTML, CSS, JavaScript Frontend (Bootstrap)
*   `uv` Package Manager
*   OpenStreetMap (Map Display)
*   OpenWeatherAPI (Weather Data)
*   Ploty Module For Interactive Plot

## Get Started 

**1. Prerequisites:**

*   Python 3.x 
*   uv Package Manager 

**2. Setup Steps:**

```bash
# Clone the repository 
git clone <your_repository_url>
cd <your_weather_app_directory>

# Create a virtual environment using uv
uv venv .weather-web-app

# Activate the environment
source .venv/bin/activate  # Linux/macOS

# Install dependencies using uv sync
uv sync

# Apply database migrations
python manage.py migrate

# Run the development server
python manage.py runserver

**App URLs:**

*   `http://127.0.0.1:8000/home/` - Weather Map (Login Required)
*   `http://127.0.0.1:8000/register/` - Signup
*   `http://127.0.0.1:8000/login/` - Login
*   `http://127.0.0.1:8000/logout/` - Logout
