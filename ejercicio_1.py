
import requests
import json
from loguru import logger

class GeoAPI:
    API_KEY = "d81015613923e3e435231f2740d5610b"
    LAT =  "-35.836948753554054"
    LON = "-61.870523905384076"
    
    @classmethod
    def is_hot_in_pehuajo(cls):
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={GeoAPI.LAT}&lon={GeoAPI.LON}&appid={GeoAPI.API_KEY}&units=metric'
        response = requests.get(url)
        if response.status_code == 200:
            try:
                data = json.loads(response.text)
                temp = data['main']['temp']
                
                if temp > 28:
                    return (True)
                else:
                    return(False)
            except Exception as ex:
                logger.info(ex)
        else:
            return logger.info(response.status_code)

        