class Payment:
     def __init__(self, wage, commission):
         self.wage = wage
         self.commission = commission

     def salary(self):
         return (self.wage * 52) + self.commission

class Person:
     def __init__(self, name, height, wage, bonus):
         self.name = name
         self.height = height
         self.obj_payment = Payment(wage, bonus)
     def yearly_wage(self):
         return self.obj_payment.salary()


michael = Person("Michael", 1.8, 500, 5000)

my_total_wage = michael.yearly_wage()

print(my_total_wage)
31000