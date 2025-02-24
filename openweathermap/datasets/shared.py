"""
This python script is for the shared dataclasses used for the current weather
and forecast for the openweather API.
"""
import os
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class Coord:
    """Class representing the location latitude and longitude"""
    lon: Optional[float] = field(default=None)
    lat: Optional[float] = field(default=None)

    @staticmethod
    def from_dict(obj: Any) -> 'Coord':
        """
        :param obj      :      The coordinates' information.

        :return:               Latitude and longitude information.
        """
        _lon = float(obj.get("lon"))
        _lat = float(obj.get("lat"))
        return Coord(_lon, _lat)


@dataclass
class Clouds:
    """Class representing a cloud information"""
    all: Optional[int] = field(default=None)

    @staticmethod
    def from_dict(obj: Any) -> 'Clouds':
        """
        :param obj      :      The cloud information.

        :return:               Cloud information.
        """
        _all = int(obj.get("all"))
        return Clouds(_all)


@dataclass
class Weather:
    """Class representing a weather information"""
    id: Optional[int] = field(default=None)
    main: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    icon: Optional[str] = field(default=None)

    @staticmethod
    def from_dict(obj: Any) -> 'Weather':
        """
        :param obj      :      The weather information.

        :return:               Weather information.
        """
        _id = int(obj.get("id"))
        _main = str(obj.get("main"))
        _description = str(obj.get("description"))
        _icon = str(obj.get("icon"))
        return Weather(_id, _main, _description, _icon)


@dataclass
class Rain:
    """Class representing a rain information"""
    rain_amount: Optional[float] = field(default=None)
    rain_type: Optional[str] = field(default=None)

    @staticmethod
    def from_dict(obj: Any, rtype: str) -> 'Rain':
        """
        :param obj      :      The rain information.
        :param rtype    :      The type of rain.

        :return:               Rain amount and type information.
        """
        _rain_amount = float(obj.get(rtype)) if obj.get(rtype) is not None else None
        _rain_type = rtype
        return Rain(_rain_amount, _rain_type)


@dataclass
class Snow:
    """Class representing a snow information"""
    snow_amount: Optional[float] = field(default=None)
    snow_type: Optional[str] = field(default=None)

    @staticmethod
    def from_dict(obj: Any, rtype: str) -> 'Snow':
        """
        :param obj      :      The snow and snow type information.
        :param rtype    :      The type of snow.

        :return:               Snow amount and type information.
        """
        _snow_amount = float(obj.get(rtype)) if obj.get(rtype) is not None else None
        _snow_type = rtype
        return Snow(_snow_amount, _snow_type)


@dataclass
class Wind:
    """Class representing a wind information"""
    speed: Optional[float] = field(default=None)
    deg: Optional[int] = field(default=None)
    gust: Optional[float] = field(default=None)

    @staticmethod
    def from_dict(obj: Any) -> 'Wind':
        """
        :param obj      :      The wind information.

        :return:               Wind speed, direction and gusts information.
        """
        _speed = float(obj.get("speed"))
        _deg = int(obj.get("deg"))
        _gust = float(obj.get("gust")) if obj.get("gust") is not None else -999999.0
        return Wind(_speed, _deg, _gust)


@dataclass
class Formats:
    """Class representing the current weather formats"""
    temperature_format: Optional[str] = field(default=None)
    pressure_format: Optional[str] = field(default=None)
    humidity_format: Optional[str] = field(default=None)
    wind_speed_format: Optional[str] = field(default=None)
    wind_direction_format: Optional[str] = field(default=None)
    visibility_format: Optional[str] = field(default=None)

    @staticmethod
    def set_format_items(units_of_measure: str) -> 'Formats':
        """
        :param units_of_measure      :      The units of measure information.

        :return:                            The different formats' information.
        """
        try:
            if units_of_measure == "metric":
                _temperature_format: str | None = os.getenv("METRIC_TEMPERATURE")
            elif units_of_measure == "imperial":
                _temperature_format: str | None = os.getenv("IMPERIAL_TEMPERATURE")
            else:
                _temperature_format: str | None = os.getenv("STANDARD_TEMPERATURE")
            _pressure_format: str | None = os.getenv("PRESSURE")
            _humidity_format: str | None = os.getenv("HUMIDITY")
            if units_of_measure == "imperial":
                _wind_speed_format: str | None = os.getenv("IMPERIAL_WIND_SPEED")
            else:
                _wind_speed_format: str | None = os.getenv("STANDARD_WIND_SPEED")
            _wind_direction_format: str | None = os.getenv("WIND_DIRECTION")
            if units_of_measure == "imperial":
                _visibility_format: str | None = os.getenv("IMPERIAL_VISIBILITY")
            else:
                _visibility_format: str | None = os.getenv("STANDARD_VISIBILITY")
            return Formats(_temperature_format, _pressure_format, _humidity_format,
                           _wind_speed_format, _wind_direction_format, _visibility_format)
        except (IndexError, ValueError, TypeError, AttributeError, ImportError, NameError) as e:
            raise e
