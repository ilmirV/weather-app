import eel
import pyowm

# city = "New York, USA"

owm = pyowm.OWM("85537b25d59c3b938deccd57727c918d")

@eel.expose
def get_weather(place):
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    temp_max = w.temperature('celsius')['temp_max']
    temp_min = w.temperature('celsius')['temp_min']
    status_short = w.status
    weather_details = [round(temp), round(temp_max), round(temp_min), status_short]
    status_detailed = w.detailed_status
    wind_speed = w.wind()['speed']
    print(status_detailed)
    print(status_short)
    print(temp)
    print(temp_max)
    print(temp_min)
    print(wind_speed)

    return weather_details
    #return "В городе " + place + " сейчас " + str(temp) + " градусов!"

eel.init("web")
eel.start("main.html", size=(700, 700))