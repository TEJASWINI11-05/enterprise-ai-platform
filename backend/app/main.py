from app.database.models import Base
from fastapi import FastAPI

from app.database.database import engine
from app.database.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Enterprise AI Platform")


@app.get("/")
def home():
    return {
        "message": "Enterprise AI Platform Started Successfully!"
    }