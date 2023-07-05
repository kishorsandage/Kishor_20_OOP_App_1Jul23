# Employee Management System: Build an employee management system that enables users to add employees, manage their
# information, and generate reports.

employee_master = []


class Employee:
    def __init__(self,name,date_joining,position,manager,age,salary,function,experience,gender):
        self.name = name
        self.date_joining = date_joining
        self.position = position
        self.manager = manager
        self.age = age
        self.salary = salary
        self.function = function
        self.experience = experience
        self.gender = gender

    def getEmpDetails(self):
        print(f"{self.name} has joined on {self.date_joining} as {self.position} in {self.function} function and will "
              f"report to {self.manager}")
        print(f"He is {self.age} old, with experience of {self.experience} of years")


emp1 = Employee('Umesh','20 Jun 2020','Senior Engineer','Ramdas',25,50000,'Quality',5,'M')

emp1.getEmpDetails()

class PerformanceMgmt:
    def __init__(self,cutoff_yr):
        self.experience = None
        self.cutoff_yr = cutoff_yr

    def give_rise(self,minrise,maxrise):
        if self.experience > 3:
            newsalary = self.salary * minrise
        else:
            newsalary = self.salary * maxrise
        return newsalary

print(emp1.give_rise)
