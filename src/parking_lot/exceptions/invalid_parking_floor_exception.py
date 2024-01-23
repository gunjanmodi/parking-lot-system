from .parking_lot_exception import ParkingLotException


class InvalidParkingFloorException(ParkingLotException):
    def __init__(self, floor_name: str):
        self.floor_name: str = floor_name
        super().__init__(f"Invalid parking floor: {floor_name}")
