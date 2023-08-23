## Python - Object-relational mapping

1. **How to connect to a MySQL database from a Python script:**
   To connect to a MySQL database from a Python script, you can use the `mysql-connector` library or other similar libraries like `PyMySQL`. You'll need to provide connection details like host, username, password, and database name to establish a connection.

2. **How to SELECT rows in a MySQL table from a Python script:**
   You can use SQL queries within your Python script to retrieve data from a MySQL table. After establishing a connection, you can execute a `SELECT` query using the `cursor` object provided by the connection. The fetched data can be accessed through methods like `fetchone()` or `fetchall()`.

3. **How to INSERT rows in a MySQL table from a Python script:**
   To add data to a MySQL table from a Python script, you'll again use SQL queries. After establishing a connection, you can execute an `INSERT` query using the `cursor` object. Provide the necessary values using placeholders or string formatting to insert data into the table.

4. **What ORM means:**
   ORM stands for Object-Relational Mapping. It's a programming technique that allows you to interact with a database using object-oriented paradigms. An ORM maps database tables to classes and rows to objects, simplifying database interactions and reducing the need to write raw SQL queries.

5. **How to map a Python Class to a MySQL table:**
   Mapping a Python class to a MySQL table involves using an ORM framework like SQLAlchemy or Django's ORM. You define a Python class that represents the table's structure, and the ORM handles the mapping between the class attributes and the table columns. This abstraction enables you to work with database records as Python objects.

Remember, these explanations are concise, so feel free to explore each topic further for more in-depth understanding and implementation details.
