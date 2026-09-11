class Glassware:
    def __init__(self, name):
        self.name = name
        print(f"\na {self.name} will be used")
        
    def putAway(self, name):
        print(f"putting away the {self.name}...")

class Beaker(Glassware):
    def __init__(self, name):
       super().__init__(name)
       print(f"I have a {self.name}")
    
    def __del__(self):
        (f"a {self.name} was deleted !!")
        
    def putAway(self, name):
        super().putAway(self, name)

class Tray:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        print("\nI have a tray")
        self.firstBeaker = Beaker("beaker filled with water")
        self.secondBeaker = Beaker("small beaker filled with some oil")
        self.thirdBeaker = Beaker("currently empty beaker")
        self.fourthBeaker = Beaker("recently cleaned beaker")
        self.fifthBeaker = Beaker("beaker filled with saltwater")
    
    def __del__(self):
        ("Tray deleted !!")
        del self.firstBeaker; del self.secondBeaker; del self.thirdBeaker; del self.fourthBeaker; del self.fifthBeaker

tray = Tray()
tray.firstBeaker.putAway
del tray
