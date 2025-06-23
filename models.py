# models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
import enum
from datetime import datetime

Base = declarative_base()

class AlertStatus(str, enum.Enum):
    NEW = "NEW"
    ACKNOWLEDGED = "ACKNOWLEDGED"
    RESOLVED = "RESOLVED"

class AlertType(str, enum.Enum):
    OFFLINE = "OFFLINE"
    CONNECTIVITY = "CONNECTIVITY"
    BATTERY = "BATTERY"
    CHECKING = "CHECKING"

class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String, nullable=False)

    readings = relationship("SensorReading", back_populates="sensor")
    alerts = relationship("Alert", back_populates="sensor")


class SensorReading(Base):
    __tablename__ = "sensor_readings"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, ForeignKey("sensors.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    noise_intensity = Column(Float)
    rsrq = Column(Float)
    last_update = Column(DateTime)
    battery_level = Column(Float)

    sensor = relationship("Sensor", back_populates="readings")


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    sensor_id = Column(Integer, ForeignKey("sensors.id"))
    type = Column(Enum(AlertType), nullable=False)
    status = Column(Enum(AlertStatus), default=AlertStatus.NEW)
    created_at = Column(DateTime, default=datetime.utcnow)

    sensor = relationship("Sensor", back_populates="alerts")
