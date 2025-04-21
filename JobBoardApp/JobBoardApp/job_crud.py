from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from . import models, schema


def createJob(job: schema.jobCreate, db: Session) -> str:

    db_job = db.query(models.job).filter(models.job.title == job.title).first()
    if db_job:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Job with this title already exists"
        )

    db_job = models.job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    
    return {"message": "New Job is created successfully"}


def get_Job(db: Session):
    return db.query(models.job).all()

def job_by_id(id: int, db: Session):
    db_job = db.query(models.job).filter(models.job.id == id).first()
    

    if db_job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    
    return db_job


def update_job(id: int, db: Session, data: schema.updateJob):
    db_job = db.query(models.job).filter(models.job.id == id).first()


    if db_job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    

    for key, value in data.dict(exclude_unset=True).items():
        setattr(db_job, key, value)
    
    db.commit()
    db.refresh(db_job)
    
    return {"message": "Job is updated successfully"}

def delte_job(id: int, db: Session):

    db_job = db.query(models.job).filter(models.job.id == id).first()

    if db_job is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Job not found"
        )
    

    db.delete(db_job)
    db.commit() 
    
    return {"message": "Job is deleted successfully"}
