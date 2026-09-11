class Glassware:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} will be used")


class Beaker:
    def __init__(self, name):
       super().__init___(name)
       print(f"\nI have a {self.name}")
    def __del__(self):
        ("Beaker deleted !!")

class Tray:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        print("\nI have a tray")
        self.beaker = Beaker
    def __del__(self):
        ("Tray deleted !!")

waterBeaker = Beaker("Beaker filled with water")


