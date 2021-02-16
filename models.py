from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.types import Date
from database import Base


class Order(Base):
    __tablename__ = "Order"

    id = Column(Integer, primary_key=True, index=True)    
    order_code = Column(String(255), index=True)
    order_date = Column(Date)
    amount = Column(Float)