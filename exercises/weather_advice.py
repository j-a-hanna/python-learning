#weather_advice.py

weather = input("What's the weather like today? (sunny, rainy, snowy, windy): ").lower()

if weather == "sunny":
    print("Don't forget your sunglasses! 😎")
elif weather == "rainy":
    print("Don't forget your umbrella! ☔️")
elif weather == "snowy":
    print("Don't forget to wear warm clothes and boots! ❄️ ")
elif weather == "windy":
    print("Hold onto your hat! 🎩 ")
else:
    print("Hmm, I don't recognize that kind of weather.")
