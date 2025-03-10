import mariadb
from datetime import datetime


class MeteoDataWriter:
    def __init__(self, host, port, user, password, database):
        """
        Initialize the MeteoDataWriter with database connection parameters.
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
        self.connect_db()

    def connect_db(self):
        """
        Establish a connection to the MariaDB database.
        """
        try:
            self.connection = mariadb.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print("Database connection established.")
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB: {e}")
            self.connection = None

    def write_reading(self, temperature, humidity, pressure=None, wind_speed=None, timestamp=None):
        """
        Insert a new meteorological reading into the database.

        Parameters:
            temperature (float): Temperature value.
            humidity (float): Humidity value.
            pressure (float, optional): Pressure value.
            wind_speed (float, optional): Wind speed.
            timestamp (str, optional): Timestamp for the reading (e.g., 'YYYY-MM-DD HH:MM:SS').
                                       If None, the database default (e.g., NOW()) can be used.
        """
        if self.connection is None:
            print("No database connection available.")
            return

        # Depending on whether a timestamp is provided, choose the proper SQL query.
        if timestamp is None:
            query = """
                INSERT INTO readings (temperature, humidity, pressure, wind_speed)
                VALUES (?, ?, ?, ?)
            """
            params = (temperature, humidity, pressure, wind_speed)
        else:
            query = """
                INSERT INTO readings (timestamp, temperature, humidity, pressure, wind_speed)
                VALUES (?, ?, ?, ?, ?)
            """
            params = (timestamp, temperature, humidity, pressure, wind_speed)

        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print("Data inserted successfully.")
        except mariadb.Error as e:
            print(f"Error inserting data: {e}")

    def close(self):
        """
        Close the database connection.
        """
        if self.connection:
            self.connection.close()
            print("Database connection closed.")


# Example usage:
if __name__ == "__main__":
