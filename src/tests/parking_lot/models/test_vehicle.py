import unittest
from parking_lot.models.vehicle import Car, Truck, Motorcycle


class TestCar(unittest.TestCase):
    def test_create_car(self):
        registration_number, brand = "ABC123", "Toyota"
        car = Car(registration_number, brand)
        assert car.get_registration_number() == registration_number
        assert car.get_brand() == brand
        assert car.get_vehicle_type() == "Car"


class TestTruck(unittest.TestCase):
    def test_create_truck(self):
        registration_number = "STU123"
        truck = Truck(registration_number)
        assert truck.get_registration_number() == registration_number
        assert truck.get_vehicle_type() == "Truck"


class TestMotorcycle(unittest.TestCase):
    def test_create_motor_cycle(self):
        registration_number = "MNO123"
        motor_cycle = Motorcycle(registration_number)
        assert motor_cycle.get_registration_number() == registration_number
        assert motor_cycle.get_vehicle_type() == 'Motorcycle'
