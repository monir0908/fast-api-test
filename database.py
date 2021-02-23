from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456@localhost:5432/fastapiDB"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} # this "check_same_thread" is needed only for sqlite
# )
# metadata = sqlalchemy.MetaData()
# Order = sqlalchemy.Table(
#     "order",
#     metadata,
#     sqlalchemy.Column("id",sqlalchemy.Integer, primary_key = True),
#     sqlalchemy.Column("order_code",sqlalchemy.String(500))
# )
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()