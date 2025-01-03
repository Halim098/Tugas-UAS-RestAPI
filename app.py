from flask import Flask, jsonify, request
from models import db, User, Book, Order
from utils import generate_token, verify_token
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mXK8f5R32A3awd4W@mlvjbuusruadndqlhyop.supabase.co:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password, email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        token = generate_token(user.id)
        return jsonify({"token": token})
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/books', methods=['GET', 'POST'])
def manage_books():
    if request.method == 'POST':
        token = request.headers.get('Authorization')
        if not verify_token(token):
            return jsonify({"message": "Unauthorized"}), 401
        data = request.json
        new_book = Book(title=data['title'], author=data['author'], price=data['price'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Book added successfully!"})
    books = Book.query.all()
    return jsonify([{"id": b.id, "title": b.title, "author": b.author, "price": b.price} for b in books])

@app.route('/orders', methods=['POST'])
def create_order():
    token = request.headers.get('Authorization')
    user_id = verify_token(token)
    if not user_id:
        return jsonify({"message": "Unauthorized"}), 401
    data = request.json
    new_order = Order(user_id=user_id, book_id=data['book_id'], order_date=data['order_date'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({"message": "Order placed successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
