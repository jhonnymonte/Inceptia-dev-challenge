from ejercicio_1 import GeoAPI as GEO
from loguru import logger
import unittest

class TestChallenge(unittest.TestCase):
    def test_geoAPI(self):
        resultado = GEO.is_hot_in_pehuajo()
        self.assertFalse(resultado)

    
if __name__ == '__main__':
    unittest.main()