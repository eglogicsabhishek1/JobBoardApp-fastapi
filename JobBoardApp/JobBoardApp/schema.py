from pydantic import BaseModel
from datetime import date


class jobBase(BaseModel):
    title : str
    description :str
    company :str
    location :str
    salary :float    
    posted_date :date

class jobCreate(jobBase):
    pass

class ShowJob(jobBase):
    id : int
    
    class Config:
        from_attributes = True

class updateJob(jobBase):
    title :str | None = None
    description :str| None = None
    company :str| None = None
    location :str| None = None
    salary :float | None = None    
    posted_date :date| None = None




