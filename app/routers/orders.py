
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas
from ..database import get_db
from ..models import Order, OrderItem

router = APIRouter()

@router.post("/", response_model=schemas.Order)
async def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
   
    db_order = Order(
        customer_id=order.customer_id,
        total_amount=order.total_amount,
        customer_name=order.customer_name,
        order_date=order.order_date,  
        status=order.status
    )
    
    
    db.add(db_order)

    try:
        db.commit()  
        db.refresh(db_order)  
    except Exception as e:
        db.rollback()  
        print(f"Error occurred while inserting order: {e}")  
        raise HTTPException(status_code=400, detail=str(e))
    
    
    for item in order.order_items:  
        order_item = OrderItem(
            order_id=db_order.id,  
            product_id=item.product_id,
            quantity=item.quantity
        )
        db.add(order_item)  

    try:
        db.commit()  
    except Exception as e:
        db.rollback()  
        print(f"Error occurred while committing order items: {e}")  
        raise HTTPException(status_code=400, detail=str(e))

   
    db_order.order_items = [schemas.OrderItem.from_orm(item) for item in db_order.order_items]  
    return schemas.Order.from_orm(db_order)

@router.get("/", response_model=list[schemas.Order])
async def read_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
   
    for order in orders:
        order.order_items = [schemas.OrderItem.from_orm(item) for item in order.order_items]
    return [schemas.Order.from_orm(order) for order in orders]

@router.get("/{order_id}", response_model=schemas.Order)
async def read_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter(Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    order.order_items = [schemas.OrderItem.from_orm(item) for item in order.order_items]  
    return schemas.Order.from_orm(order)

@router.put("/{order_id}", response_model=schemas.Order)
async def update_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    for key, value in order.dict(exclude_unset=True).items():
        setattr(db_order, key, value)
    
    db.commit()
    db.refresh(db_order)

    db_order.order_items = [schemas.OrderItem.from_orm(item) for item in db_order.order_items]   
    return schemas.Order.from_orm(db_order)

@router.delete("/{order_id}")
async def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    db.delete(db_order)
    db.commit()
    return {"message": f"Order {order_id} deleted"}
