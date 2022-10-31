from sqlalchemy import Column, ForeignKey, Integer, String, DateTime,FileField
from sqlalchemy.orm import relationship
from database import Base
import datetime


class Organization(Base):
    _tablename_ = "organization"

    id=Column(String, primary_key=True, index=True)
    name=Column(String)
    tenant_id = relationship("Tenant", back_populates="org_tenant")


class Tenant(Base):

    __tablename__="tenant"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    company_logo = Column(FileField(100))
    organization_id=Column(String, ForeignKey('organization.id',ondelete='CASCADE'), nullable=False)
    created_date = Column(DateTime,default=datetime.datetime.utcnow)
    updated_date = Column(DateTime,default=datetime.datetime.utcnow)
    g_tenant = relationship("Group", back_populates="g_tenantid")
    user_tenant = relationship("TenantUser", back_populates="user_tenantid")
    org_tenant = relationship("Organization", back_populates="tenant_id")


class Group(Base):
    _tablename_ = "group"

    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    tenant_id = Column(String, ForeignKey('tenant.id',ondelete='CASCADE'), nullable=False)
    group_id=Column(String, ForeignKey('group.id'))
    created_date = Column(DateTime,default=datetime.datetime.utcnow)
    updated_date = Column(DateTime,default=datetime.datetime.utcnow)
    group = relationship("Group")
    g_tenantid = relationship("Tenant", back_populates="g_tenant")
    guser_id= relationship("GroupUsers", back_populates="group_user")


class TenantUser(Base):

    __tablename__="tenantuser"
    id = Column(String, primary_key=True, index=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email=Column(String)
    role_id=Column(String, ForeignKey('role.id',ondelete='CASCADE'), nullable=False)
    tenant_id=Column(String, ForeignKey('tenant.id',ondelete='CASCADE'), nullable=False)
    created_date = Column(DateTime,default=datetime.datetime.utcnow)
    updated_date = Column(DateTime,default=datetime.datetime.utcnow)
    guser_tenant = relationship("GroupUsers", back_populates="guser_tenantid")
    user_tenantid = relationship("Tenant", back_populates="user_tenant")
    role = relationship("Role", back_populates="roleid")


class GroupUsers(Base):

    _tablename_ = "groupusers"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey('tenantuser.id',ondelete='CASCADE'), nullable=False)
    group_id = Column(String, ForeignKey('group.id',ondelete='CASCADE'), nullable=False)
    group_user = relationship("Group", back_populates="guser_id")
    guser_tenantid = relationship("TenantUser", back_populates="guser_tenant")



class Role(Base):
    _tablename_ = "role"

    id=Column(String, primary_key=True, index=True)
    name=Column(String)
    roleid = relationship("TenantUser", back_populates="role")