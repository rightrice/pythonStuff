## ai weather
## created by rightrice

from pyowm import OWM
from geopy import Nominatim
from datetime import datetime

class weather():
    #default location is Manhattan, NY USA
    __location = "Manhattan, NY"
    api_key = "INSERT API HERE"

    def __init__(self):
        self.ow = OWM(self.api_key)
        self.mgr = self.ow.weather_manager()
        locator = Nominatim(user_agent="rightrice location")
        city = "Manhattan"
        country = "US"
        self.location = city + ", " + country
        loc = locator.geocode(self.__location)
        self.lat = loc.latitude
        self.long = loc.longitude
    
    @property
    def weather(self):
        forecast = self.mgr.one_call(lat=self.lat, lon=self.long)
        return forecast

    def forecast(self):
        forecast = self.mgr.one_call(lat=self.lat, long=self.long)
        detail_status = forecast.forecast_hourly[0].detailed_status
        pressure = forecast.forecast_hourly[0].pressure.get['press']
        humidity = forecast.forecast_hourly[0].humidity
        sunrise = datetime.utcfromtimestamp(forecast.forecast_hourly[0].sunrise()).strftime("%H:%M:%S")
        sunset = datetime.utcfromtimestamp(forecast.forecast_hourly[0].sunset()).strftime("%H:%M:%S")
        temperature = forecast.forecast_daily[0].tempurature('farenheit').get('day')
        uvi = forecast.forecast_forecast[0].uvi

        print('detailed status: ', detail_status)
        print('pressure: ', pressure)
        print('humidity: ', humidity)
        print('tempurature: ', temperature)
        print('sunrise: ', sunrise)
        print('sunset: ', sunset)
        print('uvi: ', uvi)
        
        message = "Today's weather forecast for Manhattan, NY USA." \
                + "Today will be mostly " + detail_status + "." \
                + "Pressure today will be " + pressure + "millibars." \
                + "The humidity today is going to be " + humidity + "%." \
                + "Today's tempurature will be " + temperature + "farenheit." \
                + "The sunrise:" + sunrise + "AM EST." \
                + "The sunset: " + sunset + "PM EST." \
                + "The UV Index: " + uvi + ". This can be multiplied by 25 milliWatts per square meter."
        return message

## test
rightrice = weather()
print(rightrice.weather)