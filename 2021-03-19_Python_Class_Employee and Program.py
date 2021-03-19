#Python class (Employee) and program
# Computer Programming Tutor_YT_March 19,2021

class Employee:
    " common base class for for all employees"
    emptotal = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.emptotal +=1

    def displayCount(self):
        print("Total No of Employees %d" % Employee.emptotal)

    def showEmployee(self):
        print("Employee Name :",self.name, " Salary:",self.salary)

"This would create first OBJECT of Employee Class"
emDetail1 =Employee("Yijie Zheng",8000)
"This would create second OBJECT of Employee Class"
emDetail2 = Employee("Ernie Duracell",9000)

emDetail1.showEmployee()
emDetail2.showEmployee()

print("Total Employee = %d"  % Employee.emptotal)

