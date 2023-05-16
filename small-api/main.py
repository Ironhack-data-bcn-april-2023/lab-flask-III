from flask import Flask, request, jsonify
import random

import config.sql_connection as conn
import tools.sql_queries as queries
import pandas as pd


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/random-number")
def random_int ():
    x = random.randint(0, 10)
    return f"{x}"

@app.route("/everything-employees")
def example():
    return queries.get_everything()

@app.route("/table/<tablename>")
def ultima(tablename):
    return queries.table_ten(tablename)

@app.route("/insert-into-employees", methods=["POST"])
def seed():
    dict_ = {
    "emp_no": request.args["emp_no"],
    "birth_date": request.args["birth_date"],
    "first_name": request.args["first_name"],
    "last_name": request.args["last_name"],
    "gender": request.args["gender"],
    "hire_date": request.args["hire_date"]
    } 
    return queries.insert_data(dict_)

if __name__ == "__main__":
     app.run(port=9000, debug=True)