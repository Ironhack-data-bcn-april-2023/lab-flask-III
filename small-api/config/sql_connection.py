import sqlalchemy as alch

from getpass import getpass
from dotenv import load_dotenv
import os

# Hidding my token for FourSquare
load_dotenv()
sql_pass = os.getenv('sql_pass')

def connection_to_sql ():
    password = sql_pass
    dbName = "employees"
    connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
    engine = alch.create_engine(connectionData)
    return engine