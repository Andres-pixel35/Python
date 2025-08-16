class Vehicle:
    def __init__(self, make, model, year: int, fuel_level=100, engine_running=False):
        self.make = make
        self.model = model
        self.year = year
        self.fuel_level = fuel_level
        self.engine_running = engine_running

    def start_engine(self):
        if self.engine_running == True:
            print("The engine is already running")
        elif self.fuel_level < 25:
            print(f"You need at least 25 fuel in your tank to start the vehicle and your tank has {self.fuel_level} fuel right now")
        else:
            self.engine_running = True
            self.fuel_level = self.fuel_level - 25
            print("Engine started")
    
    def stop_engine(self):
        if self.engine_running == False:
            print("The engine is already stop")
        else:
            self.engine_running = False
            print("Engine stopped")

    def refuel(self, amount: float):
        if self.fuel_level == 100:
            print("The tank is full, you can not add more fuel")
        elif self.fuel_level + amount > 100:
            print(f"Your tank can not be over 100, your tank has {self.fuel_level} fuel and you tried to add {amount}")
        else:
            self.fuel_level = self.fuel_level + amount
            print(f"The tank has refuelled {amount} fuel successfully, taking your tank to {self.fuel_level}")

    def get_info(self):
        return f"Make: {self.make}. Model: {self.model}. Year: {self.year}"
    

class Car(Vehicle):
    def __init__(self, make, model, year: int, fuel_level=100, engine_running=False, trunk_open=False):
        super().__init__(make, model, year, fuel_level, engine_running)
        self.trunk_open = trunk_open

    def start_engine(self):
        was_running = self.engine_running
        super().start_engine()
        if not was_running and self.engine_running:
            print("Car engine started with a purr")

    def open_trunk(self):
        if self.trunk_open:
            print("The trunk is already open")
        else: 
            self.trunk_open = True
            print("Trunk opened")
    
    def close_trunk(self):
        if not self.trunk_open:
            print("The trunk is already closed")
        else:
            self.trunk_open = False
            print("Trunk closed")
    
class Motorcycle(Vehicle):
    def __init__(self, make, model, year: int, fuel_level=100, engine_running=False):
        super().__init__(make, model, year, fuel_level, engine_running)

    def start_engine(self):
        was_runnning = self.engine_running
        super().start_engine()
        if not was_runnning and self.engine_running:
            print("Motorcycle engine roared to life")
    
    def wheelie(self):
        if self.fuel_level > 10:
            self.fuel_level = self.fuel_level - 10
            print("Performing a wheelie!")
        else:
            print(f"The motorcycle {self.make} need at leat 10 fuel to perform this action, and you have {self.fuel_level} right now")

class Truck(Vehicle):
    def __init__(self, make, model, year: int, cargo_capacity: int, current_load = 0,fuel_level=100, engine_running=False):
        super().__init__(make, model, year, fuel_level, engine_running)
        self.cargo_capacity = cargo_capacity
        self.current_load = current_load
    
    def start_engine(self):
        was_running = self.engine_running
        super().start_engine()
        if not was_running and self.engine_running:
            print("Truck engine rumbled to life")
        
    def load_cargo(self, weight):
        if self.current_load == self.cargo_capacity:
            print(f"You can not load more to the cargo since it's full, your cargo capacity is {self.cargo_capacity}")
        elif self.current_load + weight > self.cargo_capacity:
            print(f"You tried to load ({weight}), but that plus your current load ({self.current_load})" 
                 f" overpass your cargo capacity ({self.cargo_capacity})")
            
        else:
            self.current_load = self.current_load + weight
            print(f"Your current load after add {weight} is {self.current_load}")

    def unload_cargo(self):
        if self.current_load == 0:
            print("You can not unload since you current load is 0")
        else:
            self.current_load = 0
            print("You have successfully unload all your cargo!")

# Test script for Vehicle inheritance exercise
print("=== VEHICLE INHERITANCE TEST ===\n")

# Create instances
print("1. Creating vehicles...")
car = Car("Toyota", "Camry", 2023)
motorcycle = Motorcycle("Harley-Davidson", "Street Glide", 2022)
truck = Truck("Ford", "F-150", 2024, 1000)

print(f"Car created: {car.make} {car.model}")
print(f"Motorcycle created: {motorcycle.make} {motorcycle.model}")
print(f"Truck created: {truck.make} {truck.model}")

print("\n" + "="*50)

# Test basic vehicle info
print("\n2. Testing get_info() method...")
print("Car info:", car.get_info())
print("Motorcycle info:", motorcycle.get_info())
print("Truck info:", truck.get_info())

print("\n" + "="*50)

# Test engine starting (should show different messages)
print("\n3. Testing start_engine() - should show different messages...")
car.start_engine()
motorcycle.start_engine()
truck.start_engine()

print("\n" + "="*50)

# Test starting engine when already running
print("\n4. Testing start_engine() when already running...")
car.start_engine()
motorcycle.start_engine()
truck.start_engine()

print("\n" + "="*50)

# Test stopping engines
print("\n5. Testing stop_engine()...")
car.stop_engine()
motorcycle.stop_engine()
truck.stop_engine()

print("\n" + "="*50)

# Test class-specific methods
print("\n6. Testing class-specific methods...")
car.start_engine()  # Start car again
car.open_trunk()
car.close_trunk()
car.close_trunk()

motorcycle.start_engine()  # Start motorcycle
motorcycle.wheelie()

truck.start_engine()  # Start truck
truck.load_cargo(500)
truck.load_cargo(600)  # This should exceed capacity
truck.unload_cargo()

print("\n" + "="*50)

# Test fuel system
print("\n7. Testing fuel system...")
print(f"Motorcycle fuel before: {motorcycle.fuel_level}")
motorcycle.fuel_level = 5  # Set low fuel
motorcycle.wheelie()  # Should not work with low fuel
motorcycle.refuel(50)
print(f"Motorcycle fuel after refuel: {motorcycle.fuel_level}")

print("\n" + "="*50)

# Test inheritance - accessing parent methods
print("\n8. Testing inheritance - parent methods on child objects...")
print("Car refueling...")
car.refuel(20)
print("Truck refueling...")
truck.refuel(30)

print("\n" + "="*50)

print("=== TEST COMPLETED ===")
