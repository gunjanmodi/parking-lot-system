from abc import ABC, abstractmethod

from parking_lot.models.parking_spot import ParkingSpot
from parking_lot.models.parking_spot import CarParkingSpot
from parking_lot.models.parking_spot import TruckParkingSpot
from parking_lot.models.parking_spot import MotorCycleSpot


class ParkingSpotFactory(ABC):
    @abstractmethod
    def create_parking_spot(self, spot_number: int) -> ParkingSpot:
        pass


class CarParkingSpotFactory(ParkingSpotFactory):
    def create_parking_spot(self, spot_number: int) -> ParkingSpot:
        return CarParkingSpot(spot_number)


class TruckParkingSpotFactory(ParkingSpotFactory):
    def create_parking_spot(self, spot_number: int) -> ParkingSpot:
        return TruckParkingSpot(spot_number)


class MotorcycleSpotFactory(ParkingSpotFactory):
    def create_parking_spot(self, spot_number: int) -> ParkingSpot:
        return MotorCycleSpot(spot_number)
