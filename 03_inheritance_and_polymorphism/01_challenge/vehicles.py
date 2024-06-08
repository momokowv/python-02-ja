# ここにコードを書いてください
class Vehicle:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        
    def get_details(self):
        pass
        

class Car(Vehicle):
    def get_details(self):
        return f"Car: {self.year} {self.make} {self.model}"

class Truck(Vehicle):
    def __init__(self, make, model, year, towing_capacity):
        self.make=make
        self.model=model
        self.year=year
        self.towing_capacity=towing_capacity
    
    def get_details(self):
        return f"Truck: {self.year} {self.make} {self.model}, Towing Capacity: {self.towing_capacity}"

def get_vehicle_details(vehicle):
    # ここにコードを書いてください
    pass

def display_vehicle_details(vehicle):
    if vehicle is None or vehicle == "":
        raise TypeError("Invalid argument. Must not be None or an empty string.")
    if not vehicle.make or vehicle.year =="0":
        raise TypeError("Invalid vehicle details. 'make' and 'year' must not be empty or zero.")
    if isinstance(vehicle, Vehicle):
        print(vehicle.get_details())
    else:
        raise TypeError("Invalid argument. Must be a Vehicle object or its subclass.")


if __name__ == "__main__":
    car = Car(make="Toyota", model="Corolla", year=2021)
    truck = Truck(make="Ford", model="F-150", year=2020, towing_capacity=5000)

    print(car.get_details())  # Car: 2021 Toyota Corolla
    print(truck.get_details())  # Truck: 2020 Ford F-150, Towing Capacity: 5000

    display_vehicle_details(car)  # Car: 2021 Toyota Corolla
    display_vehicle_details(truck)  # Truck: 2020 Ford F-150, Towing Capacity: 5000