from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.types import Date
from database import Base


class Order(Base):
    __tablename__ = "Order"

    id = Column(Integer, primary_key=True, index=True)    
    order_code = Column(String(255), index=True)
    order_date = Column(Date)
    amount = Column(Float)

class Product(Base):
    __tablename__ = "Product"

    id = Column(Integer, primary_key=True, index=True)    
    product_code = Column(String(255), index=True)
    product_name = Column(String(255))

class Purchase(Base):
    __tablename__ = "Purchase"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("Product.id"))    
    qty = Column(Integer)

class Test(Base):
    __tablename__ = "Test"

    id = Column(Integer, primary_key=True, index=True)
    purchase_id = Column(Integer, ForeignKey("Purchase.id"))    
    qty = Column(Integer)