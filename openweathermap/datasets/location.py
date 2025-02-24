"""
This python script is for the location dataclasses used for the current weather
and forecast for the openweather API.
"""
from dataclasses import dataclass, field
from typing import Any, Optional


# pylint: disable=too-many-instance-attributes
# Thirty Six is reasonable in this case.
@dataclass
class LocalNames:
    """Class representing the local names"""
    my: Optional[str] = field(default=None)
    uk: Optional[str] = field(default=None)
    yi: Optional[str] = field(default=None)
    la: Optional[str] = field(default=None)
    th: Optional[str] = field(default=None)
    os: Optional[str] = field(default=None)
    ta: Optional[str] = field(default=None)
    lt: Optional[str] = field(default=None)
    bg: Optional[str] = field(default=None)
    zh: Optional[str] = field(default=None)
    hy: Optional[str] = field(default=None)
    gu: Optional[str] = field(default=None)
    kw: Optional[str] = field(default=None)
    ml: Optional[str] = field(default=None)
    te: Optional[str] = field(default=None)
    ja: Optional[str] = field(default=None)
    ko: Optional[str] = field(default=None)
    sr: Optional[str] = field(default=None)
    ur: Optional[str] = field(default=None)
    he: Optional[str] = field(default=None)
    ru: Optional[str] = field(default=None)
    el: Optional[str] = field(default=None)
    ht: Optional[str] = field(default=None)
    oc: Optional[str] = field(default=None)
    ar: Optional[str] = field(default=None)
    eo: Optional[str] = field(default=None)
    fa: Optional[str] = field(default=None)
    bo: Optional[str] = field(default=None)
    ka: Optional[str] = field(default=None)
    mr: Optional[str] = field(default=None)
    be: Optional[str] = field(default=None)
    mk: Optional[str] = field(default=None)
    pl: Optional[str] = field(default=None)
    ce: Optional[str] = field(default=None)
    en: Optional[str] = field(default=None)
    kn: Optional[str] = field(default=None)

    # pylint: disable=too-many-instance-attributes
    # Thirty Seven is reasonable in this case.
    @staticmethod
    def from_dict(obj: Any) -> 'LocalNames':
        """
        :param obj      :      The coordinates' information.

        :return:               Local names information.
        """
        _my = str(obj.get("my"))
        _uk = str(obj.get("uk"))
        _yi = str(obj.get("yi"))
        _la = str(obj.get("la"))
        _th = str(obj.get("th"))
        _os = str(obj.get("os"))
        _ta = str(obj.get("ta"))
        _lt = str(obj.get("lt"))
        _bg = str(obj.get("bg"))
        _zh = str(obj.get("zh"))
        _hy = str(obj.get("hy"))
        _gu = str(obj.get("gu"))
        _kw = str(obj.get("kw"))
        _ml = str(obj.get("ml"))
        _te = str(obj.get("te"))
        _ja = str(obj.get("ja"))
        _ko = str(obj.get("ko"))
        _sr = str(obj.get("sr"))
        _ur = str(obj.get("ur"))
        _he = str(obj.get("he"))
        _ru = str(obj.get("ru"))
        _el = str(obj.get("el"))
        _ht = str(obj.get("ht"))
        _oc = str(obj.get("oc"))
        _ar = str(obj.get("ar"))
        _eo = str(obj.get("eo"))
        _fa = str(obj.get("fa"))
        _bo = str(obj.get("bo"))
        _ka = str(obj.get("ka"))
        _mr = str(obj.get("mr"))
        _be = str(obj.get("be"))
        _mk = str(obj.get("mk"))
        _pl = str(obj.get("pl"))
        _ce = str(obj.get("ce"))
        _en = str(obj.get("en"))
        _kn = str(obj.get("kn"))
        return LocalNames(_my, _uk, _yi, _la, _th, _os, _ta, _lt, _bg, _zh, _hy, _gu, _kw, _ml,
                          _te, _ja, _ko, _sr, _ur, _he, _ru, _el, _ht, _oc, _ar, _eo, _fa, _bo,
                          _ka, _mr, _be, _mk, _pl, _ce, _en, _kn)


@dataclass
class Location:
    """Class representing the Location data"""
    name: Optional[str] = field(default=None)
    local_names: Optional[LocalNames] = field(default=None)
    lat: Optional[float] = field(default=None)
    lon: Optional[float] = field(default=None)
    country: Optional[str] = field(default=None)
    state: Optional[str] = field(default=None)

    @staticmethod
    def from_dict(obj: Any) -> 'Location':
        """
        :param obj      :      The Location information.

        :rtype          :      The Location information.
        """
        try:
            _name = str(obj.get("name"))
            _local_names = LocalNames.from_dict(obj.get("local_names")) \
                if obj.get("local_names") is not None else None
            _lat = float(obj.get("lat"))
            _lon = float(obj.get("lon"))
            _country = str(obj.get("country"))
            _state = str(obj.get("state"))
            return Location(_name, _local_names, _lat, _lon, _country, _state)
        except (IndexError, ValueError, TypeError, AttributeError, ImportError, NameError) as e:
            raise e
