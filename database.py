import databases, sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import urllib


host_server = os.environ.get('host', 'database-ee.cfyme5ng2cuo.eu-west-1.rds.amazonaws.com')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
database_name = os.environ.get('database_name', 'postgres')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'postgres')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', 'postgres123')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))

SQLALCHEMY_DATABASE_URL  = 'postgres://{}:{}@{}:{}/{}'.format(db_username, db_password, host_server, db_server_port, database_name)
# SQLALCHEMY_DATABASE_URL = "postgresql://myuser1:mypass@127.0.0.1:5432/usersaas"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

