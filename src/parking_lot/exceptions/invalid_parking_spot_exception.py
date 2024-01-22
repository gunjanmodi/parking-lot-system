from .parking_lot_exception import ParkingLotException


class InvalidParkingSpotException(ParkingLotException):
    def __init__(self, spot_number: int):
        self.spot_number: int = spot_number
        super().__init__(f"Invalid parking spot number: {spot_number}")
