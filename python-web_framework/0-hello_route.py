# Import the Flask class from the Flask module
from flask import Flask

# Create an instance of the Flask class and use '__name__' as the module name
app = Flask(__name__)

# Route for the root URL ('/') and disable strict trailing slashes
@app.route('/', strict_slashes=False)
def hello():
    """
    Function to handle requests to the root URL ('/') 
    and return a greeting message.
    :return: A string containing the greeting message.
    """
    return 'Hello HBNB!'

# Check if the script is being run directly (not imported as a module)
if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
