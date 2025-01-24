import sqlite3


class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def connect(self):
        self.conn = sqlite3.connect(self.db_path, timeout=10)
        self.cursor = self.conn.cursor()
        self.cursor.execute('PRAGMA journal_mode=WAL;')
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS stations (
                query_time TEXT,
                place_id TEXT,
                place_name TEXT,
                bikes INTEGER,
                empty_docks INTEGER,
                slots INTEGER,
                lat REAL,
                lon REAL,
                timestamp TEXT,
                extra TEXT
            )
        ''')

    def insert_stations(self, stations):
        for station in stations:
            self.cursor.execute('''
                INSERT INTO stations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', station.to_tuple())
        self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
