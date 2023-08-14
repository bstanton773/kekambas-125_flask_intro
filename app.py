from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)


# Add a route
@app.route('/')
def index():
    return 'Hello World!!!!!!!!'

@app.route('/new')
def new():
    name = 'Brian' + ' ' + 'Stanton'
    return f'This is a new route! How are you, {name}?'
