![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

## Introduction

On this lab, you will continue working on the API you created on the previous lab. On this lab, you will create a connection to a MySQL database.

The goal is to have this workflow:

Browser endpoints < function defined under endpoint < function that queries < function that establishes connection

This way, we will manage to run SQL queries by just passing one word/one endpoint.

### Iteration 1

Copy the API you created. It should look like this:

```bash
your-code/
    main.ipynb
.gitignore
README.md

small-api/
    main.py
    config/
        sql_connection.py # for now empty
    tools/
        sql_queries.py #for now empty
```

- From your terminal, run `python main.py`
- In that terminal, you'll get feedback of your prints and the errors.
- After the server is up and running you'll be able to go into your browser and access the endpoints you defined.

### Iteration 2

Now, we are going to work with data: we'll establish a connection to the database.

1. Go to your `config/sql_connection.py` file.
2. Establish a connection to MySQL.
   - Import the necessary libraries (SQL alchemy)
   - Use `python-dotenv` & `.env` to load your password.
   - Remember to include your `.env` file in your `.gitignore`.
   - Define the database you want to connect to (let's go with employees)
   - Define an engine :)

### Iteration 3

Now, we want to make sure we can use the engine we defined.

- 1. Go to `tools/sql_queries.py` and import the engine.
- 2. Import the necessary libraries
- 3. Define a function that:
  - is called `get_everything()`
  - takes no arguments
  - selects everything from the table salaries with a limit of 10 and saves it into a df
  - returns the [df as a dict](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html) (mind orient argument).

### Iteration 4

Now, we'll make that function available on the main file.

1. Go to `main.py`
2. Import your sql_queries as sql
3. Create a route with the name `"/everything-employees"`
4. Under that route, define a function with the name `example`
5. The function `example` should defined on iteration 3: `sql.get_everything()`
6. Make sure you jsonify the return of that function
7. Check it works: go to your browser, go to the `"/everything-employees"` endpoint and see if you get the result: you should get a stringified version of a dictionary of 10 elements.

### Iteration 5

Now we'll create an endpoint that has parameters. Create a query that selects 10 elements for any given table.

1. On your `tools/sql_queries.py` define a function that takes one argument. That function should run a query that selects 10 elements from any table in your database. Call it `table_ten()`
2. On your `main.py`
3. Create an route: `table/<one_table>`
4. Under that route, create a function that returns a stringified version of calling table_ten(one_table).

### BONUS

Repeat the same process to connect to mongo.

## Submission

Upon completion, add your deliverables to git. Then commit git and push your branch to the remote.

## Resources

[]()
