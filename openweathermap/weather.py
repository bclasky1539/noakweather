"""
This python script gets the current weather from the openweather API.
"""
import os
from typing import Type
from urllib.error import HTTPError

import requests
from dotenv import load_dotenv
from requests import Response

from utils.get_class_name import get_full_class_name
from openweathermap.datasets.current_weather import CurrentWeatherData
from openweathermap.datasets.forecast import Forecast
from openweathermap.datasets.location import Location
from openweathermap.datasets.shared import Formats

# Get configuration information
load_dotenv()
api_key: str | None = os.getenv("API_KEY")
owm_geo_url: str | None = os.getenv("OWM_GEO_URL")
owm_cur_weather_url: str | None = os.getenv("OWM_CUR_WEATHER_URL")
own_forecast_url: str | None = os.getenv("OWM_FRC_WEATHER_URL")
language: str | None = os.getenv("LANGUAGE")
units_of_measure: str | None = os.getenv("UNITS_OF_MEASURE")


# help(CurrentWeatherData)

# def postgres_close(p_connection: Connection) -> None:
def get_lan_lon(city_name: str, state_code: str, country_code: str, limit: int = 1) -> Location:
    """
    :param city_name:      The city name to get the latitude and longitude from.
    :param state_code:     The state code to get the latitude and longitude from.
    :param country_code:   The country code to get the latitude and longitude from.
    :param limit:          The number of latitude and longitude combinations to retrieve.

    :return:               Location dataclass representing the location.
    """
    try:
        location_data: Location | None = Location()
        resp: Response = requests.get(
            f"{owm_geo_url}{city_name},{state_code},{country_code}&limit={limit}&appid={api_key}",
            timeout=5)
        print(f"get_lan_lon: {resp.status_code = }")
        print(f"{resp.json() = }")
        print(f"{type(resp.json()) = }")
        if resp.status_code == 200 and resp.json():
            location_data = Location.from_dict(resp.json()[0])
    except HTTPError as e:
        print(f"{get_full_class_name(e)}: {e.read().decode()}")
        location_data = None
    except (IndexError, ValueError, TypeError, AttributeError, ImportError, NameError) as e:
        print(f"{get_full_class_name(e)}: {e.args}")
        location_data = None

    return location_data


def get_current_weather(lat: float, lon: float) -> CurrentWeatherData:
    """
    :param lat:      The latitude to get the current weather from.
    :param lon:      The longitude to get the current weather from.

    :return:         CurrentWeatherData dataclass representing the current weather.
    """
    try:
        current_weather_data: CurrentWeatherData | None = CurrentWeatherData()
        resp: Response = requests.get(
            f"{owm_cur_weather_url}lat={lat}&lon={lon}&lang={language}&appid={api_key}"
            f"&units={units_of_measure}", timeout=5)
        print(f"get_current_weather: {resp.status_code = }")
        print(f"{resp.json() = }")
        print(f"{type(resp.json()) = }")
        if resp.status_code == 200 and resp.json():
            current_weather_data = CurrentWeatherData.from_dict(resp.json(), units_of_measure)
    except HTTPError as e:
        print(f"{get_full_class_name(e)}: {e.read().decode()}")
        current_weather_data = None
    except (IndexError, ValueError, TypeError, AttributeError) as e:
        print(f"{get_full_class_name(e)}: {e.args}")
        current_weather_data = None

    return current_weather_data


def get_forcast(lat: float, lon: float) -> Forecast:
    """
    :param lat:      The latitude to get the forecast from.
    :param lon:      The longitude to get the forecast from.

    :return:         ForecastData dataclass representing the forecast.
    """
    try:
        forecast_data: Forecast | None = Forecast()
        resp: Response = requests.get(
            f"{own_forecast_url}lat={lat}&lon={lon}&lang={language}&appid={api_key}"
            f"&units={units_of_measure}", timeout=5)
        print(f"get_forcast: {resp.status_code = }")
        print(f"{resp.json() = }")
        print(f"{type(resp.json()) = }")
        if resp.status_code == 200 and resp.json():
            forecast_data = Forecast.from_dict(resp.json(), units_of_measure)
    except HTTPError as e:
        print(f"{get_full_class_name(e)}: {e.read().decode()}")
        forecast_data = None
    except (IndexError, ValueError, TypeError, AttributeError) as e:
        print(f"{get_full_class_name(e)}: {e.args}")
        forecast_data = None

    return forecast_data


def main(city_name: str, state_code: str, country_code: str) -> \
        (tuple[Type[Location], Type[CurrentWeatherData], Type[Formats]] | tuple):
    """
    :param city_name:      The city name to get the latitude and longitude from.
    :param state_code:     The state code to get the latitude and longitude from.
    :param country_code:   The country code to get the latitude and longitude from.

    :return:               Tuple of the Location and the CurrentWeatherData dataclasses.
    """
    formats_data: Formats = Formats.set_format_items(units_of_measure)
    print(f"In main: {formats_data = }")

    location_data: Location = get_lan_lon(city_name, state_code, country_code)
    print(f"In main: {location_data = }")

    current_weather_data: CurrentWeatherData = get_current_weather(location_data.lat,
                                                                   location_data.lon)
    print(f"In main: {current_weather_data = }")

    forecast_data: Forecast = get_forcast(location_data.lat, location_data.lon)
    print(f"In main: {forecast_data = }")

    return location_data, current_weather_data, forecast_data, formats_data


if __name__ == '__main__':
    main('Atlanta', 'GA', country_code='US')
    # main('Toronto', '', country_code='CA')
    # main('Dublin', '', country_code = 'IE')
    # main('London', '', country_code='GB')
    # main('Solon', 'OH', 'US')
    # main('Letlhakane', '', country_code='BW')
