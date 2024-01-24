from typing import Dict, NewType

from parking_lot.factories.parking_spot import ParkingSpotFactory
from parking_lot.exceptions.data_not_found_in_dict_exception import DataNotFoundInDictException
from .address import Address
from .parking_floor import ParkingFloor
from parking_lot.exceptions.invalid_parking_floor_exception import InvalidParkingFloorException

ParkingFloorDict = NewType('ParkingFloorDict', Dict[str, ParkingFloor])


class ParkingLot:

    def __init__(self, unique_id: int, name: str, address: Address):
        self._unique_id: int = unique_id
        self._name: str = name
        self._address: Address = address
        self._parking_floors: ParkingFloorDict = ParkingFloorDict({})

    def create_floor(self, floor_name: str, capacity: int,
                     spot_factories: Dict[str, ParkingSpotFactory]) -> ParkingFloor:
        if self.is_valid_floor(floor_name):
            all_floors: ParkingFloorDict = self.get_parking_floors()
            if floor_name not in all_floors:
                all_floors[floor_name] = ParkingFloor(floor_name, capacity, spot_factories)
            return self.get_floor(floor_name)

    def get_floor(self, floor_name: str) -> ParkingFloor:
        if not self.is_valid_floor(floor_name):
            raise InvalidParkingFloorException(floor_name)

        all_floors: ParkingFloorDict = self.get_parking_floors()

        if floor_name not in all_floors:
            raise DataNotFoundInDictException

        return all_floors[floor_name]

    def get_unique_id(self) -> int:
        return self._unique_id

    def get_name(self) -> str:
        return self._name

    def get_address(self) -> Address:
        return self._address

    def get_parking_floors(self) -> ParkingFloorDict:
        return self._parking_floors

    @classmethod
    def is_valid_floor(cls, floor_name: str):
        if isinstance(floor_name, str) and len(floor_name) > 0:
            return True
        else:
            raise InvalidParkingFloorException(floor_name)
