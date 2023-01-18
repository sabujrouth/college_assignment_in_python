class Vehicle:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):
    
    def fare(self):
        fare_car = self.capacity * 100 
        total_fare = fare_car + (0.1 *fare_car)
        return total_fare

School_bus = Bus("School Volvo", 50)
print("Total Bus fare is:", School_bus.fare())