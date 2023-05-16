import sqlalchemy as alch
from dotenv import load_dotenv
import os
load_dotenv()


def connection_to_sql ():
    password = os.getenv("password")
    dbName = "employees"
    connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
    engine = alch.create_engine(connectionData)
    return engine


def connection_to_sql_sakila ():
    password = os.getenv("password")
    dbName = "employees"
    connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
    engine = alch.create_engine(connectionData)
    return engine

