__version__ = '0.0.11'

from cuba_weather_municipality import CubaWeatherMunicipality
from .models import SourceModel, WeatherModel, WeatherDateModel
from .repositories import SourceRepository, WeatherRepository

class CubaWeatherRedCuba:
  '''
    Main class to provide package functionality.
  '''

  def __init__(self):
    self._cubaWeatherMunicipality = CubaWeatherMunicipality()
    self._sourceRepository = SourceRepository()
    self._weatherRepository = WeatherRepository()

  
  def get(self, input: str):
    '''
      Method that given a municipality searches the cuban municipalities to
      find the best match and returns the weather information.
    '''

    municipality = self._cubaWeatherMunicipality.get(input, suggestion=True)
    source = self._sourceRepository.getSource(municipality)
    weather = self._weatherRepository.getWeather(source)

    weatherDate = WeatherDateModel(
      date=weather.dt.date,
      timezoneType=weather.dt.timezoneType,
      timezone=weather.dt.timezone,
    )

    return WeatherModel(
      cityName=municipality.name,
      dt=weatherDate,
      temp=weather.temp,
      iconWeather=weather.iconWeather,
      descriptionWeather=weather.descriptionWeather,
      windVelocity=weather.windVelocity,
      windDirection=weather.windDirection,
      windDirectionDescription=weather.windDirectionDescription,
      pressure=weather.pressure,
      humidity=weather.humidity,
    )