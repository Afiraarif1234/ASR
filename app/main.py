from fastapi import FastAPI
from app.database import engine

from app.models import Base
from app.database import engine   # assuming this is where your engine is

Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "ASR API is running"}


# include your routers
