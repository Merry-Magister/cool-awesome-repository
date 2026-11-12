from abc import ABC, abstractmethod

class Sensor(ABC):
  @abstractmethod
  def get_reading(self):
    pass

class PHSensor(Sensor):
  def get_reading(self):
    return "7.2 pH"

class TempSensor(Sensor):
  def get_reading(self):
    return "24.5°C"

first_sensor = PHSensor()
second_sensor = TempSensor()

print("pH Reading:",first_sensor.get_reading())
print("Temperature Reading:",second_sensor.get_reading())
