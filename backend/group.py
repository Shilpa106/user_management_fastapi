from sqlalchemy.orm import Session
import models
from fastapi import status,HTTPException
def get_all(db:Session):
    groups =db.query(models.Group).all()
    # groups = db.query(models.User).filter(models.User.tenant_id == tenant_id).first()
    return groups


def create(request,db:Session):
    creates = models.Group(tenant_id=request.tenant_id,name=request.name)
    db.add(creates)
    db.commit()
    db.refresh(creates)
    return creates

def add_user(request,db:Session):
    add_users = models.Groupuser(group_id=request.group_id,user_id=request.user_id)
    db.add(add_users)
    db.commit()
    db.refresh(add_users)
    return add_users

def show(tenant_id,db):
    shows = db.query(models.Group).filter(models.Group.tenant_id == tenant_id).first()
    if not shows:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Group with id {tenant_id} is not avaialble")
    return shows

def destroy(id,db):
    destroys = db.query(models.Group).filter(models.Group.id == id)

    if not destroys.first():
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,detail=f"Group with id {id} is not avaialble")
    destroys.delete(synchronize_session=False)
    db.commit()
    return {'done'}

def update(id,request,db):
    updates = db.query(models.Group).filter(models.Group.id == id)
    if not updates.first():
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,detail=f"Group with id {id} is not avaialble")
    updates.update(request)
    db.commit()
    return {'update'}