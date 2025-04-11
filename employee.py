
class Employee:
    def __init__(self, name, age, position=None, salary=None):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
    
    def __str__(self):
        return f"Employee(Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: {self.salary})"
