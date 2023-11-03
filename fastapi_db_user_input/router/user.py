from fastapi import APIRouter,Depends,HTTPException,status,Response
from sqlalchemy.orm import Session
from database import get_db
from user_data import user_data_base
from db_user import crud
obj=crud()


router=APIRouter(prefix='/user',
    tags=['user'])

@router.post('/')
def user(request:user_data_base,db:Session=Depends(get_db)):
    return obj.create_user(request,db)


@router.get('/fetch')
def fetch(id):
    data=obj.fetchdata(id)
    return data

@router.put("/fetchtoupdate")
def update(id,username,password,email):
    obj.update_data(id,username,password,email)
    return "data updated!!!!!!!!"

@router.delete("/delete")
def delete(id):
    data=obj.deletedata(id)
    return data