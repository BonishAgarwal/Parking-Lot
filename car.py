from vehicle import Vehicle
from vehicle_type import VehicleType

class Car:
    def __init__(self, license_plate: int):
        super().__init__(license_plate, VehicleType.CAR)
    
    def get_license_plate(self):
        return self.license_plate
    
    def get_type(self):
        return VehicleType.CAR