from pydantic import BaseModel
# from sqlalchemy.orm import Session
# session=Session()

class user_data_base(BaseModel):
        username:str
        password:str
        email:str
