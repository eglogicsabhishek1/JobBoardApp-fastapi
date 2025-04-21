from fastapi import APIRouter,Depends
from .database import sessionlocal
from . import job_crud,schema,models
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix="/job", tags=["Job management"])

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/new_job')
async def Create_Job(job:schema.jobCreate,db: Session=(Depends(get_db)))-> dict:
    return job_crud.createJob(job,db)
    

@router.get('/{id}')
async def Job_By_Id(id: int,db: Session =(Depends(get_db)))-> schema.ShowJob:
    return job_crud.job_by_id(id,db)


@router.get('/') 
async def All_Jobs(db: Session =(Depends(get_db)))-> List[schema.ShowJob]:
    return job_crud.get_Job(db)

@router.put('/{id}')
async def Update_Job(id: int, data: schema.updateJob, db: Session = Depends(get_db))->dict:
    return job_crud.update_job(id,db,data)

@router.delete('/{id}')
async def Delete_Job(id:int,db: Session=(Depends(get_db))):
    return job_crud.delte_job(id,db)
    
