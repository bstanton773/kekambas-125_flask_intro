from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)
# Configure our app with a secret key
app.config['SECRET_KEY'] = 'you-will-never-guess'


# import all of the routes from the routes file into the current package
from app import routes
# Must be imported at the bottom of the file
