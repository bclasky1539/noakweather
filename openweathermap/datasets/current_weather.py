"""
This python script is for the current weather dataclasses for the openweather API.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from typing import List, Optional

from openweathermap.datasets.shared import Coord, Clouds, Weather, Wind, Rain, Snow
from utils.property_conversions import visibility_in_km, visibility_in_miles


# pylint: disable=too-many-instance-attributes
# Eight is reasonable in this case.
@dataclass
class Main:
    """Class representing the main information"""
    temp: Optional[float] = field(default=None)
    feels_like: Optional[float] = field(default=None)
    temp_min: Optional[float] = field(default=None)
    temp_max: Optional[float] = field(default=None)
    pressure: Optional[int] = field(default=None)
    humidity: Optional[int] = field(default=None)
    sea_level: Optional[int] = field(default=None)
    grnd_level: Optional[int] = field(default=None)

    @staticmethod
    def from_dict(obj: Any) -> 'Main':
        """
        :param obj      :      The Main information.

        :return:               Main information.
        """
        _temp = float(obj.get("temp"))
        _feels_like = float(obj.get("feels_like"))
        _temp_min = float(obj.get("temp_min"))
        _temp_max = float(obj.get("temp_max"))
        _pressure = int(obj.get("pressure"))
        _humidity = int(obj.get("humidity"))
        _sea_level = int(obj.get("sea_level"))
        _grnd_level = int(obj.get("grnd_level"))
        return Main(_temp, _feels_like, _temp_min, _temp_max, _pressure, _humidity,
                    _sea_level, _grnd_level)


@dataclass
class Sys:
    """Class representing the sys information"""
    type: Optional[int] = field(default=None)
    id: Optional[int] = field(default=None)
    country: Optional[str] = field(default=None)
    sunrise: Optional[datetime] = field(default=datetime.fromtimestamp(18000))  # Set to 01/01/1970
    sunset: Optional[datetime] = field(default=datetime.fromtimestamp(18000))  # Set to 01/01/1970

    @staticmethod
    def from_dict(obj: Any) -> 'Sys':
        """
        :param obj      :      The Sys information.

        :return:               Sys information.
        """
        _type = int(obj.get("type")) if obj.get("type") is not None else None
        _id = int(obj.get("id")) if obj.get("id") is not None else None
        _country = str(obj.get("country"))
        _sunrise = datetime.fromtimestamp(obj.get("sunrise"))
        _sunset = datetime.fromtimestamp(obj.get("sunset"))
        return Sys(_type, _id, _country, _sunrise, _sunset)


@dataclass
class CurrentWeatherData:
    """Class representing the Current Weather Data information"""
    coord: Coord = field(default=None)
    weather: List[Weather] = field(default=None)
    base: Optional[str] = field(default=None)
    main: Optional[Main] = field(default=None)
    visibility: Optional[float] = field(default=None)
    wind: Wind = field(default=None)
    rain: Rain = field(default=None)
    snow: Snow = field(default=None)
    clouds: Clouds = field(default=None)
    dt: Optional[int] = field(default=None)
    sys: Sys = field(default=None)
    timezone: Optional[int] = field(default=None)
    id: Optional[int] = field(default=None)
    name: Optional[str] = field(default=None)
    cod: Optional[int] = field(default=None)

    # pylint: disable=too-many-instance-attributes
    # Eight is reasonable in this case.
    @staticmethod
    def from_dict(obj: Any, units_of_measure: str) -> 'CurrentWeatherData':
        """
        :param obj                 :      The CurrentWeatherData information.
        :param units_of_measure    :      The units of measure.

        :return:                          CurrentWeatherData information.
        """
        try:
            _coord = Coord.from_dict(obj.get("coord"))
            _weather = [Weather.from_dict(y) for y in obj.get("weather")]
            _base = str(obj.get("base"))
            _main = Main.from_dict(obj.get("main"))
            if units_of_measure == "imperial":
                _visibility = visibility_in_miles(float(obj.get("visibility")))
            else:
                _visibility = visibility_in_km(float(obj.get("visibility")))
            _wind = Wind.from_dict(obj.get("wind"))
            _rain = Rain.from_dict(obj.get("rain"), "1h") if obj.get("rain") is not None else None
            _snow = Snow.from_dict(obj.get("snow"), "1h") if obj.get("snow") is not None else None
            _clouds = Clouds.from_dict(obj.get("clouds"))
            _dt = int(obj.get("dt"))
            _sys = Sys.from_dict(obj.get("sys"))
            _timezone = int(obj.get("timezone"))
            _id = int(obj.get("id"))
            _name = str(obj.get("name"))
            _cod = int(obj.get("cod"))
            return CurrentWeatherData(_coord, _weather, _base, _main, _visibility, _wind, _rain,
                                      _snow, _clouds, _dt, _sys, _timezone, _id, _name, _cod)
        except (IndexError, ValueError, TypeError, AttributeError, ImportError, NameError) as e:
            raise e
