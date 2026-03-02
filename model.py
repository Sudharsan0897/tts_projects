from datetime import date
from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, Date
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255))
class Portal(Base):
    __tablename__ = "portals"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(500))
    owner_id = Column(Integer, ForeignKey("users.id"))
    start_date = Column(Date)
    target_end_date = Column(Date)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
