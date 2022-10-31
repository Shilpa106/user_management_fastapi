from fastapi import APIRouter,Depends,status,HTTPException,UploadFile,File
from typing import List,Optional
import schemas
from sqlalchemy.orm import Session
from database import get_db
from backend import user
from awscognito import getuser,user_del,listuser,user_filter

router=APIRouter(
    tags=["User"],
    prefix="/User"
)



# @router.get('/',response_model=List[schemas.ShowUser],status_code=status.HTTP_200_OK)
# def all(db: Session=Depends(get_db)):
#     return user.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.User,db:Session=Depends(get_db)):
    return user.create(request, db)

# @router.get('/{id}',response_model=schemas.ShowUser,status_code=status.HTTP_200_OK)
# def show(id, db:Session=Depends(get_db)):
#     return user.show(id, db)

@router.put('/{id}',status_code=status.HTTP_200_OK)
def update(id, request:schemas.User):
    return user.update(id, request)




@router.post("/bulkupload/{id}",status_code=status.HTTP_201_CREATED)
def check(id,file: UploadFile = File(...), db:Session=Depends(get_db)):
    print(id)

    return user.bluckupload(file,db,id)
@router.get('/cognito_userlist',status_code=status.HTTP_200_OK)
def userlist():
    user=listuser.list_user()
    return user

@router.delete('/cognito{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id,db:Session=Depends(get_db)):
    users= user_del.user_delete(id)
    del_user=user.destroy(id, db)
    return del_user

@router.get('/cognito{id}',status_code=status.HTTP_200_OK)
def get_user(id):
   user=getuser.users_get(id)
   return user



@router.get("/cognito/userlist/")
async def read_item(q: Optional[str] = None):
    item = {"item_id": q}
    if q:
        item.update({"q": id})
        user = user_filter.filter_user(q)
        return user





