from typing import List
from datetime import datetime
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from fastapi.responses import JSONResponse
import models, schemas
from database import SessionLocal, engine
from models import Order
models.Base.metadata.create_all(bind=engine)
now = datetime.utcnow()
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/orders/", response_model=List[schemas.Order])
def show_orders(db: Session = Depends(get_db)):
    orders = db.query(models.Order).all()
    return orders

# @app.post("/save-order/")
# def create_order(order: Order, db: Session = Depends(get_db)):
#     query = Order.insert().values(order_code=order.order_code, order_date=now)
#     last_record_id = db.execute(query)
#     # return {**order.dict(), "id": last_record_id}
#     # return JSONResponse({"msg": "hello"})
#     return {"message": "Hello World"}

@app.get("/test/")
def main():
    return RedirectResponse(url="/docs/")