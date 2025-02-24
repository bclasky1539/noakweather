"""
This python script is to perform conversions for different property types.
"""


def visibility_in_km(visibility: float) -> float:
    """
    :param visibility:      visibility.

    :return:          round(self.visibility / 1000)
    """
    return round(visibility / 1000, 2)


def visibility_in_miles(visibility: float) -> float:
    """
    :param visibility:      visibility.

    :return:          round(visibility_in_km(visibility) * 0.621371)
    """
    return round(visibility_in_km(visibility) * 0.621371, 2)
