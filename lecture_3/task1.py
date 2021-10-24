class Vehicle:
    def __init__(self, brand, year_of_production, max_speed):
        self.brand = brand
        self.year_of_production = year_of_production
        self.max_speed = max_speed

    def move(self):
        print(f'{self.brand} is moving with max speed {self.max_speed}')

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

if __name__ == '__main__':
    bmw_b7 = Vehicle("BMW B7 Alphine", 2003, 311)
    toyota_gt86 = Vehicle("Toyota GT86", 2015, 275)
    landrover_defender = Vehicle("Land Rover Defender", 2021, 280)

    bmw_b7.move()
    toyota_gt86.move()
    landrover_defender.move()