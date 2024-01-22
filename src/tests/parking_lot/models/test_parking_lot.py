import unittest

from typing import List, Dict, Any
from parking_lot.models.parking_lot import ParkingLot
from parking_lot.models.parking_spot import ParkingSpot
from parking_lot.models.address import Address
from parking_lot.models.vehicle import Car
from .test_address import create_address_1
from parking_lot.exceptions.invalid_parking_spot_exception import InvalidParkingSpotException
from parking_lot.exceptions.parking_spot_already_occupied_exception import ParkingSpotAlreadyOccupied
from parking_lot.exceptions.parking_spot_already_empty_exception import ParkingSpotAlreadyEmpty


def _generate_parking_lot_1(unique_id: int, name: str, address: Address, capacity: int):
    return ParkingLot(unique_id, name, address, capacity)


def _generate_parking_slot_1():
    return ParkingSpot(1)


class TestParkingLot(unittest.TestCase):
    def setUp(self) -> None:
        self.parking_lot_1_data: Dict[str, Any] = {'unique_id': 1, 'name': 'Mandal Nagar Parking Lot',
                                                   'address': create_address_1(), 'capacity': 1000}

    def test_create_parking_lot(self):
        parking_lot: ParkingLot = _generate_parking_lot_1(**self.parking_lot_1_data)
        assert parking_lot.get_unique_id() == self.parking_lot_1_data['unique_id']
        assert parking_lot.get_name() == self.parking_lot_1_data['name']
        assert parking_lot.get_address() == self.parking_lot_1_data['address']
        assert parking_lot.get_capacity() == self.parking_lot_1_data['capacity']

    def test_add_valid_parking_spot(self):
        parking_lot: ParkingLot = _generate_parking_lot_1(**self.parking_lot_1_data)
        number: int = 11
        parking_lot.create_parking_spot(number)
        assert parking_lot.get_parking_spot(number).number == number

    def test_invalid_parking_spot(self):
        parking_lot: ParkingLot = _generate_parking_lot_1(**self.parking_lot_1_data)
        numbers: List[int] = [-3, 4001]
        for number in numbers:
            with self.assertRaises(InvalidParkingSpotException):
                parking_lot.create_parking_spot(number)

    def test_park_vehicle(self):
        car: Car = Car("ABC123", "Toyota")
        parking_lot: ParkingLot = _generate_parking_lot_1(**self.parking_lot_1_data)
        parking_lot.park_vehicle(car, 45)

    def test_vacate_vehicle(self):
        car: Car = Car("ABC123", "Toyota")
        spot_number: int = 45
        parking_lot: ParkingLot = _generate_parking_lot_1(**self.parking_lot_1_data)
        parking_lot.park_vehicle(car, spot_number)

        parking_lot.vacate_vehicle(spot_number)

    def test_park_vehicle_in_occupied_spot(self):
        spot_number: int = 45
        parking_lot: ParkingLot = _generate_parking_lot_1(**self.parking_lot_1_data)

        car: Car = Car("ABC123", "Toyota")
        parking_lot.park_vehicle(car, spot_number)

        car: Car = Car("PQR897", "Hyundai")
        with self.assertRaises(ParkingSpotAlreadyOccupied):
            parking_lot.park_vehicle(car, spot_number)

    def test_trying_vacate_empty_spot(self):
        spot_number: int = 45
        parking_lot: ParkingLot = _generate_parking_lot_1(**self.parking_lot_1_data)

        with self.assertRaises(ParkingSpotAlreadyEmpty):
            parking_lot.vacate_vehicle(spot_number)

    def test_parking_spot_at_higher_than_capacity(self):
        spot_number: int = 2001
        parking_lot: ParkingLot = _generate_parking_lot_1(**self.parking_lot_1_data)

        car: Car = Car("ABC123", "Toyota")
        with self.assertRaises(InvalidParkingSpotException):
            parking_lot.park_vehicle(car, spot_number)

    def test_parking_spot_at_invalid_spot_number(self):
        spot_number: int = -3
        parking_lot: ParkingLot = _generate_parking_lot_1(**self.parking_lot_1_data)

        car: Car = Car("ABC123", "Toyota")
        with self.assertRaises(InvalidParkingSpotException):
            parking_lot.park_vehicle(car, spot_number)

    def test_trying_vacate_invalid_spot(self):
        spot_number: int = -30
        parking_lot: ParkingLot = _generate_parking_lot_1(**self.parking_lot_1_data)

        with self.assertRaises(InvalidParkingSpotException):
            parking_lot.vacate_vehicle(spot_number)

