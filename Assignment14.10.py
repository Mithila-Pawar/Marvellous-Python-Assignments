class Employee:
    def __init__(self, name, department, salary):
        self.name = name                
        self._department = department   
        self.__salary = salary         

    def display(self):
        print(f"Name (Public): {self.name}")
        print(f"Department (Protected): {self._department}")
        print(f"Salary (Private): {self.__salary}")

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
        else:
            print("Invalid salary")

emp = Employee("John", "IT", 50000)
emp.display()

print("\nAccess public attribute:", emp.name)
print("Access protected attribute:", emp._department)
print("Access private attribute via getter:", emp.get_salary())
emp.set_salary(60000)
print("Updated salary via getter:", emp.get_salary())
