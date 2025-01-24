class Station:
    def __init__(self,
                 query_time,
                 place_id,
                 place_name,
                 bikes,
                 empty_docks,
                 slots,
                 lat,
                 lon,
                 timestamp,
                 extra
                 ):
        self.query_time = query_time
        self.place_id = place_id
        self.place_name = place_name
        self.bikes = bikes
        self.empty_docks = empty_docks
        self.slots = slots
        self.lat = lat
        self.lon = lon
        self.timestamp = timestamp
        self.extra = extra

    def to_tuple(self):
        return (
            self.query_time, self.place_id, self.place_name, self.bikes,
            self.empty_docks, self.slots, self.lat, self.lon, self.timestamp, self.extra
        )
