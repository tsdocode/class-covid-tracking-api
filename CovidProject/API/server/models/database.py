from sqlalchemy import Integer, String, DateTime, ForeignKey
from sqlalchemy.sql.schema import Column
from server.database import Base
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = 'students'
    mssv = Column(Integer, primary_key=True)
    fullName = Column(String, nullable=False)
    classCode = Column(String, nullable=False)
    positive = relationship("Positive", back_populates="student", uselist=False)

class Positive(Base):
    __tablename__ = 'positives'
    mssv = Column(Integer, ForeignKey('students.mssv'), primary_key=True)
    firstTestDay = Column(DateTime, nullable=False)
    negativeDay = Column(DateTime, nullable=True)
    student = relationship("Student", back_populates="positive", uselist=False)
    
