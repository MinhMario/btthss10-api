from fastapi import FastAPI,HTTPException, status, Depends
from sqlalchemy.orm import Session
from database import *
from models import *
from schemas import ShipmentResponse
from userservice import *
from typing import List

app=FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db=LocalSession()
    try:
        yield db
    finally:
        db.close()

@app.post('/shipments', response_model=ShipmentResponse, status_code=status.HTTP_201_CREATED)
def add_shipment(ship: ShipmentCreate, db: Session = Depends(get_db)):
    check = create_shipment(ship, db)
    if check is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Mã vận đơn nay đã được khoi tao trưoc đo'
        )
    return check

@app.get('/shipments', response_model=List[ShipmentResponse], status_code=status.HTTP_200_OK)
def get_all(db: Session = Depends(get_db)):
    return show_all(db)
    