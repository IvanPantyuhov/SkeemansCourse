NAME = 'Vehicle'

class Vehicle:
    def __init__(self, brand, year_of_production, max_speed):
        self.brand = brand
        self.year_of_production = year_of_production
        self.max_speed = max_speed

    def __str__(self):
        print(f'{self.NAME} {self.brand} is moving with max speed {self.max_speed}')

class Bus(Vehicle):
    def __init__(self, brand, year_of_production,):
        super().__init__(brand, year_of_production, max_speed = 70)

    def move(self):
        print(f'Bus {self.brand} is moving with max speed {self.max_speed}')


    mercedes = Vehicle("Mercedes-Benz Tourismo", 2021, 150)
    isuzu = Vehicle("Isuzu Ataman", 2019, 170)
    setra = Vehicle("Setra TopClass", 2020, 180)

    mercedes.move()
    isuzu.move()
    setra.move()
