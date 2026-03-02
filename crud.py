from sqlalchemy.orm import Session
from model import Portal, User
from schema import PortalCreate


def create_portal(db: Session, portal: PortalCreate):
    owner_id = portal.owner_id
    owner_name = portal.owner_name if portal.owner_name else f'User {owner_id}'
    owner_email = portal.owner_email if portal.owner_email else f'user{owner_id}@test.com'

    # AUTO-CREATE USER
    user = db.query(User).filter(User.id == owner_id).first()
    if not user:
        user = User(id=owner_id, name=owner_name, email=owner_email)
        db.add(user)
        db.commit()
        db.refresh(user)

    # Create portal with YOUR owner_id from request!
    portal_data = {
        'name': portal.name,
        'description': portal.description,
        'start_date': portal.start_date,
        'target_end_date': portal.target_end_date,
        'owner_id': owner_id
    }
    db_portal = Portal(**portal_data)

    db.add(db_portal)
    db.commit()
    db.refresh(db_portal)

    return {
        "id": db_portal.id,
        "name": db_portal.name,
        "description": db_portal.description,
        "owner_id": db_portal.owner_id,
        "owner_name": owner_name,
        "start_date": str(db_portal.start_date) if db_portal.start_date else None,
        "target_end_date": str(db_portal.target_end_date) if db_portal.target_end_date else None,
        "created_at": db_portal.created_at.isoformat() if db_portal.created_at else None
    }
def get_user_portals(db: Session, owner_id: int):
    return db.query(Portal).filter(Portal.owner_id == owner_id).all()