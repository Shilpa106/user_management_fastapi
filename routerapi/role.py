from fastapi import APIRouter,Depends,status
from typing import List
import schemas
from sqlalchemy.orm import Session
from database import get_db
from backend import role


router=APIRouter(
    tags=["role"],
    prefix="/role"
)



@router.get('/',response_model=List[schemas.ShowRole],status_code=status.HTTP_200_OK)
def all(db: Session=Depends(get_db)):
    return role.get_all(db)



@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Role,db:Session=Depends(get_db)):
    return role.create(request, db)

@router.get('/{id}',response_model=schemas.ShowRole,status_code=status.HTTP_200_OK)
def show(id, db:Session=Depends(get_db)):
    return role.show(id, db)



# @routerapi.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
# def destory(id,db:Session=Depends(get_db)):
#     return role.destroy(id, db)



@router.put('/{id}',status_code=status.HTTP_200_OK)
def update(id, request:schemas.Role,db:Session=Depends(get_db)):
    return role.update(id, request, db)


