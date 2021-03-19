from datetime import date
from pydantic import BaseModel


class Order(BaseModel):
    id: int
    order_code: str
    order_date: date

    class Config:
        orm_mode = True



class Product(BaseModel):
    id: int
    product_code: str
    product_name: str

    class Config:
        orm_mode = True

class Testtable(BaseModel):
    id: int
    test_code: str