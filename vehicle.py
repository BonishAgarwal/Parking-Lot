from abc import ABC, abstractmethod
from vehicle_type import VehicleType

class Vehicle:
    def __init__(self, license_plate: int, type: VehicleType):
        self.license_plate = license_plate
        self.type = type
    
    @abstractmethod
    def get_license_plate(self):
        pass
    
    @abstractmethod
    def get_type(self):
        pass
    
    