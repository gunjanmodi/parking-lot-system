from typing import Dict
from .address import Address
from .parking_spot import ParkingSpot
from .vehicle import Vehicle
from ..exceptions.invalid_parking_spot_exception import InvalidParkingSpotException
from ..exceptions.parking_spot_already_occupied_exception import ParkingSpotAlreadyOccupied
from ..exceptions.parking_spot_already_empty_exception import ParkingSpotAlreadyEmpty


class ParkingLot:

    def __init__(self, unique_id: int, name: str, address: Address, capacity: int):
        self._unique_id: int = unique_id
        self._name: str = name
        self._address: Address = address
        self._capacity: int = capacity
        self._parking_slots: Dict[int, ParkingSpot] = {}

    def create_parking_spot(self, spot_number: int) -> None:
        if self.is_valid_spot_number(spot_number):
            all_spots: Dict[int, ParkingSpot] = self.get_parking_slots()
            if spot_number not in all_spots:
                self._parking_slots[spot_number] = ParkingSpot(spot_number)

    def get_parking_spot(self, spot_number: int) -> ParkingSpot:
        if self.is_valid_spot_number(spot_number):
            all_spots: Dict[int, ParkingSpot] = self.get_parking_slots()
            if spot_number not in all_spots:
                self.create_parking_spot(spot_number)
            return all_spots[spot_number]

    def is_valid_spot_number(self, slot_number: int) -> bool:
        if slot_number > self._capacity or slot_number <= 0:
            raise InvalidParkingSpotException(slot_number)
        return True

    def park_vehicle(self, vehicle: Vehicle, spot_number: int) -> ParkingSpot:
        parking_spot: ParkingSpot = self.get_parking_spot(spot_number)

        if not parking_spot.is_available():
            raise ParkingSpotAlreadyOccupied(parking_spot.number)

        parking_spot.park(vehicle)

        return parking_spot

    def vacate_vehicle(self, spot_number) -> ParkingSpot:
        parking_spot: ParkingSpot = self.get_parking_spot(spot_number)

        if parking_spot.is_available():
            raise ParkingSpotAlreadyEmpty(parking_spot.number)

        parking_spot.vacate()

        return parking_spot

    def get_parking_slots(self) -> Dict[int, ParkingSpot]:
        return self._parking_slots

    def get_unique_id(self) -> int:
        return self._unique_id

    def get_name(self) -> str:
        return self._name

    def get_address(self) -> Address:
        return self._address

    def get_capacity(self) -> int:
        return self._capacity
