from fastapi import FastAPI
from router import user
import model
from database import engine

app=FastAPI()
app.include_router(user.router)

model.Base.metadata.create_all(engine)