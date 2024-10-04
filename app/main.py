from fastapi import FastAPI
from .database import engine, Base
from .routers.products import router as product_router
from .routers.suppliers import router as supplier_router
from .routers.customers import router as customer_router
from .routers.orders import router as order_router
from .routers.shipments import router as shipment_router
from .routers.categories import router as category_router
from .routers.order_items import router as order_item_router  

app = FastAPI()


Base.metadata.create_all(bind=engine)


app.include_router(product_router, prefix="/products", tags=["products"])
app.include_router(supplier_router, prefix="/suppliers", tags=["suppliers"])
app.include_router(customer_router, prefix="/customers", tags=["customers"])
app.include_router(order_router, prefix="/orders", tags=["orders"])
app.include_router(shipment_router, prefix="/shipments", tags=["shipments"])
app.include_router(category_router, prefix="/categories", tags=["categories"])
app.include_router(order_item_router, prefix="/order-items", tags=["order items"])  


@app.get("/")
async def read_root():
    return {"message": "Welcome to Madina API!"}
