from ..models import WeatherModel
from ..utils import BadRequestException, InvalidSourceException

from urllib.parse import quote
from urllib.request import urlopen
from urllib.error import HTTPError

from json import loads

class WeatherApiClient:
  '''
    Class to provide the functionality of making API requests
  '''

  def __init__(self):
    self.baseUrl = 'https://www.redcuba.cu/api/weather_get_summary/'

  def fetchWeather(self, location: str) -> WeatherModel:
    '''
      Method to make the request GET to API
    '''
    url = self.baseUrl + quote(location)

    try:
      resp = urlopen(url)
    except HTTPError as ex:
      if ex.code == 404:
        raise InvalidSourceException('Source is invalid')
      elif ex.code != 200:
        raise BadRequestException('Bad request')
    
    content = resp.read()
    if type(content) == bytes:
      content = content.decode()
    
    data_json = loads(content)
    return WeatherModel.fromJson(data_json)