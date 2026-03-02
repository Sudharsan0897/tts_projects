from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from model import Portal, User
from schema import PortalCreate, Portal
from crud import create_portal, get_user_portals
from sqlalchemy import func

router = APIRouter(prefix="/portals", tags=["portals"])


def get_current_user(db: Session = Depends(get_db)):
    return type('User', (), {'id': 1, 'name': 'Rajesh K'})()


@router.post("/", response_model=Portal)
def create_portal_endpoint(
        portal: PortalCreate,
        #current_user=Depends(get_current_user),
        db: Session = Depends(get_db)
):
    return create_portal(db, portal)


@router.get("/", response_model=List[Portal])
def list_portals(
        owner_id: Optional[int] = Query(None, description="Filter by owner ID (optional)"),
        current_user=Depends(get_current_user),
        db: Session = Depends(get_db)
):
    # Use provided owner_id OR fallback to current_user
    target_owner_id = owner_id if owner_id else current_user.id

    portals = get_user_portals(db, target_owner_id)
    result = []
    for portal in portals:
        owner = db.query(User.name).filter(User.id == portal.owner_id).first()
        owner_name = owner[0] if owner else "Unknown"
        result.append({
            "id": portal.id,
            "name": portal.name,
            "description": portal.description,
            "owner_id": portal.owner_id,
            "owner_name": owner_name,
            "start_date": portal.start_date,
            "target_end_date": portal.target_end_date,
            "created_at": portal.created_at
        })
    return result
