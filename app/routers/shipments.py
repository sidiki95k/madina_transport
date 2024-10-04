
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from ..models import Shipment

router = APIRouter()

@router.post("/", response_model=schemas.Shipment)
async def create_shipment(shipment: schemas.ShipmentCreate, db: Session = Depends(get_db)):
    db_shipment = Shipment(**shipment.dict())
    db.add(db_shipment)
    db.commit()
    db.refresh(db_shipment)
    return db_shipment

@router.get("/", response_model=list[schemas.Shipment])
async def read_shipments(db: Session = Depends(get_db)):
    return db.query(Shipment).all()

@router.get("/{shipment_id}", response_model=schemas.Shipment)
async def read_shipment(shipment_id: int, db: Session = Depends(get_db)):
    shipment = db.query(Shipment).filter(Shipment.id == shipment_id).first()
    if shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment

@router.put("/{shipment_id}", response_model=schemas.Shipment)
async def update_shipment(shipment_id: int, shipment: schemas.ShipmentUpdate, db: Session = Depends(get_db)):
    db_shipment = db.query(Shipment).filter(Shipment.id == shipment_id).first()
    if db_shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")
    
    for key, value in shipment.dict(exclude_unset=True).items():
        setattr(db_shipment, key, value)
    
    db.commit()
    db.refresh(db_shipment)
    return db_shipment

@router.delete("/{shipment_id}")
async def delete_shipment(shipment_id: int, db: Session = Depends(get_db)):
    db_shipment = db.query(Shipment).filter(Shipment.id == shipment_id).first()
    if db_shipment is None:
        raise HTTPException(status_code=404, detail="Shipment not found")
    
    db.delete(db_shipment)
    db.commit()
    return {"message": f"Shipment {shipment_id} deleted"}
