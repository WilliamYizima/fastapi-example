from typing import List
import datetime

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from msgls.ext.model import StatusMessage as model_StatusMessage
from msgls.ext.schemas import StatusMessage as schemas_StatusMessage 
from msgls.ext.db import SessionLocal, engine


app = FastAPI()

model_StatusMessage.Base.metadata.create_all(bind=engine)

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
    db_status_message = model_StatusMessage.StatusMessage(
                    created_at=datetime.datetime.now(),
                    updated_at=datetime.datetime.now(),
                    status=schemas_StatusMessage.StatusName.not_sended
                    )
    db.add(db_status_message)
    db.commit()
    db.refresh(db_status_message)
    return db_status_message


@app.get("/records/", response_model=List[schemas_StatusMessage.StatusMessage])
def show_records(db: Session = Depends(get_db)):
    records = db.query(model_StatusMessage.StatusMessage).all()
    return records