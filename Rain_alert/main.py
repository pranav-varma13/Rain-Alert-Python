import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "aed8ede121e08bbf91c05d27c774db0d"
account_sid = "ACc0f974bf10a9a35e8af558de39ec54c4"
auth_token = "814f0255ae629e466a0a746a2faadc86"

weather_params = {
    "lat": 23.918566,
    "lon": 76.911324,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint , params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data['list'][0]["weather"][0]["id"])

will_rain = False
for i in weather_data["list"]:
    condition_code = i["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    # print("Bring an Umbrella.")  
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Take an umbrella with you.",
        from_="+15017122661",
        to="+91 96429 33555",
    )
    print(message.status)   

