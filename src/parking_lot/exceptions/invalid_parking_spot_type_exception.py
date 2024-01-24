from .parking_lot_exception import ParkingLotException
from parking_lot.models.vehicle import Vehicle


class InvalidParkingSpotTypeException(ParkingLotException):
    def __init__(self, spot_number: int, vehicle: Vehicle):
        self.spot_number: int = spot_number
        super().__init__(f"Invalid parking spot type for vehicle {vehicle.get_vehicle_type()} in {spot_number}")
