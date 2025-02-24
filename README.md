# NOAK Weather Dashboard project

This project is a weather dashboard in Python. Currently, it will return the current weather from OpenWeatherMap. In the
future the project will be improved to include other items such as the following

- Additional information/features for the current weather
- 5-day forecast from OpenWeatherMap
- Other weather sources such as NOAA
- Database support for the weather results
- Machine Learning

## Project Setup

This project is set to use the OpenWeatherMap API. As a result it is necessary to have an api key from OpenWeatherMap.
To set up the environment please do the following

1) Copy the .env_template file to .env
2) If you do not have an api key from OpenWeatherMap go the [website](https://openweathermap.org/) and create one. This
   will require to sign up first. Sign up [here](http://home.openweathermap.org/users/sign_up).
3) Enter the information for the below environment variable in the .env file only:
    1) API_KEY
4) Make sure the .env file is not added/committed to the remote repository.

## Environment file (.env)

The file contains the following information

- API_KEY - This is the users api key.
- OWM_GEO_URL - This is the static URL for the GEO information.
- OWM_CUR_WEATHER_URL - This is the static URL for the current weather information.
- LANGUAGE - This is the language to be used for some of the information returned. Currently, it is set to english.
- UNITS_OF_MEASURE - This is the units of measurement which can be set to standard, metric or imperial. Currently, it is
  set to imperial.
- STANDARD_TEMPERATURE - This is the units for temperature in Kelvin.
- IMPERIAL_TEMPERATURE - This is the units for temperature in Fahrenheit.
- METRIC_TEMPERATURE - This is the units for temperature in Celsius.
- PRESSURE - This is the units for atmospheric pressure in hPa.
- HUMIDITY - This is the units for humidity in %.
- STANDARD_WIND_SPEED - This is the units for wind speed in meters/second.
- IMPERIAL_WIND_SPEED - This is the units for wind speed in miles/hour.
- WIND_DIRECTION - This is the units for wind direction in degrees.
- VISIBILITY - This is the units for visibility in kilometers (km). OpenWeatherMap returns it in meters but is converted
  to km. The maximum value of the visibility is 10 km.

## Which information is currently included in the dashboard?

- City
- Country
- Weather Conditions
- Temperature
- Feels like Temperature
- Minimum Temperature
- Maximum Temperature
- Ground Pressure
- Sea Level Pressure
- Humidity
- Visibility
- Wind Speed
- Wind Direction
- Wind Gust (if applicable)
- Sunrise
- Sunset

## Issues

If you notice any problems with running this, please open an
issue [here](https://github.com/bclasky1539/noakweather/issues).

## Fixing Issues and/or Adding New Features

- Feel free to fork and fix an issue(s) or add a feature.
- Please provide tests for the submitted code.
- Once the pull request is submitted, it'll be tested and merged.
