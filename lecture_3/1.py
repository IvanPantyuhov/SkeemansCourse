class Vehicle:
    def __init__(self, brand, year_of_production, max_speed):
        self.brand = brand
        self.year_of_production = year_of_production
        self.max_speed = max_speed

    def move(self):
        print(f'{self.brand} is moving with max speed {self.max_speed}!')

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

    @property
    def max_speed_squared(self):
        return self.max_speed ** 2


class Bus(Vehicle):

    def move(self):
        return f'Bus {self.brand} is moving!'


if __name__ == '__main__':
    chevrolet_camaro = Vehicle("Chevrolet Camaro", 1977, 240)
    chevrolet_camaro.move()

    bmw = Vehicle("BMW", 1977, 240)

    bmw.set_max_speed(70)
    print(bmw.max_speed_squared)

    concorde = Vehicle("Concorde", 1965, 2179)
    hms_defender = Vehicle("HMS Defender", 2006, 59)

    some_bus = Bus('BMW', 2008, 70)

    chevrolet_camaro.move()
    concorde.move()
    hms_defender.move()
    some_bus.move()