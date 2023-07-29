import requests
from twilio.rest import Client

"""" Weatherapi.com API"""

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"
api_key = 'f7b7caf5d7msh43c4c4e6af4444bp167b3fjsn39481196c6c8'
account_sid = 'AC4f866743f5aa85469dbb9ea2bfba7283'
auth_token = 'ca298b441141cead3a8d843ae55c5344'
LAT = '43.222015'
LON = '76.851250'

querystring = {"q": "Almaty", "days": "1"}

headers = {
    "X-RapidAPI-Key": f"{api_key}",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data['forecast']['forecastday'][0]['hour'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['condition']['code']
    if condition_code > 1030:
        will_rain = True
        print("You will need an umbrella")

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='+17624659325',
        body="It's going to rain today. Bring an umbrella!",
        to='+77072690628'
    )

    print(message.status)

""" ------------------------- OpenWeather API -------------------------"""

# OEW = 'https://api.openweathermap.org/data/2.5/forecast'
# weather_params = {
#     "lat": 43.222015,
#     'lon': 76.851250,
#     'appid': '5cab9285339c43731ab4d98128b53b00'
# }
#
# response = requests.get(OEW, params=weather_params)
# response.raise_for_status()
# weather_data = response.json()
# weather_slice = weather_data
# print(weather_slice)
