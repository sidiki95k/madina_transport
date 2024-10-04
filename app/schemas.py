from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class ProductBase(BaseModel):
    name: str
    price: float  
    category_id: int

    class Config:
        orm_mode = True
        from_attributes = True  

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True  
        from_attributes = True  



class SupplierBase(BaseModel):
    name: str
    contact_info: str

    class Config:
        orm_mode = True
        from_attributes = True  

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True  



class CustomerBase(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True
        from_attributes = True  

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    pass

class Customer(CustomerBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True  



class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

    class Config:
        orm_mode = True  
        from_attributes = True  

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemUpdate(OrderItemBase):
    pass

class OrderItem(OrderItemBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True 



class OrderBase(BaseModel):
    customer_id: int
    total_amount: float  
    customer_name: str   
    order_date: datetime  
    status: str          
    order_items: List[OrderItemBase]  

    class Config:
        orm_mode = True  
        from_attributes = True  

class OrderCreate(OrderBase):
    pass

class OrderUpdate(OrderBase):
    pass

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True  



class CategoryBase(BaseModel):
    name: str

    class Config:
        orm_mode = True  
        from_attributes = True  

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True  



class ShipmentBase(BaseModel):
    order_id: int 
    shipment_date: datetime  
    amount: float  
    payment_date: datetime  
    payment_method: str  
    status: str  

    class Config:
        orm_mode = True  
        from_attributes = True  


class ShipmentCreate(ShipmentBase):
    pass


class ShipmentUpdate(ShipmentBase):
    pass


class Shipment(ShipmentBase):
    id: int  

    class Config:
        orm_mode = True  
        from_attributes = True  
