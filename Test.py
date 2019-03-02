emp_count = 0
sal_l = []
class Employee():
    def __init__(self,name,family,salary,department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
    def average_salary(self,sal_list):
        self.sal_list = sum(sal_l) / float(len(sal_l))

class Fulltime_Employee(Employee):
    def __init__(self,name,family,salary,department):
        Employee.__init__(self,name,family,salary,department)

n = str(input("Please enter your name: "))
f = str(input("Please enter your family name: "))
s = int(input("Please input your salary:"))
d = str(input("Please enter your department: "))
emp = Employee(n,f,s,d)
emp_count = emp_count + 1
sal_l.append(s)
emp.average_salary(sal_l)
print(emp.sal_list)
emp1 = Fulltime_Employee('Rupesh Sai Ram','Doddala',4000,'CS')
print(emp1.salary)




