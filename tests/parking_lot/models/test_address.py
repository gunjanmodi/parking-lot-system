import unittest
from parking_lot.models.address import Address


def create_address_1():
    return Address('H.No. 06', 'Kumar Marg', 'Jaipur', 'Rajasthan', 'India')


class TestAddress(unittest.TestCase):

    def test_create_address(self):
        address = create_address_1()
        assert address.line_1 == 'H.No. 06'
        assert address.line_2 == 'Kumar Marg'
        assert address.city == 'Jaipur'
        assert address.state == 'Rajasthan'
        assert address.country == 'India'

