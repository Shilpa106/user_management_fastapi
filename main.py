from database import *
from fastapi import FastAPI
import models

from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from routerapi import group,user,role,subgroup


app = FastAPI(title="usermanagement api",)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.add_middleware(GZipMiddleware)
models.Base.metadata.create_all(bind=engine)



app.include_router(group.router)
app.include_router(subgroup.router)
app.include_router(user.router)
app.include_router(role.router)

