def display_weather(data):
    print(data)

    city = data['name']
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    feels_like = data['main']['feels_like']
    sunrise = data['main']['sunrise']
    sunset = data['main']['sunset']


    print(f"Weather in : {city}")
    print(f"Temperature : {temp}")
    print(f"Condition : {description}")
    print(f"Humidity :{humidity}")
    print(f"Feels like :{feels_like}")
    print(f"Sunset : {sunset}")
    print(f"Sunrise :{sunset}")
    

