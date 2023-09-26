"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

#Wage type (monthly or hour)
#Contract pay (amount per hour/month)
#Hours worked 
#Commission type (none, bonus, contract) 
#Commission rate/bonus(amount per contract/ fixed)
#Contracts
class Employee:
    def __init__(self, name, wage_type, pay, hours, commission_type, commission_rate, contracts):
        self.name = name
        self.wage_type = wage_type
        self.pay = pay
        self.hours = hours
        self.commision_type = commission_type
        self.commision_rate = commission_rate
        self.contracts = contracts

    def get_pay(self):
        pay = 0
        if self.wage_type == 'hourly':
            pay += self.pay*self.hours
        else:
            pay = self.pay
        if self.commision_type == 'bonus':
            pay += self.commision_rate
        elif self.commision_type == 'contract':
            pay += self.commision_rate*self.contracts
        return pay

    def __str__(self):
        if self.name == 'Charlie':
            return text_Charlie
        elif self.name == 'Billie':
            return text_Billie
        elif self.name == 'Renee':
            return text_Renee
        elif self.name == 'Jan':
            return text_Jan
        elif self.name == 'Robbie':
            return text_Robbie
        elif self.name == "Ariel":
            return text_Ariel


text_Billie = 'Billie works on a monthly salary of 4000.  Their total pay is 4000.'
billie = Employee('Billie', 'monthly', 4000, 0, 'None', 0, 0)

text_Charlie = 'Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.'
charlie = Employee('Charlie', 'hourly', 25, 100, 'None', 0, 0)

text_Renee = 'Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.'
renee = Employee('Renee', 'monthly', 3000, 0, 'contract', 200, 4)

text_Jan = 'Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.'
jan = Employee('Jan', 'hourly', 25, 150, 'contract', 220, 3)

text_Robbie =  'Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.'
robbie = Employee('Robbie', 'monthly', 2000, 0, 'bonus', 1500, 0)

text_Ariel = 'Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.'
ariel = Employee('Ariel', 'hourly', 30, 120, 'bonus', 600, 0)
