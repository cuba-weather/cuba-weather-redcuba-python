from ..data_providers import WeatherApiClient
from ..models import SourceModel

class WeatherRepository:
  '''
    Class to provide the functionality of obtaining weather data
  '''
  def __init__(self):
    self.weatherApiClient = WeatherApiClient()

  def getWeather(self, source: SourceModel):
    return self.weatherApiClient.fetchWeather(source.name)
