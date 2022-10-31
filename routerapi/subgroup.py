from fastapi import APIRouter,Depends,status
from typing import List,Optional
import schemas
from sqlalchemy.orm import Session
from database import get_db
from backend import subgroup


router=APIRouter(
    tags=["subgroup"],
    prefix="/subgroup"
)



@router.get('/',response_model=List[schemas.ShowSubgroup],status_code=status.HTTP_200_OK)
def all(db: Session=Depends(get_db)):
    return subgroup.get_all(db)



@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Subgroup,db:Session=Depends(get_db)):
    return subgroup.create(request, db)

@router.get('/{id}',response_model=schemas.ShowSubgroup,status_code=status.HTTP_200_OK)
def show(q: Optional[str] = None, db:Session=Depends(get_db)):
    item = {"item_id": q}
    if q:
        item.update({"q": q})
    return subgroup.show(q, db)


@router.put('/{id}',status_code=status.HTTP_200_OK)
def update(id, request:schemas.Subgroup_Update,db:Session=Depends(get_db)):
    return subgroup.update(id, request, db)

@router.post('/subgroup_adduser',status_code=status.HTTP_201_CREATED)
def add_user(request:schemas.sub_adduser,db:Session=Depends(get_db)):
    return subgroup.add_user(request, db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destory(id,db:Session=Depends(get_db)):
    return subgroup.destroy(id, db)