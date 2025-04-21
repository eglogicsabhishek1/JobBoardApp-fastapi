from sqlalchemy import Column,Integer,String,Date,Float
from .database import Base

class job(Base):
    __tablename__  = "job_posting"
    id =  Column(Integer,primary_key = True,index=True)
    title = Column(String,nullable=True)
    description = Column(String,nullable=True)
    company = Column(String,nullable=True)
    location =Column(String,nullable=True)
    salary =Column(Float,nullable=True)
    posted_date = Column(Date)




















      