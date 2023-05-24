import requests
from twilio.rest import Client
api_key = "74999d3770957deb65cc902cd2d899d7"
end_url = "https://api.openweathermap.org/data/2.8/onecall"
account_ssid = "ACd9fb3b717abd8f9e0f4741407e9575b2"
acct_token ="8b22d8303fa7a139b4f4ffaa29a66d42"
parameters = {
    "lon": 77.481400,
    "lat": 20.491600,
    "appid": api_key,
    "exclude" : "current,minutely,daily"
}

response  = requests.get(url= "https://api.openweathermap.org/data/2.8/onecall" , params= parameters)
response.raise_for_status()
rain = False
weather_data = response.json()
hourly_data = weather_data["hourly"]
for data in hourly_data[:13]:
    id_code = data["weather"][0]["id"]

    if id_code < 700:
       rain = True

if rain:
    client = Client(account_ssid, acct_token)
    message = client.messages.create(
        body="it's going to be rain today, remember to bring an umbrella.",
        from_="+13204139003",
        to="+818097708193"
    )
    print(message.status)

