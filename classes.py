class Employee:
    num_of_employees = 0
    raise_amount = 1.05

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.salary = salary
        Employee.num_of_employees += 1

    def printing(self):
        print('Name: ' + self.first + ' ' + self.last)
        print('Email Address: ' + self.email)
        print('Salary: ' + str(self.salary))

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @staticmethod
    def isMonday(day):
        if day == 'Monday':
            return True
        return False


emp1 = Employee('Rishi', 'Shukla', 2000)
emp2 = Employee('Praveen', 'Parmar', 3000)

print('No.of employees: {0}'.format(str(Employee.num_of_employees)))

print('\n')
emp1.printing()
print('\n')
emp2.printing()

print('\n')
print("Initial Raise Amount: {0}".format(str(Employee.raise_amount)))
Employee.set_raise_amount(1.06)
print("Changed Raise Amount: {0}".format(str(Employee.raise_amount)))

print(Employee.isMonday('Wednesday'))
