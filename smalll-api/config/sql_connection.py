from dotenv import load_dotenv 
import sqlalchemy as alch
import os
load_dotenv()

def connection_to_sql ():
    password=os.getenv("password") 
    dbName = "employees"
    connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
    engine = alch.create_engine(connectionData)
    return engine