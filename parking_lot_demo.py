from car import Car
from level import Level
from parking_lot import ParkingLot


class Demo:
    
    def run(self):
        
        level1 = Level(1, 50)
        level2 = Level(2, 10)
        level3 = Level(1, 20)
        
        p = ParkingLot()
        p.add_levels(level1)
        p.add_levels(level2)
        p.add_levels(level3)
        
        car = Car("ABC123")
        
        p.park_vehicle(car)
        
        p.display_availability()

demo = Demo()
demo.run()