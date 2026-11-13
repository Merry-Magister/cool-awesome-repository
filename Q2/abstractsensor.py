from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_data(self):
        pass

class TempSensor(Sensor):
    def get_data(self):
        return "26 deg C"
    
sensor = TempSensor()
print(sensor.get_data())
