class Sensor:
    def __init__(self, name, unit, value):
        self.__value = value
        self.__name = name
        self.__unit = unit

    def showdata(self):
        print(f"{self.__name}: {self.__value} {self.__unit}")

    def getvalue(self):
        return self.__value