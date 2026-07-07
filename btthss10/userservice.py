from models import ShipmentModel
from schemas import ShipmentCreate
from sqlalchemy.orm import Session

def create_shipment(ship: ShipmentCreate, db: Session):
    check = db.query(ShipmentModel).filter(ShipmentModel.tracking_number == ship.tracking_number).first()
    if check is not None:
        return None          # trùng -> trả None
    new_shipment = ShipmentModel(tracking_number=ship.tracking_number)
    db.add(new_shipment)
    db.commit()
    db.refresh(new_shipment)
    return new_shipment      # tạo mới thành công -> trả object

def show_all(db: Session):
    return db.query(ShipmentModel).all()