import requests
from datetime import datetime
from models.station import Station


class APIClient:
    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return self._process_data(data)
        else:
            raise Exception(f"Failed to fetch data from API: {response.status_code}")

    @staticmethod
    def _process_data(data):
        stations = []
        for station in data['network']['stations']:
            station = Station(
                query_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                place_id=station['extra'].get("uid"),
                place_name=station['name'],
                bikes=station['free_bikes'],
                empty_docks=station['empty_slots'],
                slots=station['extra'].get("slots"),
                lat=station['latitude'],
                lon=station['longitude'],
                timestamp=station['timestamp'],
                extra=str(station['extra'])
            )
            stations.append(station)
        return stations
