from datetime import date
from pydantic import BaseModel


class Order(BaseModel):
    id: int
    order_code: str
    order_date: date

    class Config:
        orm_mode = True