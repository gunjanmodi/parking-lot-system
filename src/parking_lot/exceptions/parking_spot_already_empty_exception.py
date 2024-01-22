from .parking_lot_exception import ParkingLotException


class ParkingSpotAlreadyEmpty(ParkingLotException):
    def __init__(self, spot_number: int):
        self.spot_number: int = spot_number
        super().__init__(f"Parking spot {spot_number} already empty")
