from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer,VARCHAR
from database import Base


class DBUser(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(VARCHAR(23))
    password=Column(VARCHAR(23))
    email=Column(VARCHAR(12))
    
