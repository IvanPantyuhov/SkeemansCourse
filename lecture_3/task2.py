class Vehicle:
    def __init__(self, brand, year, max_speed):
        self.brand = brand
        self.year = year
        self.max_speed = max_speed

    def move(self):
        print(f'Vehicle {self.brand} is moving with max speed {self.max_speed}!')

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

class Bus(Vehicle):

    def move(self):
        return f'Bus {self.brand} is moving '