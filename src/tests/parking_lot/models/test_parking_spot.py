import unittest
from typing import List

from parking_lot.models.parking_lot import ParkingLot
from tests.parking_lot.models.test_parking_lot import get_parking_lot_data_1
from tests.parking_lot.models.test_parking_floor import spot_factories

from parking_lot.models.vehicle import Car, Truck, Motorcycle

from parking_lot.exceptions.invalid_parking_spot_exception import InvalidParkingSpotException
from parking_lot.exceptions.parking_spot_already_occupied_exception import ParkingSpotAlreadyOccupied
from parking_lot.exceptions.parking_spot_already_empty_exception import ParkingSpotAlreadyEmpty
from parking_lot.exceptions.invalid_parking_spot_type_exception import InvalidParkingSpotTypeException


class TestParkingSpot(unittest.TestCase):
    def setUp(self) -> None:
        self.parking_lot = ParkingLot(**get_parking_lot_data_1())
        self.floor = self.parking_lot.create_floor("A1", 50, spot_factories)

    def test_add_valid_parking_spot(self):
        number: int = 11
        self.floor.create_spot(number, "car")
        assert self.floor.get_spot(number).number == number

    def test_invalid_parking_spot(self):
        numbers: List[int] = [-3, 4001]
        for number in numbers:
            with self.assertRaises(InvalidParkingSpotException):
                self.floor.create_spot(number, "car")

    def test_park_vehicle(self):
        car: Car = Car("ABC123", "Toyota")
        spot_number: int = 45
        self.floor.create_spot(spot_number, "car")

        self.floor.park_vehicle(car, spot_number)
        spot = self.floor.get_spot(spot_number)
        assert spot.is_available() is not None

    def test_vacate_vehicle(self):
        car: Car = Car("ABC123", "Toyota")
        spot_number: int = 45
        self.floor.create_spot(spot_number, "car")

        self.floor.park_vehicle(car, spot_number)
        self.floor.vacate_vehicle(spot_number)

        spot = self.floor.get_spot(spot_number)
        assert spot.is_available() is not None

    def test_park_vehicle_in_occupied_spot(self):
        spot_number: int = 45
        car: Car = Car("ABC123", "Toyota")

        self.floor.create_spot(spot_number, "car")

        self.floor.park_vehicle(car, spot_number)

        car: Car = Car("PQR897", "Hyundai")
        with self.assertRaises(ParkingSpotAlreadyOccupied):
            self.floor.park_vehicle(car, spot_number)

    def test_trying_vacate_empty_spot(self):
        spot_number: int = 30
        self.floor.create_spot(spot_number, "truck")

        with self.assertRaises(ParkingSpotAlreadyEmpty):
            self.floor.vacate_vehicle(spot_number)

    def test_parking_spot_at_higher_than_capacity(self):
        spot_number: int = 151
        car: Car = Car("ABC123", "Toyota")

        with self.assertRaises(InvalidParkingSpotException):
            self.floor.create_spot(spot_number, "car")
            self.floor.park_vehicle(car, spot_number)

    def test_parking_spot_at_invalid_spot_number(self):
        spot_number: int = -3

        car: Car = Car("ABC123", "Toyota")
        with self.assertRaises(InvalidParkingSpotException):
            self.floor.park_vehicle(car, spot_number)

    def test_trying_vacate_invalid_spot(self):
        spot_number: int = -30

        with self.assertRaises(InvalidParkingSpotException):
            self.floor.vacate_vehicle(spot_number)

    def test_trying_to_park_car_into_motorcycle_spot(self):
        spot_number: int = 5
        self.floor.create_spot(spot_number, "motorcycle")

        car: Car = Car("ABC123", "Toyota")
        with self.assertRaises(InvalidParkingSpotTypeException):
            self.floor.park_vehicle(car, spot_number)

    def test_trying_to_park_motorcycle_into_truck_spot(self):
        spot_number: int = 49
        self.floor.create_spot(spot_number, "truck")

        motorcycle: Motorcycle = Motorcycle("DEF123")
        with self.assertRaises(InvalidParkingSpotTypeException):
            self.floor.park_vehicle(motorcycle, spot_number)

    def test_trying_to_park_truck_into_car_spot(self):
        spot_number: int = 49
        truck: Truck = Truck("STU123")

        self.floor.create_spot(spot_number, "car")

        with self.assertRaises(InvalidParkingSpotTypeException):
            self.floor.park_vehicle(truck, spot_number)
