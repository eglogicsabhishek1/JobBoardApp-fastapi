from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



Database_url = "mysql+mysqlconnector://root:1234@localhost:3306/jobbase"

engine = create_engine(Database_url)
sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base  = declarative_base()
