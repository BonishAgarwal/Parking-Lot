from typing import List
from parking_spot import ParkingSpot
from vehicle import Vehicle


class Level:
    
    def __init__(self, floor: int, num_spots: int):
        self.floor = floor # to maintain the level number
        self.spots: List[ParkingSpot] = [ParkingSpot(i) for i in range(1, num_spots+1)]
    
    def add_parking_spot(self):
        self.spots += self.spots + ParkingSpot(len(self.spots) + 1)
    
    def park_vehicle(self, vehicle: Vehicle):
        for spot in self.spots:
            if spot.is_available() and spot.vehicle_type == vehicle.get_type():
                spot.park_vehicle(vehicle)
                return True

        return False
    
    def unpark_vehicle(self, vehicle: Vehicle):
        for spot in self.spots:
            if not spot.is_available() and spot.vehicle_type == vehicle.get_type():
                spot.unpark_vehicle()
                return True
        
        return False
    
    def display_availability(self):
        for spot in self.spots:
            if spot.is_available():
                print(spot.get_spot_number())