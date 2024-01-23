from typing import Optional
from .vehicle import Vehicle


class ParkingSpot:
    number: int = None
    parked_vehicle: Optional[Vehicle] = None

    def __init__(self, number: int):
        self.number: int = number
        self.parked_vehicle: Optional[Vehicle] = None

    def park(self, vehicle: Vehicle) -> None:
        self.parked_vehicle = vehicle

    def vacate(self) -> None:
        self.parked_vehicle = None

    def is_available(self) -> bool:
        return self.parked_vehicle is None
