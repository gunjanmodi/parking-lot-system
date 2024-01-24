from typing import Dict, NewType

from parking_lot.factories.parking_spot import ParkingSpotFactory
from parking_lot.models.parking_spot import ParkingSpot
from parking_lot.models.vehicle import Vehicle
from parking_lot.exceptions.invalid_parking_spot_exception import InvalidParkingSpotException
from parking_lot.exceptions.parking_spot_already_occupied_exception import ParkingSpotAlreadyOccupied
from parking_lot.exceptions.parking_spot_already_empty_exception import ParkingSpotAlreadyEmpty
from parking_lot.exceptions.data_not_found_in_dict_exception import DataNotFoundInDictException


ParkingSpotDict = NewType('ParkingFloorDict', Dict[int, ParkingSpot])


class ParkingFloor:

    def __init__(self, name: str, capacity: int, spot_factories: Dict[str, ParkingSpotFactory]) -> None:
        self.name: str = name
        self._parking_slots: ParkingSpotDict = ParkingSpotDict({})
        self._spot_factories: Dict[str, ParkingSpotFactory] = spot_factories
        self._capacity: int = capacity

    def add_spot_factory(self, spot_type: str, spot_factory: ParkingSpotFactory) -> None:
        self._spot_factories[spot_type] = spot_factory

    def create_spot(self, spot_number: int, spot_type: str) -> ParkingSpot:
        if spot_type not in self._spot_factories:
            raise ValueError(f"Spot type '{spot_type}' is not supported on this floor.")

        if self.is_valid_spot_number(spot_number):
            all_spots: ParkingSpotDict = self.get_parking_slots()
            if spot_number not in all_spots:
                all_spots[spot_number] = self._spot_factories[spot_type].create_parking_spot(spot_number)
            return all_spots[spot_number]

    def get_spot(self, spot_number: int) -> ParkingSpot:
        if self.is_valid_spot_number(spot_number):
            all_spots: ParkingSpotDict = self.get_parking_slots()
            if spot_number in all_spots:
                return all_spots[spot_number]
            else:
                raise DataNotFoundInDictException(spot_number)

    def is_valid_spot_number(self, slot_number: int) -> bool:
        if slot_number > self._capacity or slot_number <= 0:
            raise InvalidParkingSpotException(slot_number)
        return True

    def park_vehicle(self, vehicle: Vehicle, spot_number: int) -> ParkingSpot:
        parking_spot = self.get_spot(spot_number)

        if not parking_spot.is_available():
            raise ParkingSpotAlreadyOccupied(parking_spot.number)

        parking_spot.park(vehicle)

        return parking_spot

    def vacate_vehicle(self, spot_number) -> ParkingSpot:
        parking_spot: ParkingSpot = self.get_spot(spot_number)

        if parking_spot.is_available():
            raise ParkingSpotAlreadyEmpty(parking_spot.number)

        parking_spot.vacate()

        return parking_spot

    def get_parking_slots(self) -> ParkingSpotDict:
        return self._parking_slots
