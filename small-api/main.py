from flask import Flask, jsonify, request
import requests
import random
import tools.sql_queries as sql
import config.sql_connection as conn

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/random-number")
def random_int():
    return str(random.randint(0, 10))


@app.route("/everything-employees")
def example():
    return sql.get_everything()


@app.route("/table/<one_table>")
def table(one_table):
    return str(sql.table_ten(one_table))

@app.route("/insert-into-employees", methods=["POST"])
def inserts_into_db():
    
    dict_ = {
    "emp_no": request.args["emp_no"],
    "birth_date": request.args["birth_date"],
    "first_name": request.args["first_name"],
    "last_name": request.args["last_name"],
    "gender": request.args["gender"],
    "hire_date": request.args["hire_date"]
    } 

    return sql.insert_into_employees(dict_)




if __name__ == "__main__":
    app.run(port=9000, debug=False)