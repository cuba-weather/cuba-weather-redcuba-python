from datetime import datetime
from enum import IntEnum

class CardinalPoint(IntEnum):
  North=1
  Northeast=2
  East=3
  Southeast=4
  South=5
  Southwest=6
  West=7
  Northwest=8

class WeatherDateModel:
  '''
    Model class for mapping part of the json returned by the https://www.redcuba.cu weather API
  '''

  def __init__(self, date: datetime, timezoneType: float, timezone: str):
    self.date = date
    self.timezoneType = timezoneType
    self.timezone = timezone

  @staticmethod
  def fromJson(json: dict):
    '''
      Static method that returns an instance of the class from the json provided
    '''

    return WeatherDateModel(
      date=datetime.strptime(json['date'], '%Y-%m-%d %H:%M:%S.%f'),
      timezoneType=float(json['timezone_type']),
      timezone=str(json['timezone']),
    )

class WeatherModel:
  '''
    Model class for mapping the json returned by the https://www.redcuba.cu weather API
  '''

  def __init__(
    self, 
    cityName: str, 
    dt: WeatherDateModel, 
    temp: float, 
    pressure: float,
    humidity: float,
    iconWeather: str, 
    windVelocity: float,
    windDirection: CardinalPoint,
    windDirectionDescription: str,
    descriptionWeather: str
  ):
    self.cityName = cityName
    self.dt = dt
    self.temp = temp
    self.pressure = pressure
    self.humidity = humidity
    self.iconWeather = iconWeather
    self.windVelocity = round(windVelocity, 2)
    self.windDirection = windDirection
    self.windDirectionDescription = windDirectionDescription
    self.descriptionWeather = descriptionWeather

  @staticmethod
  def fromJson(json: dict):
    '''
      Static method that returns an instance of the class from the json provided
    '''

    data = json['data']
    windString = data['windstring']

    beginIndex = windString.index('Velocidad') + 9
    endIndex = windString.index('m/s')

    windVelocityString = windString[beginIndex : endIndex].strip()
    windVelocity = float(windVelocityString) * 3.6

    beginIndex = endIndex + 3
    endIndex = len(windString)

    windDirectionDesc = windString[beginIndex : endIndex].strip()

    weatherDate = WeatherDateModel.fromJson(data['dt'])

    return WeatherModel(
      cityName=data['cityName'],
      dt=weatherDate,
      temp=float(str(data['temp'])),
      pressure=float(str(data['pressure'])),
      humidity=float(str(data['humidity'])),
      iconWeather=data['iconWeather'],
      windVelocity=windVelocity,
      windDirection=WeatherModel._parseDirection(windDirectionDesc),
      windDirectionDescription=windDirectionDesc,
      descriptionWeather=data['descriptionWeather'],
    )

  def __str__(self):
    result = ''
    result += 'City Name: {}\n'.format(self.cityName)
    result += 'Temperature: {}°C\n'.format(self.temp)
    result += 'Timestamp: {}\n'.format(self.dt.date)
    result += 'Humidity: {}%\n'.format(self.humidity)
    result += 'Pressure: {} hpa\n'.format(self.pressure)
    result += 'Wind Velocity: {} Km/h\n'.format(self.windVelocity)
    result += 'Wind Direction: {}\n'.format(self.windDirection)
    result += 'Wind Direction Description: {}\n'.format(self.windDirectionDescription)
    result += 'Description: {}\n'.format(self.descriptionWeather)
    result += 'Image Link: {}'.format(self.iconWeather)
    return result

  @staticmethod
  def _parseDirection(input: str) -> CardinalPoint :
    direction = input.split(' ')[0].lower().strip()
    
    if direction == 'norte':
      return CardinalPoint.North
    if direction == 'noreste':
      return CardinalPoint.Northeast
    if direction == 'este':
      return CardinalPoint.East
    if direction == 'sureste':
      return CardinalPoint.Southeast
    if direction == 'sur':
      return CardinalPoint.South
    if direction == 'suroeste':
      return CardinalPoint.Southwest
    if direction == 'oeste':
      return CardinalPoint.West
    if direction == 'noroeste':
      return CardinalPoint.Northwest
      
    return CardinalPoint.North

