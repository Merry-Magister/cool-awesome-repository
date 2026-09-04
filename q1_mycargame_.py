class Car:
  def __init__(self,brand,model,battery=35):
    self.brand = brand
    self.model = model
    self.battery = battery
  def go(self,distance):
    self.baterry -= distance/20
    print("You traveled", distance)
    print("You have",selfbattery,"wH left")
  def charge(self, wH):
    self.battery += wH
    print("You recharged with", wH, "wH.")

car = Car("Geely", "EX5")
while car.battery > 0:
  act = input("What do we do? (g or c): ")
  if act == "g":
    distance = int(input("How far?: ")
    car.go(distance)
  elif act == "c":
    wH = int(input("How much to charge?: ")
    car.charge(wH)
  else:
    print("Invalid action, try again!") 

print("Game over. You had run out of battery.")
