from JobBoardApp.database import Base
from sqlalchemy import Column,Integer,String

class user(Base):
    __tablename__ = "user"
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,nullable=False)
    password = Column(String,nullable=False)
      