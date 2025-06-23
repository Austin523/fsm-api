# schemas.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from models import AlertType, AlertStatus

class AlertSchema(BaseModel):
    id: int
    sensor_id: int
    type: AlertType
    status: AlertStatus
    created_at: datetime
    location: Optional[str] = None  # from JOIN

    class Config:
        from_attributes = True  # equivalent to old orm_mode = True
