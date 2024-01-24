from abc import ABC, abstractmethod
from typing import Optional
from parking_lot.exceptions.invalid_parking_spot_type_exception import InvalidParkingSpotTypeException
from .vehicle import Vehicle, Car, Truck, Motorcycle


class ParkingSpot(ABC):
    number: int = None
    parked_vehicle: Optional[Vehicle] = None

    def __init__(self, number: int):
        self.number: int = number
        self.parked_vehicle: Optional[Vehicle] = None

    def park(self, vehicle: Vehicle) -> None:
        if self.is_valid_for_vehicle(vehicle):
            self.parked_vehicle = vehicle
        else:
            raise InvalidParkingSpotTypeException(self.number, vehicle)

    def vacate(self) -> None:
        self.parked_vehicle = None

    def is_available(self) -> bool:
        return self.parked_vehicle is None

    @abstractmethod
    def is_valid_for_vehicle(self, vehicle: Vehicle):
        pass


class CarParkingSpot(ParkingSpot):

    def is_valid_for_vehicle(self, vehicle: Vehicle) -> bool:
        return isinstance(vehicle, Car)


class TruckParkingSpot(ParkingSpot):

    def is_valid_for_vehicle(self, vehicle: Vehicle) -> bool:
        return isinstance(vehicle, Truck)


class MotorCycleSpot(ParkingSpot):
    def is_valid_for_vehicle(self, vehicle: Vehicle) -> bool:
        return isinstance(vehicle, Motorcycle)
