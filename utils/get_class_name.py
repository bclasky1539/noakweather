"""
This python script is to get the class name of an object.
"""


def get_full_class_name(obj: object) -> str | None:
    """
    :param obj:     The object to determine the class name.

    :return:        module + '.' + obj.__class__.__name__ string
    """
    module = obj.__class__.__module__
    if module is None or module == str.__class__.__module__:
        return obj.__class__.__name__
    return module + '.' + obj.__class__.__name__
