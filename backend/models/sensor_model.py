from sqlalchemy import Column, Integer, Float, String, DataTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()

class SensorData(Base):
    __tablename__ = 'sensor_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sensor_id = Column(String(50), nullable=False)
    temperature = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    pressure = Column(Float, nullable=True)
    air_pm2_5 = Column(Float, nullable=True)
    timestamp = Column(DataTime, default=datetime.now(datetime.UTC))

    def __repr__(self):
        return (f"<SensorData(id={self.id}, sensor_id='{self.sensor_id}', "
                f"temperature={self.temperature}, humidity={self.humidity}, "
                f"pressure={self.pressure}, air_pm2_5={self.air_pm2_5}"
                f"timestamp={self.timestamp})>")