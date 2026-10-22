# setting up parent class
class Patient:
  def __init__(self, name, bill_amount):
    self.__name = name
    self.__bill_amount = float(bill_amount)

  def get_name(self):
    print(f"Patient Name: {self.__name}")

  def set_name(self, name):
    self.__name = name

  def get_bill_amount(self):
    print(f"Original Bill: ₱{self.__bill_amount}")

  def set_bill_amount(self, bill_amount):
    self.__bill_amount = bill_amount

  def calculate_bill(self):
    print(f"Final Bill: ₱{self.__bill_amount}\n")


# creating child classes
class Senior_Patient(Patient):
  def calculate_bill(self):
    print(f"Final Bill: ₱{self._Patient__bill_amount - (self._Patient__bill_amount * 0.20)}\n")

class PhilHealth_Patient(Patient):
  def calculate_bill(self):
    print(f"Final Bill: ₱{self._Patient__bill_amount - (self._Patient__bill_amount * 0.15)}\n")

# adding objects
regular_patient = Patient("Juan Dela Cruz", 15000)
senior_citizen = Senior_Patient("Maria Santos", 15000)
philhealth_member = PhilHealth_Patient("Pedro Reyes", 15000)

# printing the output
print("Hospital Billing System \n- - - - - - - - - - - - - - - - - - -")
regular_patient.get_name(); regular_patient.get_bill_amount(); regular_patient.calculate_bill()
senior_citizen.get_name(); senior_citizen.get_bill_amount(); senior_citizen.calculate_bill()
philhealth_member.get_name(); philhealth_member.get_bill_amount(); philhealth_member.calculate_bill()
