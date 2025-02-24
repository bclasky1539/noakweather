"""
This python script is for the forecast weather dataclasses for the openweather API.
"""
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from typing import List, Optional

from openweathermap.datasets.shared import Coord, Clouds, Weather, Wind, Rain
from utils.property_conversions import visibility_in_miles, visibility_in_km


@dataclass
class City:
    """Class representing the City information"""
    id: Optional[int] = field(default=None)
    name: Optional[str] = field(default=None)
    coord: Coord = field(default=None)
    country: Optional[str] = field(default=None)
    population: Optional[int] = field(default=None)
    timezone: Optional[int] = field(default=None)
    sunrise: Optional[datetime] = field(default=datetime.fromtimestamp(18000))  # Set to 01/01/1970
    sunset: Optional[datetime] = field(default=datetime.fromtimestamp(18000))  # Set to 01/01/1970

    @staticmethod
    def from_dict(obj: Any) -> 'City':
        """
        :param obj       :      The City information.

        :return:                City information.
        """
        _id = int(obj.get("id"))
        _name = str(obj.get("name"))
        _coord = Coord.from_dict(obj.get("coord"))
        _country = str(obj.get("country"))
        _population = int(obj.get("population"))
        _timezone = int(obj.get("timezone"))
        _sunrise = datetime.fromtimestamp(obj.get("sunrise"))
        _sunset = datetime.fromtimestamp(obj.get("sunset"))
        return City(_id, _name, _coord, _country, _population, _timezone, _sunrise, _sunset)


@dataclass
class Main:
    """Class representing the Main information"""
    temp: Optional[float] = field(default=None)
    feels_like: Optional[float] = field(default=None)
    temp_min: Optional[float] = field(default=None)
    temp_max: Optional[float] = field(default=None)
    pressure: Optional[int] = field(default=None)
    sea_level: Optional[int] = field(default=None)
    grnd_level: Optional[int] = field(default=None)
    humidity: Optional[int] = field(default=None)
    temp_kf: Optional[float] = field(default=None)

    @staticmethod
    def from_dict(obj: Any) -> 'Main':
        """
        :param obj        :         The Main information.

        :return:                    Main information.
        """
        _temp = float(obj.get("temp"))
        _feels_like = float(obj.get("feels_like"))
        _temp_min = float(obj.get("temp_min"))
        _temp_max = float(obj.get("temp_max"))
        _pressure = int(obj.get("pressure"))
        _sea_level = int(obj.get("sea_level"))
        _grnd_level = int(obj.get("grnd_level"))
        _humidity = int(obj.get("humidity"))
        _temp_kf = float(obj.get("temp_kf"))
        return Main(_temp, _feels_like, _temp_min, _temp_max, _pressure, _sea_level, _grnd_level,
                    _humidity, _temp_kf)


@dataclass
class Sys:
    """Class representing the Sys information"""
    pod: Optional[str] = field(default=None)

    @staticmethod
    def from_dict(obj: Any) -> 'Sys':
        """
        :param obj         :         The Sys information.

        :return:                     Sys information.
        """
        _pod = str(obj.get("pod"))
        return Sys(_pod)


@dataclass
class ListObj:
    """Class representing the ListObj information"""
    dt: Optional[int] = field(default=None)
    main: Main = field(default=None)
    weather: List[Weather] = field(default=None)
    clouds: Clouds = field(default=None)
    wind: Wind = field(default=None)
    visibility: Optional[int] = field(default=None)
    pop: Optional[float] = field(default=None)
    rain: Rain = field(default=None)
    sys: Sys = field(default=None)
    dt_txt: Optional[str] = field(default=None)

    @staticmethod
    def from_dict(obj: Any, units_of_measure: str) -> 'ListObj':
        """
        :param obj                    :     The ListObj information.
        :param units_of_measure       :     The units of measure.

        :return:                            ListObj information.
        """
        _dt = int(obj.get("dt"))
        _main = Main.from_dict(obj.get("main"))
        _weather = [Weather.from_dict(y) for y in obj.get("weather")]
        _clouds = Clouds.from_dict(obj.get("clouds"))
        _wind = Wind.from_dict(obj.get("wind"))
        if units_of_measure == "imperial":
            _visibility = visibility_in_miles(float(obj.get("visibility"))) if obj.get(
                "visibility") is not None else None
        else:
            _visibility = visibility_in_km(float(obj.get("visibility"))) if (obj.get("visibility")
                                                                             is not None) else None
        _pop = float(obj.get("pop"))
        _rain = Rain.from_dict(obj.get("rain"), "3h") if obj.get("rain") is not None else None
        _sys = Sys.from_dict(obj.get("sys"))
        _dt_txt = str(obj.get("dt_txt"))
        return ListObj(_dt, _main, _weather, _clouds, _wind, _visibility, _pop, _rain,
                       _sys, _dt_txt)


@dataclass
class Forecast:
    """Class representing the Forecast information"""
    cod: Optional[int] = field(default=None)
    message: Optional[int] = field(default=None)
    cnt: Optional[int] = field(default=None)
    list_obj: List[ListObj] = field(default=None)
    city: City = field(default=None)

    @staticmethod
    def from_dict(obj: Any, units_of_measure: str) -> 'Forecast':
        """
        :param obj                :      The Forecast information.
        :param units_of_measure   :      The units of measure.

        :return:                          Forecast information.
        """
        try:
            _cod = int(obj.get("cod"))
            _message = int(obj.get("message"))
            _cnt = int(obj.get("cnt"))
            _list_obj = [ListObj.from_dict(y, units_of_measure) for y in obj.get("list")]
            _city = City.from_dict(obj.get("city"))
            return Forecast(_cod, _message, _cnt, _list_obj, _city)
        except (IndexError, ValueError, TypeError, AttributeError, ImportError, NameError) as e:
            raise e
