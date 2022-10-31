from sqlalchemy.orm import Session
import models

from fastapi import APIRouter,Depends,status,HTTPException
def get_all(db:Session):
    get_alls =db.query(models.Role).all()
    return get_alls


def create(request,db:Session):
    creates = models.Role(tenant_id=request.tenant_id,name=request.name)
    db.add(creates)
    db.commit()
    db.refresh(creates)
    return creates

def show(id,db):
    shows = db.query(models.Role).filter(models.Role.id == id).first()
    if not shows:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Role with id {id} is not avaialble")
    return shows

def update(id,request,db):
    updates = db.query(models.Role).filter(models.Role.id == id)
    if not updates.first():
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,detail=f"Role with id {id} is not avaialble")
    updates.update(request)
    db.commit()
    return {'update'}