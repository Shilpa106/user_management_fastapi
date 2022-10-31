from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    tenant_id = Column(String)
    created_date = Column(DateTime,default=datetime.datetime.utcnow)
    updated_date = Column(DateTime,default=datetime.datetime.utcnow)
    subgroup = relationship("SubGroup", back_populates="owner")
    addgroup = relationship("Groupuser", back_populates="group")





class SubGroup(Base):
    __tablename__ = "subgroup"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    group_id = Column(Integer, ForeignKey("groups.id", ondelete='CASCADE'), nullable=False)
    tenant_id=Column(String)
    created_date = Column(DateTime,default=datetime.datetime.utcnow)
    updated_date = Column(DateTime,default=datetime.datetime.utcnow)

    owner = relationship("Group", back_populates="subgroup")
    subgroup_user = relationship("Subgroup_user", back_populates="subgroups")

class User(Base):
    __tablename__ = "user"
    id = Column(String, primary_key=True, autoincrement=False)
    email = Column(String,unique=True)
    tenant_id = Column(String)
    role = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    cell_number=Column(String)
    password=Column(String)
    level_twomanager = Column(String)
    company_name = Column(String)
    account_name=Column(String)
    title=Column(String)
    country=Column(String)
    line_manager=Column(String)
    address=Column(String)
    department=Column(String)
    job_title=Column(String)
    date_of_birth=Column(String)
    start_date=Column(String)
    town=Column(String)
    postcode=Column(String)
    created_date = Column(DateTime,default=datetime.datetime.utcnow)
    updated_date = Column(DateTime,default=datetime.datetime.utcnow)
    adduser = relationship("Groupuser", back_populates="user")
    addusers = relationship("Subgroup_user", back_populates="users")




class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(String)
    name = Column(String)
    created_date = Column(DateTime,default=datetime.datetime.utcnow)
    updated_date = Column(DateTime,default=datetime.datetime.utcnow)


class Groupuser(Base):

    __tablename__ = "useradd"
    id = Column(Integer, primary_key=True, index=True)

    group_id = Column(Integer, ForeignKey("groups.id", ondelete='CASCADE'), nullable=False)
    user_id = Column(String, ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="adduser")
    group = relationship("Group",back_populates='addgroup')

class Subgroup_user(Base):

    __tablename__ = "subgroupuser"
    id = Column(Integer, primary_key=True, index=True)
    subgroup_id = Column(Integer, ForeignKey("subgroup.id", ondelete='CASCADE'), nullable=False)
    user_id = Column(String, ForeignKey("user.id"), nullable=False)
    users = relationship("User", back_populates="addusers")
    subgroups = relationship("SubGroup",back_populates='subgroup_user')

