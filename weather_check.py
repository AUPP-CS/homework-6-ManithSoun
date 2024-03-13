import requests

def get_weather(city):
    api_key = 'e212f3292b421b52d5721a50a9fc0c12'
    endpoint = 'https://api.openweathermap.org/data/2.5/weather?'
    url = f'{endpoint}q={city}&units=metric&appid={api_key}'

    response = requests.get(url).json()

    # city_name = response['name']
    city_name = response['name']

    temp = response['main']['temp']

    feel_like = response['main']['feels_like']
   

    description = response['weather'][0]['description']

    return {
        'temp': round(temp, 2),
        'feel': round(feel_like, 2),
        'description': description,
        'name' : city_name
       
    }
