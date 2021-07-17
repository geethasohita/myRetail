from app import app, db


@app.route('/')
def index():
    db.example.insert_one({'message': 'test message'})
    return 'Welcome to myRetail'
