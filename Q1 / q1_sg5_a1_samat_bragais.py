class Hero:
  def __init__(self, name, hp=25):
    self.name = name
    self.hp = hp
    
  def take_damage(self, amount):
    self.hp -= amount
    print(f"{self.name} took {amount} damage!")
    
  def hp_tracker(self):
    print(f"{self.name} currently has {self.hp} hp.")

arthur = Hero("Arthur")
morgana = Hero("Morgana")

arthur.take_damage(10)

arthur.hp_tracker()
morgana.hp_tracker()
