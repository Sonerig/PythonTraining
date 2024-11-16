from pprint import pprint
import inspect


class Temp:
    def __init__(self):
        self.a = "temp"

    def foo(self):
        return self.a


def introspection_info(obj):
    return {"Тип объекта: ": type(obj),
            "Атрибуты обекта: ": [attr_name for attr_name in dir(obj) if not callable(getattr(obj, attr_name))],
            "Методы объекта: ": [attr_name for attr_name in dir(obj) if callable(getattr(obj, attr_name))],
            "Модуль к которому принадлежит объект: ": inspect.getmodule(obj)}


b = Temp()
pprint(introspection_info(b))
