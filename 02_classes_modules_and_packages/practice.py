

class Vehicle:
    def __init__(self, make, model):
        self.make=make
        self.model=model
    
    def display_info(self):
        print(f"Vehicle Make: {self.make}, Model: {self.model}")
    
    def update_model(self, model):
        self.model = model
        
        
my_car = Vehicle("Toyota", "Corolla")
my_car.display_info()

print(my_car.make)

my_car.update_model("Yaris")
my_car.display_info()

class Bicycle:
    def __init__(self, brand, gear_count=0):
        self.brand=brand
        self.gear_count=gear_count
    
    def display_specs(self):
        print(f"Brand name: {self.brand}, Gear count: {self.gear_count}")
        
my_bicycle=Bicycle("Kawasaki","6")
my_bicycle.display_specs()


class Garden:
    climate ="Temperate"
    
    def __init__(self, name):
        self.name=name
        self.plants=[]
        
    def plant_flower(self, flower):
        self.plants.append(flower)
        print(f"{flower} planted in {self.name}")
    
    @classmethod
    def change_climate(cls, new_climate):
        cls.climate=new_climate
        print(f"Garden climate changed to {new_climate}")
    
    @staticmethod
    def general_advice():
        print("Regular watering")
    
garden1=Garden("Tokyo")
garden2=Garden("Paris")

garden1.plants.append("Sakura")
garden2.plants.append("Panjii")

garden1.plant_flower("Momiji")
garden1.change_climate("Tropical")
garden1.general_advice()

#print(f"Garden name: {garden1.name}, Climate: {garden1.climate}")

#Garden.climate="Cold"

import time

class Timer:
    def __init__(self):
        self._start_time=None
        self._end_time=None
    
    def start(self):
        self._start_time=self._get_time()
    
    def stop(self):
        self._end_time=self._get_time()
    
    def elapsed_time(self):
        if self._start_time and self._end_time:
            return self._calculate_elapsed()
        else:
            return "Timer is not started or stopped yet!"
    
    def _calculate_elapsed(self):
        return self._end_time - self._start_time
    
    def _get_time(self):
        return time.time()

timer=Timer()
timer.start()
time.sleep(2)
timer.stop()

print(f"Elapsed Time: {timer.elapsed_time()} seconds.")

from datetime import datetime

current_time = datetime.now()
print(current_time)

