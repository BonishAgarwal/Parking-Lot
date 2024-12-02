from vehicle import Vehicle
from vehicle_type import VehicleType

class Bike:
    def __init__(self, license_plate: int):
        super().__init__(license_plate, VehicleType.BIKE)
    
    def get_license_plate(self):
        return self.license_plate
    
    def get_type(self):
        return VehicleType.CAR