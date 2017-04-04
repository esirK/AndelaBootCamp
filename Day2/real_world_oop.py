class Employee:
    numberOfEmployee=0
    basic_salary=5000

    def __init__(self,name):
        self.name=name
        Employee.numberOfEmployee+=1
    
    def displayAnEmployee(self):
        print "Name: ",self.name,", Salary:",self.basic_salary

    def displayNumberOfEmployees(self):
        print "Total Employees %d"%Employee.numberOfEmployee


class Manager(Employee):
    def getInsurance(self):
        self.basic_salary=self.basic_salary+(1000)
        return self.basic_salary

class DirectorGeneral(Employee):
    def getInsurance(self):
        self.basic_salary=self.basic_salary+(5000)
        return self.basic_salary
        
kamudi=Employee("HuKmau")
kamudi.displayNumberOfEmployees()
kamudi.displayAnEmployee()

wanja=Manager("Wanjaa")
wanja.getInsurance()
wanja.displayAnEmployee()
wanja.displayNumberOfEmployees()

Mwaniki=DirectorGeneral("Mwaniki")
Mwaniki.getInsurance()
Mwaniki.displayAnEmployee()
Mwaniki.displayNumberOfEmployees()
