# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class and use '__name__' as the module name
app = Flask(__name__)

# Decorator to define a route for the root URL ('/') and disable strict trailing slashes
@app.route('/', strict_slashes=False)
def hello():
    # Function to be executed when the root URL is accessed
    return 'Hello HBNB!'

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
