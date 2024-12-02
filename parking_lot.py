import threading
from typing import List

from level import Level
from vehicle import Vehicle


class ParkingLot:
    _instance = None
    _lock = threading.Lock()  # Lock object for thread-safety
    
    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ParkingLot._instance = self
            self.levels: List[Level] = []

    # Singelton Design Pattern
    # def __new__(cls):
    #     if not cls._instance:
    #         with cls._lock:
    #             if not cls._instance:
    #                 cls._instance = super().__new__(cls)

    #     return cls._instance

    # add levels
    def add_levels(self, level: Level):
        self.levels.append(level)
        
    def park_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True

        return False

    def unpark_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True

        return False

    def display_availability(self):
        for level in self.levels:
            level.display_availability()
        
    
    
    