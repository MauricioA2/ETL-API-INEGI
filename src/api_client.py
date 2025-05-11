import requests
from src.config import INEGI_API_KEY

class InegiAPIClient:
    BASE_URL = 'https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR'

    def __init__(self, series_ids):
        self.series_ids = series_ids

    def fetch_series(self, series_id):
        url = f'{self.BASE_URL}/{series_id}/es/0700/false/BISE/{INEGI_API_KEY}?type=json'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def fetch_all(self):
        data = {}
        for name, serie_id in self.series_ids.items():
            json_data = self.fetch_series(serie_id)
            data[name] = json_data
        return data