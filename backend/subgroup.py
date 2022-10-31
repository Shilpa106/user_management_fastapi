from sqlalchemy.orm import Session
import models

from fastapi import status,HTTPException
# user get data
def get_all(db:Session):
    get_alls =db.query(models.SubGroup).all()
    return get_alls

# user post and save data
def create(request,db:Session):
    creates = models.SubGroup(group_id=request.group_id,name=request.name,tenant_id=request.tenant_id)
    db.add(creates)
    db.commit()
    db.refresh(creates)
    return creates
# user get data by id
def show(tenant_id,db):
    shows = db.query(models.SubGroup).filter(models.SubGroup.tenant_id == tenant_id).first()
    if not shows:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"SubGroupssss with id {tenant_id} is not avaialble")
    return shows
# user update data by id
def update(id,request,db):
    updates = db.query(models.SubGroup).filter(models.SubGroup.id == id)
    if not updates.first():
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,detail=f"SubGroup with id {id} is not avaialble")
    updates.update(request)
    db.commit()
    return {'update'}

def add_user(request,db:Session):
    add_users = models.Subgroup_user(subgroup_id=request.subgroup_id,user_id=request.user_id)
    db.add(add_users)
    db.commit()
    db.refresh(add_users)
    return add_users

def destroy(id,db):
    destroys = db.query(models.SubGroup).filter(models.SubGroup.id == id)

    if not destroys.first():
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,detail=f"Group with id {id} is not avaialble")
    destroys.delete(synchronize_session=False)
    db.commit()
    return {'done'}