from vehicle import Vehicle
from vehicle_type import VehicleType

class ParkingSpot:
    
    def __init__(self, spot_number: int):
        self.spot_number = spot_number
        self.vehicle_type = VehicleType.CAR
        self.parked_vehicle = False
    
    def get_spot_number(self):
        return self.spot_number
    
    def get_vehicle_type(self):
        self.vehicle_type
    
    def park_vehicle(self, vehicle: Vehicle):
        if self.is_available() and self.vehicle_type == Vehicle.get_type():
            self.parked_vehicle = True

    def unpark_vehicle(self):
        self.parked_vehicle = False

    def is_available(self):
        return self.parked_vehicle == False