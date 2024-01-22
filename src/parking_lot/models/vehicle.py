from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_registration_number(self) -> str:
        pass

    @abstractmethod
    def get_vehicle_type(self) -> str:
        pass


class Car(Vehicle):
    def __init__(self, license_plate, brand):
        self._registration_number = license_plate
        self._brand = brand

    def get_registration_number(self) -> str:
        return self._registration_number

    def get_vehicle_type(self) -> str:
        return "Car"

    def get_brand(self) -> str:
        return self._brand


class Truck(Vehicle):
    def __init__(self, registration_number):
        self._registration_number = registration_number

    def get_registration_number(self) -> str:
        return self._registration_number

    def get_vehicle_type(self) -> str:
        return "Truck"


class Motorcycle(Vehicle):
    def __init__(self, registration_number):
        self._registration_number = registration_number

    def get_registration_number(self) -> str:
        return self._registration_number

    def get_vehicle_type(self) -> str:
        return "Motorcycle"
