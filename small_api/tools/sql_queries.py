import pandas as pd
import config.sql_connection as conn
import tools.sql_queries as sql
from config.sql_connection import engine



def get_everything():
    query = f"SELECT * FROM salaries LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")

def add_employee(dict_):
    emp_no =  dict_["emp_no"]
    birth_date = dict_["birth_date"]
    first_name = dict_["first_name"]
    last_name = dict_["last_name"]
    gender = dict_["gender"]
    hire_date = dict_["hire_date"]
    query = f"INSERT INTO employees values ('{emp_no}', '{birth_date}', '{first_name}', '{last_name}', '{gender}', '{hire_date}')"
    engine = conn.connection_to_sql()
    engine.execute(query)
    return "DONE!"

def table_ten(ten):
    query = f"SELECT * FROM  {ten} LIMIT 10;"
    df = pd.read_sql_query(query, engine)
    return df.to_dict("remployees")
