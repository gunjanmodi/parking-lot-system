from .parking_lot_exception import ParkingLotException


class DataNotFoundInDictException(ParkingLotException):
    def __init__(self, key):
        self.message = f"Data with key '{key}' does not exist in the dictionary."
        super().__init__(self.message)