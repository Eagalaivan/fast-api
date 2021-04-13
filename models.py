from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base




class Jobs(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    job_description = Column(String)
    is_active = Column(Boolean, default=True)

class Candidates(Base):
    __tablename__ = "candidates"
    c_id = Column(Integer, primary_key=True, index=True)
    c_name = Column(String)
    c_degree =Column(String)
    id = Column(Integer, ForeignKey("jobs.id"))
    
class Jobapplications(Base):
    __tablename__="jobapplication"
    job_application_id=Column(Integer,primary_key=True,index=True)
    j_id=Column(Integer,ForeignKey("candidates.c_id"))    
