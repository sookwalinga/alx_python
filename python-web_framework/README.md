## Python - Web Framework

1. **What is a Web Framework:**
   A web framework is a software framework designed to aid the development of web applications by providing pre-built structures, tools, and patterns that facilitate tasks like handling HTTP requests, managing databases, and generating dynamic content.

2. **How to build a web framework with Flask:**
   Flask is a Python web framework that can be used to build web applications. However, Flask itself is a web framework and not a tool to build web frameworks.

3. **How to define routes in Flask:**
   In Flask, routes are defined using decorators. For example:

   ```
   from flask import Flask
   app = Flask(__name__)

   @app.route('/')
   def home():
       return 'Hello, World!'
   ```

4. **What is a route:**
   A route is a URL pattern associated with a specific view or function in a web application. It defines how the application responds to specific HTTP requests.

5. **How to handle variables in a route:**
   You can use route parameters to handle variables in Flask. For example:

   ```
   @app.route('/user/<username>')
   def show_user(username):
       return f'User: {username}'
   ```

6. **What is a template:**
   A template is a pre-designed HTML file with placeholders for dynamic content. It allows you to separate the presentation logic from the application logic.

7. **How to create an HTML response in Flask by using a template:**
   Flask uses a template engine (e.g., Jinja2) to render templates. Example:

   ```
   from flask import render_template

   @app.route('/hello/<name>')
   def hello(name):
       return render_template('hello.html', name=name)
   ```

8. **How to create a dynamic template (loops, conditions…):**
   Flask's template engine supports control structures like loops and conditions. Example:

   ```
   {% for item in items %} {{ item }} {% endfor %} {% if condition %} Display
   this if condition is true. {% endif %}
   ```

9. **How to display in HTML data from a MySQL database:**
   You would first need to connect to the MySQL database using a library like `mysql-connector-python`. Retrieve data using queries and then pass it to a template for rendering in HTML. Here's a simplified example:

   ```
   import mysql.connector
   from flask import render_template

   @app.route('/users')
   def show_users():
       connection = mysql.connector.connect(host='localhost', user='username', password='password', database='mydb')
       cursor = connection.cursor()
       cursor.execute('SELECT * FROM users')
       users = cursor.fetchall()
       connection.close()
       return render_template('users.html', users=users)
   ```

   In the `users.html` template, you can then loop through the `users` data and display it in HTML.
