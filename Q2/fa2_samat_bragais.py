class Patient:
  def __init__(self, name, bill_amount):
    self.__name = name
    self.__bill_amount = bill_amount

  def get_name(self):
    print(f" Patient Name: {self.name}")

  def set_name(self, name):
    self.__name = name

  def get_bill_amount(self):
    print(f"Original Bill: {self.__bill_amount}")

 def set_bill_amount(self, bill_amount):
    self.__bill_amount = bill_amount

 def calculate_bill(self):
    print
   
