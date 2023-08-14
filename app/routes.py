from app import app

# Add a route
@app.route('/')
def index():
    return 'Hello World!!!!!!!!'

@app.route('/new')
def new():
    name = 'Brian' + ' ' + 'Stanton'
    return f'This is a new route! How are you, {name}?'