from flask import Flask, request, jsonify
import tools.sql_queries as sql

app = Flask(__name__)   
    
@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/insert-into-employees")
def insert_employees():
    return "This is the df"

@app.route("/insert-into-employees", methods = ["POST"])
def insert_into_employees():
    my_params = request.args
    sql.add_employee(my_params)
    return "ALL DONE!"

if __name__ == "__main__":
    app.run(port=3003, debug=False)