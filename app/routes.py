from app import app
from flask import render_template

# Add a route
@app.route('/')
def index():
    return render_template('index.html', first_name='David')

@app.route('/new')
def new():
    name = 'Brian' + ' ' + 'Stanton'
    return f'This is a new route! How are you, {name}?'