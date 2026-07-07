from pydantic import BaseModel

class ShipmentCreate(BaseModel):
    tracking_number: str

class ShipmentResponse(BaseModel):
    id: int
    tracking_number: str
    status: str

    class Config():
        from_attributes=True