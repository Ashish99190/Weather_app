import requests
from twilio.rest import Client
api_key = "your_key"
end_url = "https://api.openweathermap.org/data/2.8/onecall"
account_ssid = "yout_id"
acct_token ="your_token"
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
        from_="your_no",
        to="+818097708193"
    )
    print(message.status)

