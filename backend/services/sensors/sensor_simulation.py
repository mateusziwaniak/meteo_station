from abc import ABC, abstractmethod


class BaseSensor(ABC):

    def __init__(self, sensor_id: str, location:str):
        self.sensor_id = sensor_id
        self.location = location


    @abstractmethod
    def read_data(self):
        pass