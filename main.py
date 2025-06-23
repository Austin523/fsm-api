from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Alert
from schemas import AlertSchema
from typing import List

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FSM API is running"}

@app.get("/alerts/latest/", response_model=List[AlertSchema])
def get_latest_alerts(db: Session = Depends(get_db)):
    return db.query(Alert).order_by(Alert.created_at.desc()).limit(10).all()
