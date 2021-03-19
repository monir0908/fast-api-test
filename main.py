from typing import List
from datetime import datetime
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from fastapi.responses import JSONResponse
import models, schemas
from database import SessionLocal, engine
from models import Order, Purchase

now = datetime.utcnow()
from pydantic import BaseModel

import sqlalchemy
import databases
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)



models.Base.metadata.create_all(bind=engine)
DATABASE_URL = "postgresql://postgres:123456@localhost:5432/fastapiDB"
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()
testtable = sqlalchemy.Table(
    "testtable",
    metadata,
    sqlalchemy.Column("id",sqlalchemy.Integer, primary_key = True),
    sqlalchemy.Column("test_code",sqlalchemy.String(500))
)
metadata.create_all(engine)



engine = sqlalchemy.create_engine(DATABASE_URL)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.get("/orders/", response_model=List[schemas.Order])
def show_orders(db: Session = Depends(get_db)):
    orders = db.query(models.Order).all()
    return orders


@app.post("/save-order/")
def create_order(order: schemas.Order, db: Session = Depends(get_db)):    
    q = models.Order(order_code=order.order_code, order_date=now)
    db.add(q)
    db.commit()
    db.refresh(q)
    return q

@app.get("/test/")
def main():
    return RedirectResponse(url="/docs/")

@app.get('/test2/{msg}')
def test(msg:int):
    return{'msg':msg}

@app.get("/testtable/", response_model=List[schemas.t])
async def read_notes():
    query = testtable.select()
    return await database.fetch_all(query)