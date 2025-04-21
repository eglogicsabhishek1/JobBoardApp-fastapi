from fastapi import APIRouter,Depends
from JobBoardApp.database import sessionlocal
from . import schema,models
from sqlalchemy.orm import Session
from typing import List, Annotated
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

router = APIRouter(prefix="/auth", tags=["Authetication of users"])
security = HTTPBasic()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/create_user')
async def Create_New_user(user:schema.createUser,db: Session=(Depends(get_db)))->dict:
    db_user = models.user(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message":"New User is created successfully"}

@router.post('/login_user')
async def Login_User(user: schema.LoginUser, db: Session = Depends(get_db)):
    db_user = db.query(models.user).filter(models.user.username == user.username).first()
    
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not secrets.compare_digest(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    return {"message": f"Hello {db_user.username}"}