class Employee(object):
    raise_saraly_by=1.04
    numberOfEmployee=0
    def __init__(self,firstName,lastName,pay):
        self.firstName=firstName
        self.lastName=lastName
        self.pay=pay
        self.email=firstName+'.'+lastName+'@company.com'
        Employee.numberOfEmployee+=1

    def displayNumberOfEmployees(self):
        print "Total Employees %d"%Employee.numberOfEmployee
        
    def fullname(self):
        #return '{} {}'.format(self.firstName,self.lastName)
        return self.firstName+' '+self.lastName
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)

class Developer(Employee):#Inheritance
    raise_saraly_by=1.07#Information Hideing
    def __init__(self,firstName,lastName,pay,programmingLanguage):
        super(Developer,self).__init__(firstName,lastName,pay)
        self.programmingLanguage=programmingLanguage

class Manager(Employee):
    def __init__(self,firstName,lastName,pay,employees=None):
        super(Manager,self).__init__(firstName,lastName,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_employees(self,employee):
        if employee not in self.employees:
            self.employees.append(employee)
    def remove_employee(self,employee):
        if employee in self.employees:
            self.employees.remove(employee)
    def employees_managed(self):
        for emp in self.employees:
            print ('-->',emp.firstName+' '+emp.lastName)

emp_1=Employee('Esir','Kings',35000)
emp_2=Employee('Sarah','Wangari',25000)
developer_1=Developer('Mwakai','Wakesho',35000,'C++')

manager_1=Manager('Kimoda','Fransis',70000,[emp_1])
manager_1.add_employees(developer_1)
manager_1.remove_employee(emp_1)



print  developer_1.fullname()+' Programming In  '+developer_1.programmingLanguage#A developer And His/her Prog Language

print manager_1.fullname()+' Manager '

print manager_1.employees_managed()#Employees Managed By This Manager

manager_1.displayNumberOfEmployees()

