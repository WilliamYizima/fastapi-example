from typing import List
import datetime

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from msgls.ext.model import model
from msgls.ext.schemas import schemas
from msgls.ext.db import SessionLocal, engine


app = FastAPI()

model.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
# def main():
#     return RedirectResponse(url="/docs/")
def main(
        # user: schemas_StatusMessage.StatusMessage,
        db: Session = Depends(get_db)):
    try:
        db_status_message = model.StatusMessage(
                        created_at=datetime.datetime.now(),
                        updated_at=datetime.datetime.now(),
                        status=schemas.StatusName.not_sended
                        )
        db.add(db_status_message)
        db.commit()
        db.refresh(db_status_message)
        
        return db_status_message
    except Exception as e: 
        
        raise HTTPException(
            status_code=500, 
            detail=e)
        


@app.get("/records/", response_model=List[schemas.StatusMessage])
def show_records(db: Session = Depends(get_db)):
    records = db.query(model.StatusMessage).all()
    return records