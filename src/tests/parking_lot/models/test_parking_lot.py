import unittest

from typing import Dict, Any
from parking_lot.models.parking_lot import ParkingLot
from .test_address import create_address_1


def get_parking_lot_data_1():
    return {'unique_id': 1, 'name': 'Mandal Nagar Parking Lot', 'address': create_address_1()}


def create_parking_lot_1():
    return ParkingLot(**get_parking_lot_data_1())


class TestParkingLot(unittest.TestCase):
    def setUp(self) -> None:
        self.parking_lot_1_data: Dict[str, Any] = get_parking_lot_data_1()

    def test_create_parking_lot(self):
        parking_lot: ParkingLot = create_parking_lot_1()
        assert parking_lot.get_unique_id() == self.parking_lot_1_data['unique_id']
        assert parking_lot.get_name() == self.parking_lot_1_data['name']
