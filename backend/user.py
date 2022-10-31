from sqlalchemy.orm import Session
import models

from awscognito import signup,bulksignup,user_get

from fastapi import status,HTTPException


def get_all(db:Session):
    users =db.query(models.User).all()
    return users
def create(request,db:Session):
    creates= models.User(
        id=request.id,tenant_id=request.tenant_id,cell_number=request.cell_number,
        firstname=request.firstname, lastname=request.lastname,
        email=request.email,password=request.password ,company_name=request.company_name,
        role=request.role, account_name=request.account_name,
        title=request.title, country=request.country,
        line_manager=request.line_manager, address=request.address,
        department=request.department,level_twomanager=request.level_twomanager,
        job_title=request.job_title,date_of_birth=request.date_of_birth,start_date=request.start_date,town=request.town,postcode=request.postcode)

    return signup.handler(request, creates, db)

def saves(request, subid, db:Session):
    user= models.User(id=subid,tenant_id=request.tenant_id,
        email=request.email,
        role=request.role)

    user = db.query(models.User).filter(models.User.email == request.email)
    if user.first():
        raise HTTPException(status_code=status.HTTP_302_FOUND,
                            detail="email is already avaibale please try with unique email")


    db.add(user)
    db.commit()
    db.refresh(user)
    # raise HTTPException(status_code=status.HTTP_201_CREATED, detail="User is Created Sucessfully")
    return user

def show(id,db):
    user= db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Userwith id {id} is not avaialble")
    return user

def destroy(id,db):
    user= db.query(models.User).filter(models.User.id == id)

    if not user.first():
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,detail=f"Userwith id {id} is not avaialble")
    user.delete(synchronize_session=False)
    db.commit()
    return {'done'}

# def update(id,request,db):
#     user= db.query(models.User).filter(models.user.id == id)
#     if not user.first():
#         raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,detail=f"Userwith id {id} is not avaialble")
#     user.update(request)
#     db.commit()
#     return {'update'}

def bluckupload(file,db,id):


    if file.filename.endswith('.csv'):
        return bulksignup.files(file,db,id)
    else:
        raise HTTPException(status_code=404, detail="file is not accpeted ")

def blucksaves(event, subid, db: Session):
    users = models.User(id=subid,tenant_id=event['tenant_id'],
                       email=event['email'],
                       role=event['role']
                       )

    user=db.query(models.User).filter(models.User.email==event['email'])
    if user.first():
        raise HTTPException(status_code=status.HTTP_302_FOUND,detail="email is already avaibale please try with unique email")

    db.add(users)
    db.commit()
    db.refresh(users)
    return users


def update(id,request):
    # print("hey is",id)
    # print("ddddd",request)
    creates= models.User(
        tenant_id=request.tenant_id,cell_number=request.cell_number,
        firstname=request.firstname, lastname=request.lastname,company_name=request.company_name,
        role=request.role, account_name=request.account_name,
        title=request.title, country=request.country,
        line_manager=request.line_manager, address=request.address,
        department=request.department,level_twomanager=request.level_twomanager,
        job_title=request.job_title,date_of_birth=request.date_of_birth,start_date=request.start_date,town=request.town,postcode=request.postcode)

    return user_get.handler(id, creates)

def destroy(id,db):
    destroys = db.query(models.User).filter(models.User.id == id)

    if not destroys.first():
        raise HTTPException(status_code =status.HTTP_404_NOT_FOUND,detail=f"Group with id {id} is not avaialble")
    destroys.delete(synchronize_session=False)
    db.commit()
    return {'done'}