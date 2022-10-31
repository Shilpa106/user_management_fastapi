from fastapi import APIRouter,Depends,status,HTTPException
from typing import List,Optional
import schemas
from sqlalchemy.orm import Session
from database import get_db
from backend import group


router=APIRouter(
    tags=["Group"],
    prefix="/group"
)



@router.get('/',response_model=List[schemas.ShowGroup],status_code=status.HTTP_200_OK)
def all(db: Session=Depends(get_db)):
    return group.get_all(db)



@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Group,db:Session=Depends(get_db)):
    return group.create(request, db)

@router.get('/{id}',response_model=schemas.ShowGroup,status_code=status.HTTP_200_OK)
def show(q: Optional[str] = None, db:Session=Depends(get_db)):
    item = {"item_id": q}
    if q:
        item.update({"q": q})
    return group.show(q, db)



@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destory(id,db:Session=Depends(get_db)):
    return group.destroy(id, db)



@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Group_Update,db:Session=Depends(get_db)):
    return group.update(id, request, db)


@router.post('/add user',status_code=status.HTTP_201_CREATED)
def add_user(request:schemas.User_add,db:Session=Depends(get_db)):
    return group.add_user(request, db)