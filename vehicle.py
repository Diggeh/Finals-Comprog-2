# vehicle.py
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def vehicle_info(self):
        return f"{self.year} {self.make} {self.model}"

class SchoolBus(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

    def vehicle_info(self):
        return f"School Bus: {self.year} {self.make} {self.model} with capacity of {self.capacity} students"
        
    def is_instance_of_vehicle(self):
        return isinstance(self, Vehicle)
