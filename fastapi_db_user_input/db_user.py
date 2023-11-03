from model import DBUser
from user_data import user_data_base
from sqlalchemy.orm import Session
from database import session
from sqlalchemy import update,delete
from fastapi import HTTPException,status

class crud():
    def create_user(self,request:user_data_base,db:Session):
        new_user=DBUser(
            username=request.username,
            password=request.password,
            email=request.email
        )
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    def fetchdata(self,id):
        fetchone=session.query(DBUser).filter(DBUser.id==id).first()
        if fetchone:
            return fetchone
        else:
            return "ID not found"
       
    
    
    def update_data(self,id,username,password,email):
        update_data=update(DBUser).filter(DBUser.id==id).values(username=username,password=password,email=email)
        s=session.execute(update_data)
        return update_data
    
    
    def deletedata(self,id):
        fetchone=session.query(DBUser).filter(DBUser.id==id).first()
        print(fetchone,"========================================")
        if fetchone:
            delete_data=delete(DBUser).filter(DBUser.id==id)
            session.execute(delete_data)
            return "deleted"
        else:
            return "ID not found"