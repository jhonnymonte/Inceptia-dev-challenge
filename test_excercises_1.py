from ejercicio_1 import GeoAPI as GEO
from ejercicio_2 import is_product_available
from ejercicio_3 import validate_discount_code
from loguru import logger
import unittest

class TestChallenge(unittest.TestCase):
    def test_is_available_False(self):
        resultado = is_product_available("Granizado",20)
        self.assertFalse(resultado)

   
    def test_geoAPI(self):
        resultado = GEO.is_hot_in_pehuajo()
        self.assertFalse(resultado)

    def test_validate_discount(self):
        resultado = validate_discount_code("inceptia")
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()
