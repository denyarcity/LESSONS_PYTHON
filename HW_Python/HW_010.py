# 1. Дискрипторы:


class Descriptor:
    def __init__(self):
        self.__fuel_cap = 0

    def __get__(self, instance, owner):
        return self.__fuel_cap

    def __set__(self, instance, value):
        if isinstance(value, int):
            print(value)
        else:
            raise TypeError("Запас топлива может быть только целым числом")
        if value < 0:
            raise ValueError("Запас топлива никогда не может быть меньше нуля")
        self.__fuel_cap = value

    def __delete__(self, instance):
        del self.__fuel_cap

class Descriptor1:
    def __init__(self):
        self.__make = 'BMW'

    def __get__(self, instance, owner):
        return self.__make

    def __set__(self, instance, value):
        if isinstance(value, str):
            print(value)
        else:
            raise TypeError("Марка автомобиля должна быть в строковом формате")
        self.__fuel_cap = value

    def __delete__(self, instance):
        del self.__make

class Car:
    fuel_cap = Descriptor()
    make = Descriptor1()
    def __init__(self, make, model, fuel_cap):
        self.make = make
        self.model = model
        self.fuel_cap = fuel_cap

    def __str__(self):
        return "{0} модель {1} с запасом топлива в {2} литров.".format(self.make, self.model, self.fuel_cap)


car1 = Car("BMW", "X7", 40)
print(car1)

car2 = Car("BMW", "X5", 50)
print(car2)


# 2 Метакласс


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,                                      cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
    
class SingletonClass(metaclass=Singleton):
    pass


class RegularClass():
    pass


x = SingletonClass()
y = SingletonClass()
print(x == y)


x = RegularClass()
y = RegularClass()
print(x == y)