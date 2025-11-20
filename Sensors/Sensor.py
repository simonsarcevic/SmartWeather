class Sensor:
    def __init__(self, name, unit, value):
        self.__value = value
        self.__name = name
        self.__unit = unit
        self.__value = value

    def showdata(self):
        print(self.__name, self.__unit, self.__value)
