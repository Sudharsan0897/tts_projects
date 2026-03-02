from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class PortalBase(BaseModel):
    owner_id: int
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    target_end_date: Optional[date] = None


class PortalCreate(PortalBase):
    owner_name: Optional[str] = None
    owner_email: Optional[str] = None


class Portal(PortalBase):
    id: int
    owner_id: int
    owner_name: str
    created_at: datetime

    class Config:
        from_attributes = True
