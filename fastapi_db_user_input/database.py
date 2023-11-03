from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

SQLALCHEMY_DATABASE_URL="mysql+pymysql://root@localhost/fastapidb"
engine=create_engine(   
    SQLALCHEMY_DATABASE_URL,connect_args={}
)

sessionaLocal=sessionmaker(bind=engine,autocommit=False, autoflush=False,)
session=sessionaLocal()


Base=declarative_base()

def get_db():
    db=sessionaLocal()
    try:
        yield db
    finally:
        db.close()