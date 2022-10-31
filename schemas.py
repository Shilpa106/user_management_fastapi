from pydantic import BaseModel,EmailStr
from typing import List
class Group(BaseModel):
    tenant_id: str
    name :str


class Group_Update(BaseModel):
    name :str


class User_add(BaseModel):
    group_id :int
    user_id :str


class sub_adduser(BaseModel):
    subgroup_id :int
    user_id :str


class Subgroup(BaseModel):
    name :str
    tenant_id:str
    group_id :int

class Subgroup_Update(BaseModel):
    name :str
    group_id :int

class User(BaseModel):
    id: str
    # subgroup_id: int
    tenant_id: str
    email: str
    role: str
    firstname: str
    lastname: str
    email: str
    password:str
    cell_number:str
    level_twomanager: str
    company_name: str
    account_name: str
    title: str
    country: str
    line_manager: str
    address: str
    department: str
    job_title: str
    date_of_birth: str
    start_date: str
    town:str
    postcode:str


class Role(BaseModel):

    tenant_id: str
    name :str


class ShowSubgroup(BaseModel):
    id:int
    name: str
    group_id: int
    tenant_id:str

    class Config():
        orm_mode=True

class ShowGroup(BaseModel):
    id: int
    tenant_id :str
    name :str
    class Config():
        orm_mode=True


class ShowUser(BaseModel):
    id: str
    # subgroup_id: int
    tenant_id: str
    email: str
    role: str
    class Config():
        orm_mode=True

class ShowRole(BaseModel):
    tenant_id :str
    name :str
    class Config():
        orm_mode=True