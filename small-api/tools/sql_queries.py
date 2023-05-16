import pandas as pd
import config.sql_connection as conn


def get_everything():
    query = "SELECT * FROM salaries LIMIT 10;"
    engine = conn.connection_to_sql()
    df = pd.read_sql_query(query, engine)
    data = df.to_dict(orient="records")
    return  data

def table_ten(table):
    query = f"SELECT * FROM {table} LIMIT 10;"
    engine = conn.connection_to_sql()
    df = pd.read_sql_query(query, engine)
    data = df.to_dict(orient="records")
    return data

def insert_data(dict_):
    emp_no = dict_["emp_no"]
    birth_date = dict_["birth_date"]
    first_name = dict_["first_name"]
    last_name = dict_["last_name"]
    gender = dict_["gender"]
    hire_date = dict_["hire_date"]

    query = f"INSERT INTO employees VALUES ('{emp_no}', '{birth_date}', '{first_name}', '{last_name}', '{gender}', '{hire_date}');"
    engine = conn.connection_to_sql()
    engine.execute(query)
    return "Inserted!"
    