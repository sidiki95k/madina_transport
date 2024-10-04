from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import get_db  

router = APIRouter()


@router.post("/", response_model=schemas.OrderItem)
async def create_order_item(order_item: schemas.OrderItemCreate, db: Session = Depends(get_db)):
    db_order_item = models.OrderItem(**order_item.dict())
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item


@router.get("/", response_model=List[schemas.OrderItem])
async def read_order_items(db: Session = Depends(get_db)):
    return db.query(models.OrderItem).all()


@router.get("/{order_item_id}", response_model=schemas.OrderItem)
async def read_order_item(order_item_id: int, db: Session = Depends(get_db)):
    order_item = db.query(models.OrderItem).filter(models.OrderItem.id == order_item_id).first()
    if order_item is None:
        raise HTTPException(status_code=404, detail="Order item not found")
    return order_item


@router.put("/{order_item_id}", response_model=schemas.OrderItem)
async def update_order_item(order_item_id: int, order_item: schemas.OrderItemUpdate, db: Session = Depends(get_db)):
    db_order_item = db.query(models.OrderItem).filter(models.OrderItem.id == order_item_id).first()
    if db_order_item is None:
        raise HTTPException(status_code=404, detail="Order item not found")
    
    for key, value in order_item.dict(exclude_unset=True).items():
        setattr(db_order_item, key, value)
    
    db.commit()
    db.refresh(db_order_item)
    return db_order_item


@router.delete("/{order_item_id}", response_model=schemas.OrderItem)
async def delete_order_item(order_item_id: int, db: Session = Depends(get_db)):
    db_order_item = db.query(models.OrderItem).filter(models.OrderItem.id == order_item_id).first()
    if db_order_item is None:
        raise HTTPException(status_code=404, detail="Order item not found")
    
    db.delete(db_order_item)
    db.commit()
    return db_order_item
