import unittest

from parking_lot.models.parking_floor import ParkingFloor
from parking_lot.exceptions.invalid_parking_floor_exception import InvalidParkingFloorException
from parking_lot.models.parking_lot import ParkingLot
from tests.parking_lot.models.test_parking_lot import create_parking_lot_1, get_parking_lot_data_1


def generate_parking_floor_1() -> ParkingFloor:
    parking_lot = ParkingLot(**get_parking_lot_data_1())
    parking_lot.create_floor("A1", 50)
    return parking_lot.get_floor("A1")


class ParkingSpot(unittest.TestCase):

    def test_create_valid_parking_floor(self):
        parking_lot: ParkingLot = create_parking_lot_1()
        name: str = "A1"
        capacity: int = 30
        parking_lot.create_floor(name, capacity)
        assert parking_lot.get_floor(name).name == name

    def test_create_invalid_parking_floor(self):
        parking_lot: ParkingLot = create_parking_lot_1()
        name: str = ""
        capacity: int = 30
        with self.assertRaises(InvalidParkingFloorException):
            parking_lot.create_floor(name, capacity)

    def test_create_invalid_parking_floor_zero_capacity(self):
        # TODO
        assert True
