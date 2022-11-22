# `Database Connector`

The `db_connector` is a python package to connect with different database backends and perform CRUD and other filltering operations.

## Install & Usage

You can install `db_connector` as follows:

```
pip install -i https://test.pypi.org/simple/ db-connector
```
Example Usage

```
from db_connector import MySqlDBConnector


mysql_connector = MySqlDBConnector(
    user="username",
    password="password",
    host="localhost",
    database="database_name"
)
students = mysql_connector.fetch_all("select * from `students` where class = %s;", (class_id,))
```

## Database Support
- MySQL

## Features
- Fetch All Records
- Fetch One Record
- Automatic and Optimized DB connection management
- Prevention from Injections
- Return all records in the form of python Dict object
